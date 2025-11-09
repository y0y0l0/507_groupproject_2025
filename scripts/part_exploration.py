#from scripts.common_functions import run_sport_data_query
from scripts.common_functions import get_sports_team_and_counts_for_top_metrics, get_unique_athletes,get_unique_sports,get_unique_date_ranges,get_num_device_records,get_invalid_athletes,get_multi_source_athletes,get_top_metrics_by_source,get_unique_metrics_count,get_date_range_and_counts_for_top_metrics
import platform as platform

'''
1.2 Data Quality Assessment (Group)
|Column                  |Type         |Description                                                                 |
|------------------------|-------------|----------------------------------------------------------------------------|
|id                      |BIGINT       |Unique record identifier (auto-increment)                                   |
|playername              |VARCHAR(255) |Anonymized player identifier (e.g., PLAYER_001, PLAYER_002)                 |
|timestamp               |DATETIME     |Date and time of the measurement/session                                    |
|device                  |VARCHAR(50)  |Specific device/equipment used for measurement                              |
|metric                  |VARCHAR(255) |Name of the performance metric being measured                               |
|value                   |DECIMAL(20,6)|Numeric value of the metric                                                 |
|team                    |VARCHAR(255) |Sport/team affiliation (e.g., Football, Soccer, Basketball)                 |
|session_type            |VARCHAR(255) |Type of session (e.g., Practice, Game, Training) - only relevant for Kinexon|
|session_description     |TEXT         |Detailed description of the session                                         |
|function_description    |VARCHAR(255) |Movement or exercise description                                            |
|data_source             |VARCHAR(50)  |Original data source (Hawkins, Kinexon, or Vald)                            |
|timestamp               |TIMESTAMP    |Record creation timestamp                                                   |
|session_description     |TEXT         |Detailed description of the session                                         |
|function_description    |VARCHAR(255) |Movement or exercise description                                            |
|data_source             |VARCHAR(50)  |Original data source (Hawkins, Kinexon, or Vald)                            |
|created_at              |TIMESTAMP    |Record creation timestamp                                                   |
'''
## How many unique athlete are in the database?
num_unique_athletes = get_unique_athletes()

## How many different sports/teams are represented in the database?
num_unique_sports = get_unique_sports()

## What is the date range of available data?
date_range = get_unique_date_ranges()

## Which data source (Hawkins/Kinexon/Vald) has the most records?
device_count = get_num_device_records()

## Are there any athletes with missing or invalid names?
find_invalid_athletes = get_invalid_athletes()

## How many athletes have data from multiple sources (2 or 3 systems)?
find_multi_source_athletes = get_multi_source_athletes()

'''1.3 Metric Discovery & Selection (Group)'''

## Lists the top 10 most common metrics for Hawkins data (filter by data_source = 'Hawkins')
top_hawkins_metrics = get_top_metrics_by_source('Hawkins',10)

## Lists the top 10 most common metrics for Kinexon data (filter by data_source = 'Kinexon')
top_kinexon_metrics = get_top_metrics_by_source('Kinexon',10)

## Lists the top 10 most common metrics for Vald data (filter by data_source = 'Vald')
top_vald_metrics = get_top_metrics_by_source('Vald',10)

## Identifies how many unique metrics exist across all data sources
unique_metrics_count = get_unique_metrics_count()

## For each data source, show the date range and record count for the top metrics
date_range_and_counts = get_date_range_and_counts_for_top_metrics('Hawkins',10)
date_range_and_counts = get_date_range_and_counts_for_top_metrics('Kinexon',10)
date_range_and_counts = get_date_range_and_counts_for_top_metrics('Vald',10)

## Team question: How many unique teams are represented in the top metrics for each data source?
teams = get_sports_team_and_counts_for_top_metrics('Vald',10)
teams = get_sports_team_and_counts_for_top_metrics('Hawkins',10)    
teams = get_sports_team_and_counts_for_top_metrics('Kinexon',10)


