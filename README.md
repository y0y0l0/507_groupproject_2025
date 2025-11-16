# HHA507_Group_Project
Group Project
## Project Structure
├── 1.1 Team Database Setup Screenshots/               # Individual database connection setup screenshots from each team member
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
The `part_exploration.py` script in the `scripts/` directory contains functions for initial data exploration, including loading datasets, summarizing data, and visualizing key metrics.
    - 1.2 Data Quality Assessment (Group)
        -1. How many unique athletes are in the database?
            *Identify the total number of unique athletes across all datasets.*
        - 2. How many different sports/teams are represented?
            * Determine the number of sports teams included in the data (this data includes invalid entries).*
        - 3. What is the date range of available data?
            * Identify the earliest and latest dates of data collection (this data includes invalid entries).*
        - 4. Which data source (Hawkins/Kinexon/Vald) has the most records?
            * Compare the number of records from each data source (this data includes invalid entries).*
        - 5. Are there any athletes with missing or invalid names (this data includes invalid entries)?
            * Identify athletes with missing or improperly formatted names (this data includes invalid entries).*
        - 6. How many athletes have data from multiple sources (2 or 3 systems) (this data includes invalid entries)?
            * Determine the number of athletes with data from more than one source (this data includes invalid entries).*
    -1.3 Metric Discovery & Selection (Group)
        - 1. Lists the top 10 most common metrics for Hawkins data (filter by data_source = 'Hawkins')
            * Identify the most frequently recorded metrics in the Hawkins dataset (this data includes invalid entries).*
        - 2. Lists the top 10 most common metrics for Kinexon data (filter by data_source = 'Kinexon')
            * Identify the most frequently recorded metrics in the Kinexon dataset (this data includes invalid entries).*
        - 3. Lists the top 10 most common metrics for Vald data (filter by data_source = 'Vald')
            * Identify the most frequently recorded metrics in the Vald dataset (this data includes invalid entries).*
        - 4. Identifies how many unique metrics exist across all data sources
            * Identify the total number of distinct metrics recorded across all datasets.*
        - 5. For each data source, show the date range and record count for the top metrics
            * Identify the date range and number of records for the most common metrics in each dataset.*
        - 6. (Team discussion question) Team's question: How many unique teams are represented in the top metrics for each data source?
            * Identify the number of distinct sports teams associated with the most common metrics in each dataset.*
### Data Cleaning and Preprocessing
The `part2_cleaning.py` script in the `scripts/` directory contains functions to clean and preprocess the data. It identifies metrics with missing records, calculates athlete measurement percentages, and flags athletes not tested in the last 6 months.
    - 2.2 Missing Data Analysis (Group)
        - 1. Identify which of your selected metrics have the most NULL or zero values
        - 2. For each sport/team, calculate what percentage of athletes have at least 5 measurements for your selected metrics
        - 3. Identify athletes who haven't been tested in the last 6 months (for your selected metrics)
        - 4. Determine if you have sufficient data to answer your research question
    - 2.2 Data Transformation Challenge (Group)
        - 1. Takes a player name (e.g., "PLAYER_001") and your selected metrics (e.g., "leftMaxForce", "rightMaxForce") as input
            - Returns a pandas DataFrame with:
                - Columns: timestamp, [your selected metrics]
                - One row per test session
                - Properly handles missing values
                    - only include records where the team is not in ('Unknown','Player Not Found','Graduated (No longer enrolled)')
                    - Concolidate team names by removing any single quotes
                    -Saves the resulting DataFrame to a CSV file with the naming convention: `2.2_[first playername in list]_data_in_wide_format_by_athlete_and_metric.csv`
    - 2.3 Create a Derived Metric (Group)
        - 1. Calculates the mean value for each team (using the team column)
        - 2. For each athlete measurement, calculates their percent difference from their team's average
        - 3. Identifies the top 5 and bottom 5 performers relative to their team mean
        - 4. Optional: Create z-scores or percentile rankings
            - Z-score tutorial: SciPy stats.zscore
            - Percentile tutorial: NumPy percentile
            - Example: Calculating z-scores in pandas