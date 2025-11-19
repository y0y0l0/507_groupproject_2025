from datetime import timedelta, datetime
import pandas as pd
from common_functions import run_sport_data_query,get_unique_athletes

def get_all_clean_metrics_records() -> int:
    """Get all records from the database with clean metrics.
    Returns:
        int: The number of records retrieved.
        csv: A CSV file containing all records.
    """
    ## How many unique athlete are in the database?
    sql_test_query = "SELECT  metric,data_source, value,REPLACE(team,'\\'','') as team, playername " \
                        "FROM research_experiment_refactor_test WHERE value is not null AND value > 0.0 " \
                        "AND TRIM(metric) in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total')" \
                        "AND TRIM(REPLACE(team,'\\'',''))  not in ('Unknown','Player Not Found','Graduated (No longer enrolled)');"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-1_all_clean_metrics_records.csv')
    return response
def get_metric_with_most_missing_records() -> int:
    """Get a metric with the most missing records.
    Returns:
        int: The number of records retrieved.
        csv: A CSV file containing all records.
    """
    ## Identify which of your selected metrics have the most NULL or zero values?
    sql_test_query = "SELECT COUNT(*) AS count," \
                     " metric, " \
                     " data_source " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE " \
                        "metric " \
                        "IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND (team " \
                        "IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                        "OR (value IS NULL OR value = 0.0) ) " \
                     "GROUP BY metric, data_source " \
                     "ORDER BY COUNT(*) DESC;"
    response = run_sport_data_query(sql_test_query)
    if not response.empty:
        response.to_csv('output/2.1-1_metric_with_most_missing_records.csv')
    return response

def get_athletes_with_at_least_5_measurements_in_selected_metrics() -> int:
    """Get the percentage of athletes with at least 5 measurements per team.
    Returns:
        pd.DataFrame: DataFrame with team, athlete counts, and percentages.
        csv: A CSV file containing results per team.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics?
    sql_test_query = "SELECT REPLACE(t.team, '\\'', '') AS team, " \
                     "COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) AS athletes_with_5_plus, " \
                     "COUNT(DISTINCT playername) AS total_athletes_in_team, " \
                     "ROUND(COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) / " \
                     "COUNT(DISTINCT playername) * 100, 2) AS percentage " \
                     "FROM (SELECT REPLACE(team, '\\'', '') AS team, playername, COUNT(*) AS cnt " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                     "GROUP BY REPLACE(team, '\\'', ''), playername) t " \
                     "GROUP BY REPLACE(t.team, '\\'', '') " \
                     "ORDER BY percentage DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_athletes_with_at_least_5_measurements_in_selected_metrics.csv', index=False)
        print(f"Percentage of athletes with at least 5 measurements per team:")
        for index, row in response.iterrows():
            print(f"  {row['team']}: {row['percentage']}% ({row['athletes_with_5_plus']}/{row['total_athletes_in_team']})")
    return response

def get_athletes_with_5_measurements_not_in_selected_metrics() -> int:
    """Get the percentage of athletes with at least 5 measurements per team for non-selected metrics.
    Returns:
        pd.DataFrame: DataFrame with team, athlete counts, and percentages.
        csv: A CSV file containing results per team.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements not in your selected metrics?
    sql_test_query = "SELECT REPLACE(t.team, '\\'', '') AS team, " \
                     "COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) AS athletes_with_5_plus, " \
                     "COUNT(DISTINCT playername) AS total_athletes_in_team, " \
                     "ROUND(COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) / " \
                     "COUNT(DISTINCT playername) * 100, 2) AS percentage " \
                     "FROM (SELECT REPLACE(team, '\\'', '') AS team, playername, COUNT(*) AS cnt " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND metric NOT IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                     "GROUP BY REPLACE(team, '\\'', ''), playername) t " \
                     "GROUP BY REPLACE(t.team, '\\'', '') " \
                     "ORDER BY percentage DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_athletes_with_5_measurements_not_in_metric.csv', index=False)
        print(f"Percentage of athletes with at least 5 measurements in NON-selected metrics per team:")
        for index, row in response.iterrows():
            print(f"  {row['team']}: {row['percentage']}% ({row['athletes_with_5_plus']}/{row['total_athletes_in_team']})")
    return response

def get_team_percentages_with_athletes_with_at_least_5_measurements() -> int:
    """Get the percentage of athletes with at least 5 measurements for each sport/team.
    Returns:
        int: The percentage of athletes with at least 5 measurements.
        csv: A CSV file containing the results per team.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics?
    sql_test_query = "SELECT REPLACE(t.team, '\\'', '') AS team, " \
                     "COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) AS athletes_with_5_plus, " \
                     "COUNT(DISTINCT playername) AS total_athletes_in_team, " \
                     "ROUND(COUNT(DISTINCT CASE WHEN cnt >= 5 THEN playername END) / " \
                     "COUNT(DISTINCT playername) * 100, 2) AS percentage " \
                     "FROM (SELECT REPLACE(team, '\\'', '') AS team, playername, COUNT(*) AS cnt " \
                     "FROM research_experiment_refactor_test " \
                     "WHERE value IS NOT NULL AND value > 0.0 " \
                     "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                     "AND REPLACE(team, '\\'', '') NOT IN ('Unknown', 'Player Not Found', 'Graduated (No longer enrolled)') " \
                     "GROUP BY REPLACE(team, '\\'', ''), playername) t " \
                     "GROUP BY REPLACE(t.team, '\\'', '') " \
                     "ORDER BY percentage DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_team_percentages_athletes_with_5_measurements.csv', index=False)
        print(f"Team percentages for athletes with at least 5 measurements:")
        for index, row in response.iterrows():
            print(f"  {row['team']}: {row['percentage']}% ({row['athletes_with_5_plus']}/{row['total_athletes_in_team']})")
    return response
def get_athletes_not_tested_in_last_6_months() -> int:
    """Get the percentage of athletes not tested in the last 6 months.
    Returns:
        int: The percentage of athletes not tested in the last 6 months.
        csv: A CSV file containing all records.
    """
    ## get mysql date 6 months ago
    six_months_ago = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d %H:%M:%S')
    ## get athletes who haven't been tested in the last 6 months (for your selected metrics)
    sql_test_query = "SELECT DISTINCT playername, team " \
                        "FROM (SELECT DISTINCT playername, team FROM research_experiment_refactor_test " \
                        "WHERE REPLACE(team,'\\\'','') NOT IN ('Unknown','Player Not Found','Graduated (No longer enrolled)') " \
                        "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total')) AS all_athletes " \
                        "WHERE playername NOT IN (SELECT DISTINCT playername FROM research_experiment_refactor_test " \
                        "WHERE value IS NOT NULL AND value > 0.0 " \
                        "AND metric IN ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND (timestamp >= '" + six_months_ago + "' OR created_at >= '" + six_months_ago + "'));"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-3_athletes_not_tested_in_last_6_months.csv')
        print(f"The percentage of athletes NOT tested in the last 6 months for selected metrics is {response['playername'].nunique()/get_unique_athletes() * 100:.2f}%.")
 
    return response['playername'].unique()
def get_data_in_wide_format_by_athlete_and_metric(input_metric_list: list, input_playername_list: list, format_type: str) -> pd.DataFrame:
    """Get the data in wide format by athlete and metric based on the provides list of metrics and athletes.
    Args:
        input_metric_list (list): List of metrics to filter the data.
        input_playername_list (list): List of player names to filter the data.
        format_type (str): "wide" for wide format, "long" for long format.
    Returns:
        pd.DataFrame: A DataFrame with athletes as rows and metrics as columns.
    """
    ## create a list of metrics and players for the SQL query
    #initnialize empty strings
    metric_list = ""
    playername_list = ""
    #loop through input lists to create single quote comma-separated parameter for metrics and playernames
    for metric in input_metric_list:
        metric_list = metric_list + "\'" + metric + "',"
    metric_list = metric_list.rstrip(",")
    for playername in input_playername_list:
        playername_list = playername_list +"\'" +  playername + "',"
    playername_list = playername_list.rstrip(",")
    print(f"metric_list: {metric_list}")
    print(f"playername_list: {playername_list}")
    ## get player metric data in wide format based on the provided list of metrics requested among clean data sets where the team is valid and the metric is not null.
    sql_test_query = (
        f"SELECT timestamp, metric, value, playername, team "
        f"FROM research_experiment_refactor_test "
        f"WHERE metric IN ({metric_list}) "
        f"AND playername IN ({playername_list}) "
        f"AND value > 0.0 "
        f"AND REPLACE(team,'\\'','') not in ('Unknown','Player Not Found','Graduated (No longer enrolled)') "
        f"ORDER BY playername, timestamp DESC;"
    )
    response = run_sport_data_query(sql_test_query)
    
    if not response.empty:
        # for each athlete in the input list, create a separate csv file
        for player in input_playername_list:
            player_data = response[response['playername'] == player]
            player_data.to_csv(f'output/2.2_{player}_data_in_long_format_by_athlete_and_metric.csv')
            # only create pivoted wide format if requested
            if format_type == "wide":
                player_pivot = player_data.pivot_table(index=['playername', 'timestamp'], columns='metric', values='value').reset_index()
                player_pivot.to_csv(f'output/2.2_{player}_data_in_wide_format_by_athlete_and_metric_pivoted.csv')
            print(f"Sample raw data for athlete {player}")
            for index, row in player_data.iterrows():
                if index < 10 and row['playername'] == player:
                    print(f"  {row['playername']}:{row['timestamp']}:{row['metric']}:{row['value']}")
      
    return response