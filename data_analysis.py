import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load the data
data = pd.read_csv('breast_cancer_data.csv')

# Statistical analysis
# Correlation between Total_Breast_Samples and Positive_Breast_Cancers
correlation, p_value = pearsonr(data['Total_Breast_Samples'], data['Positive_Breast_Cancers'])
print(f'Correlation: {correlation}, P-value: {p_value}')

# Create visualizations
# Line plot for total samples and breast samples over the years
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Total_Samples', data=data, marker='o', label='Total Samples')
sns.lineplot(x='Year', y='Total_Breast_Samples', data=data, marker='o', label='Breast Samples')
plt.title('Total Samples and Breast Samples Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Samples')
plt.legend()
plt.savefig('total_samples_vs_breast_samples.png')
plt.close()

# Bar plot for positive breast cancer cases over the years
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Positive_Breast_Cancers', data=data, palette='viridis')
plt.title('Positive Breast Cancer Cases Over the Years')
plt.xlabel('Year')
plt.ylabel('Positive Breast Cancer Cases')
plt.savefig('positive_breast_cancer_cases.png')
plt.close()
