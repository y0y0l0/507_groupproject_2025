import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv("sqlconfig")

sql_username = os.getenv("SQL_USERNAME")
sql_password = os.getenv("SQL_PASSWORD")
sql_hostname = os.getenv("SQL_HOSTNAME")
sql_database = os.getenv("SQL_DATABASE")
sql_port = os.getenv("SQL_PORT")
sql_test_query = os.getenv("SQL_TEST_QUERY")

url_string = f"mysql+pymysql://{sql_username}:{sql_password}@{sql_hostname}:{sql_port}/{sql_database}"
url_string

conn=create_engine(url_string)

sql_test_query ="select * from research_experiment_refactor_test where playername = 'PLAYER_1084'" 
response = pd.read_sql(sql_test_query, conn)
response 

# get count of records grouped by player and device 
# sql_test_query = 'select count(metric), metric from research _experiment_refractpor test where device = 'vald' group by metric