import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('road_accident_data_2020.csv')

# Display basic information and check for missing values
print(df.info())
print("Missing values per column:\n", df.isnull().sum())

# Drop rows with missing values if any
df_cleaned = df.dropna()

# Basic statistical summary of the 'Count' column
print(df_cleaned['Count'].describe())

# Distribution of accidents by city
plt.figure(figsize=(12, 6))
city_order = df_cleaned.groupby('Million Plus Cities')['Count'].sum().sort_values(ascending=False).index
sns.barplot(y='Million Plus Cities', x='Count', data=df_cleaned, order=city_order, ci=None)
plt.title('Distribution of Road Accidents in Million-Plus Cities')
plt.xlabel('Total Number of Accidents')
plt.ylabel('Cities')
plt.tight_layout()
plt.show()

# Distribution of accidents by cause category
plt.figure(figsize=(10, 6))
category_order = df_cleaned.groupby('Cause category')['Count'].sum().sort_values(ascending=False).index
sns.barplot(y='Cause category', x='Count', data=df_cleaned, order=category_order, ci=None)
plt.title('Distribution of Accident Causes')
plt.xlabel('Total Number of Accidents')
plt.ylabel('Cause Category')
plt.tight_layout()
plt.show()

# Detailed analysis by cause subcategory
plt.figure(figsize=(12, 8))
subcategory_order = df_cleaned.groupby('Cause Subcategory')['Count'].sum().sort_values(ascending=False).index
sns.barplot(y='Cause Subcategory', x='Count', data=df_cleaned, order=subcategory_order, ci=None)
plt.title('Accident Causes by Subcategory')
plt.xlabel('Total Number of Accidents')
plt.ylabel('Cause Subcategory')
plt.tight_layout()
plt.show()

# Outcomes of incidents
plt.figure(figsize=(8, 5))
outcome_order = df_cleaned.groupby('Outcome of Incident')['Count'].sum().sort_values(ascending=False).index
sns.barplot(x='Outcome of Incident', y='Count', data=df_cleaned, order=outcome_order, ci=None)
plt.title('Outcomes of Road Accidents')
plt.xlabel('Outcome')
plt.ylabel('Total Number of Incidents')
plt.tight_layout()
plt.show()

# Accident causes vs outcomes (stacked bar chart)
outcome_vs_cause = df_cleaned.groupby(['Cause category', 'Outcome of Incident'])['Count'].sum().unstack()
outcome_vs_cause.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Accident Causes vs Outcomes')
plt.xlabel('Cause Category')
plt.ylabel('Number of Incidents')
plt.legend(title='Outcome of Incident')
plt.tight_layout()
plt.show()

# Additional: City-wise accident severity analysis
severity_order = ['Minor Injury', 'Greviously Injured', 'Persons Killed', 'Total Injured', 'Total number of Accidents']
city_severity = df_cleaned[df_cleaned['Outcome of Incident'].isin(severity_order)].pivot_table(
    index='Million Plus Cities', columns='Outcome of Incident', values='Count', aggfunc='sum'
)
city_severity = city_severity[severity_order]
city_severity.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='coolwarm')
plt.title('City-Wise Accident Severity Analysis')
plt.xlabel('Cities')
plt.ylabel('Number of Incidents')
plt.tight_layout()
plt.show()

# Additional: Heatmap of accident causes vs outcomes
plt.figure(figsize=(10, 6))
sns.heatmap(outcome_vs_cause, annot=True, fmt='.0f', cmap='Blues', linewidths=0.5)
plt.title('Heatmap of Accident Causes vs Outcomes')
plt.xlabel('Outcome of Incident')
plt.ylabel('Cause Category')
plt.tight_layout()
plt.show()
    