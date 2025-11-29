import platform as platform
from common_clean_functions import get_data_in_wide_format_by_athlete_and_metric,get_team_percentages_with_athletes_with_at_least_5_measurements,get_athletes_not_tested_in_last_num_days,get_all_clean_metrics_records,get_metric_with_most_missing_records,get_athletes_with_at_least_5_measurements_in_selected_metrics,get_athletes_with_5_measurements_not_in_selected_metrics,get_mean_value_for_each_team
from matched_metrics_function import get_matched_metrics_by_date

'''2.1 Data Understanding Recap (Group)
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

#2.1 Missing Data Analysis (Group)
##2.1-1 Identify which of your selected metrics have the most NULL or zero records.
get_metric_with_most_missing_records()

##2.1-2 For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total')
get_athletes_with_at_least_5_measurements_in_selected_metrics()
# 459 out of 1287 players in the selected metrics have at least 5 measurements 
# Percentage = (459/1287)*100 = 35.66%

get_athletes_with_5_measurements_not_in_selected_metrics()
# 811 out of 1287 players NOT in the selected metrics have at least 5 measurements 
# Percentage = (811/1287)*100 = 63.01%
get_team_percentages_with_athletes_with_at_least_5_measurements()
##2.1-3 Identify athletes who haven't been tested in the last 6 months (for your selected metrics)
get_athletes_not_tested_in_last_num_days(180,"2.1-3")
##4.1 Identify athletes who haven't been tested in the last 30 days(for your selected metrics)
get_athletes_not_tested_in_last_num_days(30,"4.1")
##2.1.4 Determine if you have sufficient data to answer your research question
'''------------------<TODO: Team Discussion>--------------------------
Based on the data understanding and missing data analysis, we have identified that while a significant portion of athletes have sufficient measurements for our selected metrics, there remains a considerable number of athletes with insufficient data. This discrepancy may impact the robustness of our analysis and the validity of our conclusions.
To address this, we propose the following steps:        '''
'''1. Data Imputation: For athletes with missing measurements, we can explore data imputation techniques to estimate missing values based on available data trends. This will help in retaining more athletes in our analysis.        '''
'''2. Focused Analysis: We may consider narrowing our research question to focus on athletes with sufficient data, ensuring that our findings are based on reliable measurements.        '''
'''3. Additional Data Collection: If feasible, we could look into collecting additional data for athletes with insufficient measurements to enhance the dataset's completeness.        '''
'''4. Sensitivity Analysis: Conduct sensitivity analyses to understand how the presence of missing data might affect our results and interpretations.        '''


'''2.2 - Data Transformation Challenge  helper function that returns clean data for selected metrics list and playername list'''
## Define the list of metrics and player names
metric_list = ['leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total']
playername_list = ['PLAYER_755', 'PLAYER_690', 'PLAYER_1128']
## Call the function to get data in The data is in "long format" (one row per metric per timestamp) to to "wide format"
get_data_in_wide_format_by_athlete_and_metric(metric_list, playername_list,"wide")
get_data_in_wide_format_by_athlete_and_metric(metric_list, "all","wide")
''' 2.3 - Create a Derived Metric'''
## Calculates the mean value for each team (using the team column)
get_mean_value_for_each_team()

''' 3.2-1 - Export Cleaned Data'''
## output all cleaned metrics records to a CSV file for slected metrics ('leftMaxForce', 'rightMaxForce', 'leftTorque', 'rightTorque', 'accel_load_accum', 'distance_total', 'avg_accel_load_accum','avg_torque_asymmetry','avg_max_force_asymmetry')
get_all_clean_metrics_records("wide")

''' 3.1-2 Match Force/Torque Metrics with Accel_Load_Accum and Distance_Total by Date'''
## Call the function to match metrics by if the date is the same only
get_matched_metrics_by_date()