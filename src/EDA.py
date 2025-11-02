import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load cleaned dataset
file_path = "data/cleaned_sba.csv"
df = pd.read_csv(file_path, low_memory=False)

#Loan Status Counts
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='MIS_Status', palette='coolwarm', hue='MIS_Status', legend=False)
plt.title("Loan Status Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#Average Loan Amounts
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='MIS_Status', y='DisbursementGross', estimator=np.mean, hue='MIS_Status', palette='Blues', legend=False)
plt.title("Average Disbursement by Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("Avg Disbursement ($)")
plt.tight_layout()
plt.show()

#Top 10 Banks by Total Disbursement
if 'Bank' in df.columns:
    top_banks = df.groupby('Bank')['DisbursementGross'].sum().nlargest(10)
    top_banks.plot(kind='barh', color='teal', figsize=(8,4))
    plt.title("Top 10 Banks by Total Loan Disbursement")
    plt.xlabel("Total Disbursement ($)")
    plt.tight_layout()
    plt.show()

#Loan Status by Urban/Rural
if 'UrbanRural' in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x='UrbanRural', hue='MIS_Status', palette='viridis')
    plt.title("Loan Status by Urban/Rural")
    plt.xlabel("Region Type")
    plt.ylabel("Loan Count")
    plt.tight_layout()
    plt.show()

#Jobs Created vs Disbursement
plt.figure(figsize=(6,4))
sns.scatterplot(data=df.sample(5000), x='DisbursementGross', y='CreateJob', alpha=0.4)
plt.title("Jobs Created vs Disbursement Amount")
plt.xlabel("Disbursement ($)")
plt.ylabel("Jobs Created")
plt.tight_layout()
plt.show()

#Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['DisbursementGross','SBA_Appv','CreateJob','RetainedJob','loan_processing_days','loan_to_SBA_ratio']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#summary
print("\nSummary of Key Insights:")
print(f"Total Loans: {len(df)}")
print(f"Good Loans: {sum(df['MIS_Status']=='Good Loan')}")
print(f"Bad Loans: {sum(df['MIS_Status']=='Bad Loan')}")
print(f"Average Disbursement: ${df['DisbursementGross'].mean():,.2f}")
print(f"Average Jobs Created per $1M: {df['jobs_per_million'].mean():.2f}")