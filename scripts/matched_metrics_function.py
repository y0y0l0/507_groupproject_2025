"""
Function to match force/torque metrics with accel_load_accum and distance_total by date.
This can be added to common_clean_functions.py or used as a standalone module.
"""

import pandas as pd
from common_functions import run_sport_data_query

def get_matched_metrics_by_date() -> pd.DataFrame:
    """Match force/torque metrics with the earliest following accel_load_accum and distance_total.
    
    This function joins strength metrics (leftMaxForce, rightMaxForce, leftTorque, rightTorque)
    with the earliest accel_load_accum and distance_total measurements that occurred on or after each strength test timestamp.
    
    Returns:
        pd.DataFrame: DataFrame with matched metrics - strength test matched with next accel/distance test.
        csv: A CSV file containing the matched data.
    """
    
    # Get all strength metrics
    strength_query = """
    SELECT 
        timestamp as test_timestamp,
        DATE(timestamp) as test_date,
        playername,
        REPLACE(team, '\\'', '') as team,
        MAX(CASE WHEN metric = 'leftMaxForce' THEN value END) as leftMaxForce,
        MAX(CASE WHEN metric = 'rightMaxForce' THEN value END) as rightMaxForce,
        MAX(CASE WHEN metric = 'leftTorque' THEN value END) as leftTorque,
        MAX(CASE WHEN metric = 'rightTorque' THEN value END) as rightTorque
    FROM research_experiment_refactor_test
    WHERE metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque')
        AND value IS NOT NULL AND value > 0.0
        AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)')
    GROUP BY timestamp, playername, team
    """
    
    # Get all accel/distance metrics
    accel_query = """
    SELECT 
        timestamp as accel_distance_timestamp,
        DATE(timestamp) as accel_distance_test_date,
        playername,
        REPLACE(team, '\\'', '') as team,
        MAX(CASE WHEN metric = 'accel_load_accum' THEN value END) as accel_load_accum,
        MAX(CASE WHEN metric = 'distance_total' THEN value END) as distance_total
    FROM research_experiment_refactor_test
    WHERE metric IN ('accel_load_accum', 'distance_total')
        AND value IS NOT NULL AND value > 0.0
        AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)')
    GROUP BY timestamp, playername, team
    """
    
    print("Fetching strength metrics...")
    strength_df = run_sport_data_query(strength_query)
    print(f"Fetched {len(strength_df)} strength test records")
    
    print("Fetching accel/distance metrics...")
    accel_df = run_sport_data_query(accel_query)
    print(f"Fetched {len(accel_df)} accel/distance test records")
    
    if strength_df.empty or accel_df.empty:
        print("No data found for one or both metric groups.")
        return pd.DataFrame()
    
    # Use pandas merge to find the earliest accel test after strength test
    print("Merging on playername and team...")
    merged = strength_df.merge(
        accel_df,
        on=['playername', 'team'],
        how='inner'
    )
    
    # Filter: only keep accel tests AFTER strength test timestamp
    merged = merged[merged['accel_distance_timestamp'] > merged['test_timestamp']]
    
    # Sort by strength timestamp, then accel timestamp to get earliest accel after
    merged = merged.sort_values(['playername', 'team', 'test_timestamp', 'accel_distance_timestamp'])
    
    # Keep only the first (earliest) accel test after each strength test
    matched = merged.drop_duplicates(
        subset=['test_timestamp', 'playername', 'team'],
        keep='first'
    )
    
    # Reorder columns
    matched = matched[['test_date', 'test_timestamp', 'playername', 'team', 
                       'leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque',
                       'accel_load_accum', 'distance_total', 'accel_distance_test_date', 
                       'accel_distance_timestamp']]
    
    # Sort for output
    matched = matched.sort_values(['test_date', 'team', 'playername'])
    
    if not matched.empty:
        import os
        output_path = os.path.join(os.path.dirname(__file__), '..', 'output', '3.2-2_matched_metrics_by_date_wide_format.csv')
        matched.to_csv(output_path, index=False)
        print(f"\nMatched {len(matched)} strength tests with their following accel/distance measurements.")
        print(f"Output saved to output/3.2-2_matched_metrics_by_date_wide_format.csv")
        print(f"\nFirst 10 rows:")
        print(matched.head(10))
    else:
        print("No matching records found.")
    
    return matched


if __name__ == "__main__":
    matched_data = get_matched_metrics_by_date()
