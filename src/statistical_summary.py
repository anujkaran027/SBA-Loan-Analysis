import pandas as pd
import numpy as np
from scipy import stats

#load dataset
file_path = "data/cleaned_sba.csv"
df = pd.read_csv(file_path, low_memory=False)

print(f"Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

#numeric summary
numeric_summary = df.describe().T
numeric_summary['missing_values'] = df.isna().sum()
print("\n📘 Numeric Summary:")
print(numeric_summary)

#frequency tables
categorical_cols = ['MIS_Status', 'UrbanRural', 'LowDoc', 'RevLineCr', 'NewExist']

for col in categorical_cols:
    if col in df.columns:
        print(f"\n📊 Frequency Table: {col}")
        print(df[col].value_counts(dropna=False))

#correlation matrix
corr_cols = ['DisbursementGross', 'SBA_Appv', 'GrAppv',
             'CreateJob', 'RetainedJob', 'loan_processing_days',
             'loan_to_SBA_ratio', 'jobs_per_million']

corr_matrix = df[corr_cols].corr().round(2)
print("\n🔗 Correlation Matrix:")
print(corr_matrix)

#distribution and outlier detection
col = 'DisbursementGross'
print(f"\n📈 Distribution Analysis for {col}")

print("Mean:", df[col].mean())
print("Median:", df[col].median())
print("Skewness:", df[col].skew())
print("Kurtosis:", df[col].kurt())

#Shapiro-Wilk test for normality (sample 5000)
stat, p = stats.shapiro(df[col].sample(5000, random_state=1))
print(f"Shapiro-Wilk test p-value: {p:.4f} -> {'Normal' if p > 0.05 else 'Not Normal'}")

#Outlier boundaries using IQR
Q1, Q3 = df[col].quantile([0.25, 0.75])
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
outliers = df[(df[col] < lower) | (df[col] > upper)]
print(f"Outliers detected: {len(outliers)} ({(len(outliers)/len(df))*100:.2f}%)")

#loan summary
loan_summary = df.groupby('MIS_Status')[['DisbursementGross', 'CreateJob', 'RetainedJob']].mean().round(2)
print("\n💼 Average Metrics by Loan Status:")
print(loan_summary)

#saving outputs
with pd.ExcelWriter("data/statistical_summary.xlsx") as writer:
    numeric_summary.to_excel(writer, sheet_name='Numeric Summary')
    corr_matrix.to_excel(writer, sheet_name='Correlation')
    loan_summary.to_excel(writer, sheet_name='By Loan Status')