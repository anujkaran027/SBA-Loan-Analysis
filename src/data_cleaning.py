import pandas as pd
import numpy as np

#load dataset
file_path = "data/SBAnational.csv"
df = pd.read_csv(file_path, low_memory=False)

#drop irrelevant column
drop_cols = ['LoanNr_ChkDgt', 'Name', 'Zip', 'FranchiseCode']
df.drop(columns=[c for c in drop_cols if c in df.columns], inplace=True, errors='ignore')

#covert dates
date_cols = ['ApprovalDate', 'DisbursementDate', 'ChgOffDate']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], format='%d-%b-%y', errors='coerce')

# Derived time-based features
df['loan_processing_days'] = (df['DisbursementDate'] - df['ApprovalDate']).dt.days
df['loan_age'] = (df['ChgOffDate'] - df['DisbursementDate']).dt.days

#handle categorical values
if 'MIS_Status' in df.columns:
    df['MIS_Status'] = df['MIS_Status'].str.upper().map({'P I F': 'Good Loan', 'CHGOFF': 'Bad Loan'})
    df['default_flag'] = np.where(df['MIS_Status'] == 'Bad Loan', 1, 0)

if 'UrbanRural' in df.columns:
    df['UrbanRural'] = df['UrbanRural'].map({0: 'Unknown', 1: 'Urban', 2: 'Rural'})

if 'lowdoc' in df.columns:
    df['LowDoc'] = df['LowDoc'].map({'Y': 1, 'N': 0})

if 'RevLineCr' in df.columns:
    df['RevLineCr'] = df['RevLineCr'].replace({'Y': 1, 'N': 0}).fillna(0)

if 'NewExist' in df.columns:
    df['NewExist'] = df['NewExist'].map({1: 'New', 2: 'Existing'})

#convert numeric columns
numeric_cols = ['Term', 'CreateJob', 'RetainedJob']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

#convert numeric money columns
money_cols = ['DisbursementGross', 'BalanceGross', 'SBA_Appv', 'GrAppv']
for col in money_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(r'[\$,]', '', regex=True)
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

#derive features
df['loan_to_SBA_ratio'] = np.where(df['SBA_Appv'] > 0, df['DisbursementGross'] / df['SBA_Appv'], 0)
df['jobs_per_million'] = np.where(df['DisbursementGross'] > 0,
                                  (df['CreateJob'] + df['RetainedJob']) / (df['DisbursementGross'] / 1_000_000), 0)

#data validation
df = df[df['DisbursementDate'] >= df['ApprovalDate']]

#save cleaned dataset
df.to_csv("data/cleaned_sba.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_sba.csv'")