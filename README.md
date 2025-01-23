# Road Accident Data Analysis

## Overview
This project analyzes road accident data from Indian cities with a population of over a million. The dataset contains detailed information about accidents, including cause categories, subcategories, outcomes, and city-specific data. The goal is to derive meaningful insights and visualize patterns to understand the factors contributing to road accidents.

## Dataset
- **File Name**: `road_accident_data_2020.csv`
- **Columns**:
  - `Million Plus Cities`: Cities with populations exceeding a million.
  - `Cause category`: Broad categories of accident causes (e.g., Traffic Control, Vehicle Issues).
  - `Cause Subcategory`: Detailed subcategories of accident causes.
  - `Outcome of Incident`: Outcomes such as minor injuries, grievous injuries, fatalities, etc.
  - `Count`: Number of incidents for each combination of cause and outcome.

## Features
This analysis focuses on the following aspects:
1. Distribution of accidents across cities.
2. Analysis of accident causes by category and subcategory.
3. Visualization of outcomes for various causes.
4. Severity analysis by city and incident outcomes.
5. Stacked bar charts and heatmaps for detailed insights.

## Visualizations
Key visualizations included:
- Bar plots showing the distribution of accidents by city, cause category, and subcategory.
- Outcome analysis for various incident causes.
- Stacked bar charts for accident causes vs. outcomes.
- Heatmap representing the relationship between accident causes and outcomes.

## Code Structure
The project is implemented in Python using:
- **Pandas** for data cleaning and aggregation.
- **Matplotlib** and **Seaborn** for visualizations.

### Key Steps:
1. **Data Loading and Cleaning**:
   - Load the dataset and check for missing values.
   - Remove rows with missing data.
2. **Data Analysis**:
   - Aggregated accident counts by cities, cause categories, and outcomes.
3. **Visualizations**:
   - Generated meaningful plots to analyze patterns and trends.
