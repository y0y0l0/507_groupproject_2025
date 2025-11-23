# HHA507_Group_Project

Group SBU Sports data Project
Goal of this project is to analyze sports performance data from multiple sources (Hawkins, Kinexon, Vald) to identify key metrics that can help improve athlete performance and reduce injury risk.

# Team Data Setup:
link to team database setup screenshots: https://drive.google.com/drive/folders/1bX1Yk2YJH1KX1Z3o1F6gD3fQXK5Jt5vP?usp=sharing

# Team presentation slides:
link to team presendation slides: https://docs.google.com/presentation/d/1IiI5CwbIHg4V8L8NR5JBr0AiKxmIxBGMQci9IVsK6oo/edit?usp=sharing

# Team literature review:
link to team literature review: https://docs.google.com/document/d/1hs3RljvobFhrrgEVS4Ev2E5Cl8YE0w7z1t3h8Qo_D-A/edit?tab=t.0

#Team Notebook:
link to team part3_viz_comparison notebook: https://colab.research.google.com/drive/1pl6wRVZaPeZ0Pbktx6SGiONwlCW_hQ-0?usp=sharing

## Project Structure
    HHA507_Group_Project/                  # Root directory
    ├── 1.1 Team Database Setup Screenshots/  # Directory for team database setup screenshots from each team member
    |
    ├── output/                          # Output data files
    ├── scripts/                         # Main scripts
    │   ├── common_clean_function.py     # Common data cleaning and preprocessing functions
    │   ├── common_functions.py          # Common data analysis functions
    │   ├── part_exploration.py          # Initial data analysis scripts
    │   └── part2_cleaning.py            # Data cleaning scripts
    ├── README.md                        # Readme file
    ├── requirements.txt                 # Project dependencies
    ├── GROUP_ASSIGNMENT.pdf             # Group assignment details    
    └── .gitignore                       # Git ignore file
### Data Exploration
# The `part_exploration.py` script in the `scripts/` directory contains functions for initial data exploration, including loading datasets, summarizing data, and visualizing key metrics.
    1.2 Data Quality Assessment (Group)
        1. How many unique athletes are in the database?
            *Identify the total number of unique athletes across all datasets.*
            'There are 1287 unique athletes in the database.'
        2. How many different sports/teams are represented?
            * Determine the number of sports teams included in the data (this data is sanitized).*
            'There are Unique sports/teams 89 in the database after removing duplicates and invalid entries ie: 'Unknown','Player Not Found','Graduated (No longer enrolled)'.'
        3. What is the date range of available data?
            * Identify the earliest and latest dates of data collection (this data includes invalid entries).*
            'The creation date range of a data is from 2025-10-21 16:46:54 to 2025-10-21 17:03:12.'
            'The timestamp date range of a data is from 2018-10-15 19:27:41 to 2025-10-21 12:24:21'
        4. Which data source (Hawkins/Kinexon/Vald) has the most records?
            * Compare the number of records from each data source (this data includes invalid entries).*
            'The data source hawkins has 2492372 records.'
            'The data source kinexon has 4073754 records.'
            'The data source vald has 51300 records.'
        5. Are there any athletes with missing or invalid names (this data includes invalid entries)?
            * Identify athletes with missing or improperly formatted names (this data includes invalid entries).*
            -There are no invalid athlete names in the database.
        6. How many athletes have data from multiple sources (2 or 3 systems) (this data is sanitized)?
            * Determine the number of athletes with data from more than one source (this data includes invalid entries).*
            -There are 541 athletes with data from multiple sources.
    1.3 Metric Discovery & Selection (Group)
        1. Lists the top 10 most common metrics for Hawkins data (filter by data_source = 'Hawkins')
            * Identify the most frequently recorded metrics in the Hawkins dataset (this data includes invalid entries).*
            The top 10 most common metrics for Hawkins data are:
                _________________________________________________________________________ 
                |         | metric                                     |  metric_count  |
                |---------|--------------------------------------------|----------------|
                |0        |                     System Weight(N)       |31467           |
                |1        |         Propulsive Net Impulse(N.s)        |31295           |
                |2        |           Peak Propulsive Force(N)         |31295           |
                |3        |           Avg. Propulsive Power(W)         |31295           |
                |4        |                     Jump Height(m)         |31295           |
                |5        |                 Peak Velocity(m/s)         |31295           |
                |6        |                Propulsive Phase(s)         |31295           |
                |7        |           Peak Propulsive Power(W)         |31295           |
                |8        |  Avg. Relative Propulsive Force(%)         |31295           |
                |9        |           Avg. Propulsive Force(N)         |31295           |
    2. Lists the top 10 most common metrics for Kinexon data (filter by data_source = 'Kinexon')
            * Identify the most frequently recorded metrics in the Kinexon dataset (this data includes invalid entries).*
                -The top 10 most common metrics for Kinexon data are:
                _________________________________________________________________________ 
                |         | metric                                     |  metric_count  |
                |---------|--------------------------------------------|----------------|
                |0        | track_outside_field                        |40803           |
                |1        | track_heart_rate_always                    |40803           |
                |2        | accel_load_accum                           |40703           |
                |3        | time_total                                 |40585           |
                |4        | accel_load_accum_avg_per_minute            |40485           |
                |5        | distance_total                             |40317           |
                |6        | speed_distance_per_time                    |40316           |
                |7        | distance_total_avg_per_minute              |40315           |
                |8        | speed_max                                  |40312           |
                |9        | speed_avg                                  |40298           |
            
    3. Lists the top 10 most common metrics for Vald data (filter by data_source = 'Vald')
            * Identify the most frequently recorded metrics in the Vald dataset (this data includes invalid entries).*
                -The top 10 most common metrics for Vald data are:
                _________________________________________________________________________
                |         | metric                                     |  metric_count  |
                |---------|--------------------------------------------|----------------|
                |0        | leftAvgForce                               |3517            |
                |1        | leftMaxForce                               |3517            |
                |2        | leftImpulse                                |3514            |
                |3        | rightAvgForce                              |3514            |
                |4        | rightMaxForce                              |3514            |
                |5        | rightImpulse                               |3509            |
                |6        | leftTorque                                 |3475            |
                |7        | rightTorque                                |3472            |
                |8        | rightRepetitions                           |3460            |
                |9        | leftRepetitions                            |3452            |
            
    4. Identifies how many unique metrics exist across all data sources
            * Identify the total number of distinct metrics recorded across all datasets.*
            -There are 548 unique metrics across all data sources.
    5. For each data source, show the date range and record count for the top metrics
            * Identify the date range and number of records for the most common metrics in each dataset.*
            - Hawkins Top Metrics Date Range and Record Count:
            -Date min_timestamp 2018-10-15 19:27:41 and max_timestamp 2025-10-14 12:50:32 for top metrics by data source Hawkins.
                ________________________________________________________________________________________________________
                |         | metric                             |  record_count  |   min_timestamp   |   max_timestamp   |
                |---------|------------------------------------|----------------|-------------------|-------------------|
                |0        |          System Weight(N)          |           31467|2018-10-15 19:27:41|2025-10-14 12:50:32|
                |1        | Propulsive Net Impulse(N.s)        |           31295|2018-10-15 19:27:41|2025-10-14 12:50:32|
                |2        | Peak Propulsive Force(N)           |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |3        | Avg. Propulsive Power(W)           |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |4        |          Jump Height(m)            |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |5        |      Peak Velocity(m/s)            |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |6        | Avg. Relative Propulsive Force(%)  |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                |7        | Avg. Propulsive Force(N)           |          31295 |2018-10-15 19:27:41|2025-10-14 12:50:32|
                    - Kinexon Top Metrics Date Range and Record Count:
                    -Date min_timestamp 2021-06-17 21:49:39 and max_timestamp 2025-10-21 12:24:21 for top metrics by data source Kinexon.
                ______________________________________________________________________________________________________
                |         | metric                          |  record_count  |   min_timestamp   |   max_timestamp   |
                |---------|---------------------------------|----------------|-------------------|-------------------|
                |0         | track_outside_field            |          40803 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |1         | track_heart_rate_always        |          40803 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |2         | accel_load_accum               |          40703 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |3         | time_total                     |          40585 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |4         | accel_load_accum_avg_per_minute|          40485 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |5         | distance_total                 |          40317 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |6         | speed_distance_per_time        |          40316 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |7         | distance_total_avg_per_minute  |          40315 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |8         | speed_max                      |          40312 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                |9         | speed_avg                      |          40298 |2021-06-17 21:49:39|2025-10-21 12:24:21|
                Vald Top Metrics Date Range and Record Count:
                Date min_timestamp 2020-12-14 12:56:23 and max_timestamp 2025-10-01 15:11:46 for top metrics by data source Vald.
                ______________________________________________________________________________________________________
                |         | metric                          |  record_count  |   min_timestamp   |   max_timestamp   |
                |---------|---------------------------------|----------------|-------------------|-------------------|
                |0        |leftAvgForce                     |           3517 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |1        |leftMaxForce                     |           3517 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |2        |leftImpulse                      |           3514 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |3        |rightAvgForce                    |           3514 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |4        |rightMaxForce                    |           3514 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |7        |rightTorque                      |           3472 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |8        |rightRepetitions                 |           3460 |2020-12-14 12:56:23|2025-10-01 15:11:46|
                |9        |leftRepetitions                  |           3452 |2020-12-14 12:56:23|2025-10-01 15:11:46|

### Data Cleaning and Preprocessing
The `part2_cleaning.py` script in the `scripts/` directory contains functions to clean and preprocess the data. It identifies metrics with missing records, calculates athlete measurement percentages, and flags athletes not tested in the last 6 months.
# 2.2 Missing Data Analysis (Group)
- 1. Identify which of your selected metrics have the most NULL or zero values
- 2. For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics
- 3. Identify athletes who haven't been tested in the last 6 months (for your selected metrics)
- 4. Determine if you have sufficient data to answer your research question
2.2 Data Transformation Challenge (Group)
- 1. Takes a player name (e.g., "PLAYER_001") and your selected metrics (e.g., "leftMaxForce", "rightMaxForce") as input
    - Returns a pandas DataFrame with:
        - Columns: timestamp, [your selected metrics]
        - One row per test session
        - Properly handles missing values
            - only include records where the team is not in ('Unknown','Player Not Found','Graduated (No longer enrolled)')
            - Concolidate team names by removing any single quotes
            -Saves the resulting DataFrame to a CSV file with the naming convention: `2.2_[first playername in list]_data_in_wide_format_by_athlete_and_metric.csv`
# 2.3 Create a Derived Metric (Group)
- 1. Calculates the mean value for each team (using the team column)
- 2. For each athlete measurement, calculates their percent difference from their team's average
- 3. Identifies the top 5 and bottom 5 performers relative to their team mean
- 4. Optional: Create z-scores or percentile rankings
    - Z-score tutorial: SciPy stats.zscore
    - Percentile tutorial: NumPy percentile
    - Example: Calculating z-scores in pandas