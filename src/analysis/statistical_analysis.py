"""
Data Analysis Module

This module contains functions for performing statistical analysis on healthcare data.
"""

import pandas as pd
import numpy as np


def descriptive_statistics(df, column):
    """
    Calculate descriptive statistics for a numeric column.
    
    Args:
        df (pd.DataFrame): Input dataframe
        column (str): Column name
        
    Returns:
        dict: Dictionary with descriptive statistics
    """
    if column not in df.columns:
        print(f"Error: Column '{column}' not found in dataframe")
        return None
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(f"Error: Column '{column}' is not numeric")
        return None
    
    stats_dict = {
        'mean': df[column].mean(),
        'median': df[column].median(),
        'std': df[column].std(),
        'min': df[column].min(),
        'max': df[column].max(),
        'q25': df[column].quantile(0.25),
        'q75': df[column].quantile(0.75)
    }
    
    return stats_dict


def correlation_analysis(df, columns=None):
    """
    Calculate correlation matrix for numeric columns.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of columns to include (default: all numeric columns)
        
    Returns:
        pd.DataFrame: Correlation matrix
    """
    if columns is None:
        # Select all numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
    else:
        numeric_df = df[columns]
    
    correlation_matrix = numeric_df.corr()
    return correlation_matrix


def compare_groups(df, group_column, value_column):
    """
    Compare values across different groups.
    
    Args:
        df (pd.DataFrame): Input dataframe
        group_column (str): Column name for grouping
        value_column (str): Column name for values to compare
        
    Returns:
        dict: Summary statistics by group
    """
    if group_column not in df.columns or value_column not in df.columns:
        print("Error: Specified columns not found")
        return None
    
    grouped_stats = df.groupby(group_column)[value_column].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ])
    
    return grouped_stats


if __name__ == "__main__":
    # Example usage
    print("Analysis module loaded successfully.")
    print("Import this module in your scripts to use these functions.")
