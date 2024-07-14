import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('../data/breast_cancer_data.csv')

# Create visualizations
# Line plot for total samples and breast samples over the years
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Total_Samples', data=data, marker='o', label='Total Samples')
sns.lineplot(x='Year', y='Total_Breast_Samples', data=data, marker='o', label='Breast Samples')
plt.title('Total Samples and Breast Samples Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Samples')
plt.legend()
plt.savefig('../results/total_samples_vs_breast_samples.png')
plt.close()

# Bar plot for positive breast cancer cases over the years
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Positive_Breast_Cancers', data=data, palette='viridis')
plt.title('Positive Breast Cancer Cases Over the Years')
plt.xlabel('Year')
plt.ylabel('Positive Breast Cancer Cases')
plt.savefig('../results/positive_breast_cancer_cases.png')
plt.close()

# Generate README file
with open('../README.md', 'w') as f:
    f.write('# Breast Cancer Data Analysis\n\n')
    f.write('This project analyzes breast cancer diagnosis data from the Histopathology Laboratory of National Hospital Abuja over the past five years.\n\n')
    f.write('## Project Structure\n')
    f.write('- `data`: Contains the raw data file `breast_cancer_data.csv`.\n')
    f.write('- `scripts`: Contains the Python script `data_analysis.py` for data analysis.\n')
    f.write('- `results`: Contains generated plots and analysis results.\n')
    f.write('- `.gitignore`: Specifies intentionally untracked files to ignore.\n\n')
    f.write('## Data Source\n')
    f.write('The data used in this project is provided in the attached document.\n\n')
    f.write('## Analysis\n')
    f.write('The analysis includes:\n')
    f.write('- Descriptive statistics of the data.\n')
    f.write('- Visualizations showing trends in total samples, breast samples, and positive breast cancer cases over the years.\n\n')
    f.write('## Visualizations\n\n')
    f.write('### Total Samples and Breast Samples Over the Years\n')
    f.write('![Total Samples vs Breast Samples](results/total_samples_vs_breast_samples.png)\n\n')
    f.write('### Positive Breast Cancer Cases Over the Years\n')
    f.write('![Positive Breast Cancer Cases](results/positive_breast_cancer_cases.png)\n\n')
    f.write('## How to Run the Analysis\n')
    f.write('1. Clone this repository.\n')
    f.write('2. Navigate to the `scripts` directory.\n')
    f.write('3. Run `data_analysis.py` to generate the analysis and plots.\n')
