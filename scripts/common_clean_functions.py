from common_functions import Engine, create_engine, pd, run_sport_data_query


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
    return response.head()

def get_athletes_with_at_least_5_measurements_in_selected_metrics() -> int:
    """Get the percentage of athletes with at least 5 measurements.
    Returns:
        int: The percentage of athletes with at least 5 measurements.
        csv: A CSV file containing all records.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics?
     #"-AND TRIM(metric) in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
    sql_test_query ="SELECT  metric, playername, COUNT(*) as player_counter " \
                        "FROM research_experiment_refactor_test WHERE value IS NOT NULL AND value > 0.0 " \
                        "AND metric in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND REPLACE(team,'\\'','') NOT IN('Unknown','Player Not Found','Graduated (No longer enrolled)') " \
                        "GROUP BY metric, playername " \
                        "HAVING COUNT(*) >= 5 " \
                        "ORDER BY player_counter DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_athletes_with_at_least_5_measurements_in_selected_metrics.csv')
    return response.head()


def get_athletes_with_5_measurements_not_in_selected_metrics() -> int:
    """Get the percentage of athletes with at least 5 measurements.
    Returns:
        int: The percentage of athletes with at least 5 measurements.
        csv: A CSV file containing all records.
    """
    ## For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics?
     #"-AND TRIM(metric) in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
    sql_test_query ="SELECT  metric, playername, COUNT(*) as player_counter " \
                        "FROM research_experiment_refactor_test WHERE value IS NOT NULL AND value > 0.0 " \
                        "AND metric not in ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total') " \
                        "AND REPLACE(team,'\\'','') NOT IN('Unknown','Player Not Found','Graduated (No longer enrolled)') " \
                        "GROUP BY metric, playername " \
                        "HAVING COUNT(*) >= 5 " \
                        "ORDER BY player_counter DESC;"
    response = run_sport_data_query(sql_test_query)

    if not response.empty:
        response.to_csv('output/2.1-2_athletes_with_5_measurements_not_in_metric.csv')
    return response.head()