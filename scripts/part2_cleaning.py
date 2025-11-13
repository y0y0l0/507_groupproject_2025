from common_clean_functions import get_all_clean_metrics_records,get_metric_with_most_missing_records,get_athletes_with_at_least_5_measurements_in_selected_metrics,get_athletes_with_5_measurements_not_in_selected_metrics
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
|value                   |DECIMAL(20,6)|Numeric value of the metric                                           |
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
## Identify which of your selected metrics have the most NULL or zero records.
get_all_clean_metrics_records()
get_metric_with_most_missing_records()

## For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total')
get_athletes_with_at_least_5_measurements_in_selected_metrics()
# 459 out of 1287 players have at least 5 measurements 
# Percentage = (459/1287)*100 = 35.67%
get_athletes_with_5_measurements_not_in_selected_metrics()
## Identify athletes who haven't been tested in the last 6 months (for your selected metrics)
#get_athletes_not_tested_in_last_6_months()
## Determine if you have sufficient data to answer your research question




