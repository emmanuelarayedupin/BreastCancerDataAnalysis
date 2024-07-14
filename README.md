# Breast Cancer Data Analysis

This project analyzes breast cancer diagnosis data from the Histopathology Laboratory of National Hospital Abuja over the past five years.

## Project Structure
- `data`: Contains the raw data file `breast_cancer_data.csv`.
- `scripts`: Contains the Python script `data_analysis.py` for data analysis.
- `results`: Contains generated plots and analysis results.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Data Source
National Hospital Abuja Histopathology department hospital records.

## Analysis
The analysis includes:
- Descriptive statistics of the data.
- Visualizations showing trends in total samples, breast samples, and positive breast cancer cases over the years.

# Statistical analysis
# Correlation between Total_Breast_Samples and Positive_Breast_Cancers
correlation, p_value = pearsonr(data['Total_Breast_Samples'], data['Positive_Breast_Cancers'])
print(f'Correlation: {correlation}, P-value: {p_value}')


## Visualizations

### Total Samples and Breast Samples Over the Years
![Total Samples vs Breast Samples](total_samples_vs_breast_samples.png)

### Positive Breast Cancer Cases Over the Years
![Positive Breast Cancer Cases](positive_breast_cancer_cases.png)

## How to Run the Analysis
1. Clone this repository.
2. Navigate to the `scripts` directory.
3. Run `data_analysis.py` to generate the analysis and plots.
