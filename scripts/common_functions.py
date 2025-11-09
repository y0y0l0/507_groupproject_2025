import pandas as pd
import os
import traceback
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_engine() -> Engine:
    """Create and return a SQLAlchemy Engine using environment variables.

    Raises RuntimeError if required environment variables are missing.
    """

    load_dotenv()

    sql_username = os.getenv("SQL_USERNAME")
    sql_password = os.getenv("SQL_PASSWORD")
    sql_hostname = os.getenv("SQL_HOSTNAME")
    sql_database = os.getenv("SQL_DATABASE")
    sql_port = os.getenv("SQL_PORT")

    # Check required env vars
    pairs = [("SQL_USERNAME", sql_username), ("SQL_PASSWORD", sql_password), ("SQL_HOSTNAME", sql_hostname), ("SQL_DATABASE", sql_database), ("SQL_PORT", sql_port)]
    missing = [name for name, val in pairs if val in (None, "")]
    if missing:
        raise RuntimeError(f"Missing required DB environment variables: {missing}")

    url_string = f"mysql+pymysql://{sql_username}:{sql_password}@{sql_hostname}:{sql_port}/{sql_database}"
    engine = create_engine(url_string)
    return engine


def run_sport_data_query(sql: str, engine: Engine = None) -> pd.DataFrame:
    """Run a SQL query and return the results as a pandas DataFrame.

    If no engine is provided, a new one will be created using get_engine().

    Args:
        sql (str): The SQL query to execute.
        engine (Engine, optional): An existing SQLAlchemy Engine. Defaults to None.

    Returns:
        pd.DataFrame: The query results.
    """

    try:
        if engine is None:
            engine = get_engine()
            
        response = pd.read_sql(sql, engine)
        if response.empty:
            print("Query returned no rows")
        print("Query executed. Shape:", getattr(response, 'shape', None))
        print(response.head(10))
        return response
    except Exception as e:
	    print("Error during diagnostics:", e)
traceback.print_exc()
def get_unique_athletes() -> int:
    """Get the number of unique athletes in the database.

    Returns:
        int: The count of unique athletes.
        csv: A CSV file containing the player names.
    """
    ## How many unique athlete are in the database?
    sql_test_query = "select playername from research_experiment_refactor_test  group by playername order by playername DESC;"
    response = run_sport_data_query(sql_test_query)
    if not response.empty:
        response.to_csv('output/1.2-1_playerNames.csv')
        print(f"There are {response.shape[0]} unique athletesin the database.")
    return 0

def get_unique_sports() -> int:
    """Get the number of unique sports/teams in the database.

    Returns:
        int: The count of unique sports/teams.
        csv: A CSV file containing the sport names.
    """
    sql_query = "SELECT team FROM research_experiment_refactor_test group by team;"
    response = run_sport_data_query(sql_query)
    if not response.empty:
        response.to_csv('output/1.2-2_sportTeams.csv')
        print(f"There are Unique sports/teams {response.shape[0]} in the database.")
    return 0
def get_unique_date_ranges() -> int:
    """Get the date range of available data in the database.

    Returns:
        tuple: The minimum and maximum dates in the database.
    """
    #sql_query = "SELECT playername,timestamp, created_at FROM research_experiment_refactor_test order by playername desc;"
    #response = run_sport_data_query(sql_query)
    #if not response.empty:
    #response.to_csv('output/sessionDateRanges.csv')   -- IGNORE -- this file is too large
    sql_query = "SELECT MIN(created_at) AS min_creation_date, MAX(created_at) AS max_creation_date,MIN(timestamp) AS min_session_date, MAX(timestamp) AS max_session_date FROM research_experiment_refactor_test;"
    response = run_sport_data_query(sql_query)
    if not response.empty:
        #sql_query = "SELECT MIN(created_at) AS min_date, MAX(created_at) AS max_date FROM research_experiment_refactor_test;"
        #response = run_sport_data_query(sql_query)
        #response
        #if not response.empty:
        response.to_csv('output/1.2-3_sessionandCreationDateRanges.csv') 
        print(f"The creation date range of available data: {response.iloc[0]['min_creation_date']} to {response.iloc[0]['max_creation_date']}")
        print(f"The session date range of available data: {response.iloc[0]['min_session_date']} to {response.iloc[0]['max_session_date']}")
    return 0
def get_num_device_records() -> int:
    """Get the count of records for each data source (device) in the database.

    Returns:
        dict: A dictionary with data sources as keys and their record counts as values.
        csv: A CSV file containing the device record counts.
    """
    sql_query = f"SELECT data_source, COUNT(*) AS record_count FROM research_experiment_refactor_test GROUP BY data_source;"
    response = run_sport_data_query(sql_query)
    if not response.empty:
        for index, row in response.iterrows():
            print(f"The data source {response.iloc[index]['data_source']} has {response.iloc[index]['record_count']} records.")
        response.to_csv('output/1.2-4_deviceRecordCounts.csv')
        #print(f"The data source {response.iloc[0]['data_source']} has {response.iloc[0]['record_count']} records.")
        return response.iloc[0]['record_count']
    return 0

def get_invalid_athletes() -> int:
    """Find athletes with missing or invalid names in the database.

    Returns:
        int: The count of invalid athletes.
        csv: A CSV file containing the invalid athlete names.
    """
    sql_query = "SELECT playername FROM research_experiment_refactor_test WHERE playername IS NULL OR playername = '';"
    response = run_sport_data_query(sql_query)
    if not response.empty:
        print(f"There are {response.shape[0]} invalid athletes in the database.")
        response.to_csv('output/1.2-5_invalidAthletes.csv')
    else:
        print("There are no invalid athletes in the database.")
        response.to_csv('output/1.2-5_NoDataFound_invalidAthletes.csv')    
    return response.shape[0]
def get_multi_source_athletes() -> int:
    """Get the count of athletes with data from multiple sources (2 or 3 systems).

    Returns:
        int: The count of athletes with data from multiple sources.
        csv: A CSV file containing the athlete names with multiple sources.
    """
    sql_query = """
    SELECT playername, COUNT(DISTINCT data_source) AS source_count
    FROM research_experiment_refactor_test
    GROUP BY playername
    HAVING source_count >= 2;
    """
    response = run_sport_data_query(sql_query)
    if not response.empty:
        print(f"There are {response.shape[0]} athletes with data from multiple sources.")
        response.to_csv('output/1.2-6_multiSourceAthletes.csv')
    else:
        print("There are no athletes with data from multiple sources.")
        response
    return response.shape[0]

def get_top_metrics_by_source(data_source: str, top_n: int) -> pd.DataFrame:
    """Get the top N most common metrics for a given data source.

    Args:
        data_source (str): The data source to filter by (e.g., 'Hawkins').
        top_n (int): The number of top metrics to return.

    Returns:
        csv: A CSV file containing the top N metrics for the specified data source.
    """
    sql_query = f"""
    SELECT metric,  COUNT(*) AS metric_count
    FROM research_experiment_refactor_test
    WHERE UPPER(data_source) = UPPER('{data_source}')
    GROUP BY metric
    ORDER BY metric_count DESC
    LIMIT {top_n};
    """
    response = run_sport_data_query(sql_query)
    if not response.empty:
        print(f"Top {top_n} metrics for {data_source}:")
        response.to_csv(f'output/1.3-1_top_{top_n}_metrics_{data_source}.csv')
    return 0
def get_unique_metrics_count() -> int:
    """Get the count of unique metrics across all data sources.

    Returns:
        int: The count of unique metrics.
        csv: A CSV file containing the unique metrics.
    """
    sql_query = "SELECT DISTINCT metric FROM research_experiment_refactor_test;"
    response = run_sport_data_query(sql_query)
    if not response.empty:
        print(f"There are {response.shape[0]} unique metrics across all data sources.")
        response.to_csv('output/1.3-2_uniqueMetrics.csv')
    return response.shape[0]
def get_date_range_and_counts_for_top_metrics(data_source: str, top_n: int) -> pd.DataFrame:
    """Get the date range and record count for the top metrics by data source.

    Returns:
        pd.DataFrame: A DataFrame containing the date range and counts for top metrics.
        csv: A CSV file containing the date range and counts for top metrics.
    """
    sql_query =f"""
    SELECT metric, COUNT(*) AS record_count,
            MIN(timestamp) AS min_timestamp,
            MAX(timestamp) AS max_timestamp
    FROM research_experiment_refactor_test
    WHERE UPPER(data_source) = UPPER('{data_source}')
    GROUP BY metric
    ORDER BY COUNT(*) DESC
    LIMIT {top_n};
    """
    print(f"Executing query for {data_source}: {sql_query}")
    response = run_sport_data_query(sql_query);
    if not response.empty:
        print(f"Date min_timestamp {response['min_timestamp'].min()} and max_timestamp {response['max_timestamp'].max()} for top metrics by data source {data_source}.")
        response.to_csv(f'output/1.3-3_date_range_and_counts_top_metrics_{data_source}.csv', index=False)
    return response 
def get_sports_team_and_counts_for_top_metrics(data_source: str, top_n: int) -> pd.DataFrame:
    """Get the date range and record count for the top metrics by data source.

    Returns:
        pd.DataFrame: A DataFrame containing the date range and counts for top metrics.
        csv: A CSV file containing the date range and counts for top metrics.
    """
    sql_query =f"""
    SELECT metric, COUNT(*) AS record_count,
            MAX(team) AS team
    FROM research_experiment_refactor_test
    WHERE UPPER(data_source) = UPPER('{data_source}')
    GROUP BY metric
    ORDER BY COUNT(*) DESC
    LIMIT {top_n};
    """
    print(f"Executing query for {data_source}: {sql_query}")
    response = run_sport_data_query(sql_query);
    if not response.empty:
        print(f"Teams for top metrics by data source {data_source}:")
        response.to_csv(f'output/1.3-4_teams_and_counts_top_metrics_{data_source}.csv', index=False)
    return response 