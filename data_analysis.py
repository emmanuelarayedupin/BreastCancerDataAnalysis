
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load the data
data = pd.read_csv('breast_cancer_data.csv')

# Display the first few rows of the data for verification
print(data.head())

# Statistical analysis
correlation, p_value = pearsonr(data['Total_Breast_Samples'], data['Positive_Breast_Cancers'])

# Save statistical results to a text file
with open('statistical_analysis.txt', 'w') as f:
    f.write('Statistical Analysis Results:\n')
    f.write('-----------------------------------\n')
    f.write(f'Correlation between Total Breast Samples and Positive Breast Cancers: {correlation}\n')
    f.write(f'P-value: {p_value}\n')

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

# Display a message indicating the analysis is complete
print("Statistical analysis and visualizations have been completed successfully.")
