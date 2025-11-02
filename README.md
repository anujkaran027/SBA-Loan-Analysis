# SBA Loan Analysis

This project analyzes the **U.S. Small Business Administration (SBA) loan dataset** to understand:
- Loan approval and default patterns
- Economic impact (jobs created/retained)
- Geographic and bank-level trends
- Key predictors of loan default

We clean, explore, and statistically summarize the data using **Python, Pandas, Matplotlib, and Seaborn**.

---

## Data

### 1. Raw Dataset
```bash
https://drive.google.com/file/d/1mMZoB3BR4ctv6sp0-ShMdmL-qF83zw9R/view?usp=sharing
```

### 2. Cleaned Dataset
```bash
https://drive.google.com/file/d/1n2mYAba57cHL6zdk8IAUJb49mz1Ls_AV/view?usp=sharing
```

> Download all the files into data folder of the project
> You can also use **`data_cleaning.py`** to create **Cleaned Dataset**

---

## Pipeline

1. **`data_cleaning.py`**  
   - Loads raw CSV  
   - Cleans dates, money, categories  
   - Engineers features: `loan_processing_days`, `jobs_per_million`, etc.  
   - Saves → `cleaned_sba.csv`

2. **`EDA.py`**  
   - Visualizes:
     - Default rates
     - Avg loan size by status
     - Top banks
     - Urban vs Rural defaults
     - Jobs vs Disbursement
     - Correlation heatmap

3. **`statistical_summary.py`**  
   - Numeric summaries
   - Frequency tables
   - Correlation matrix
   - Normality tests (Shapiro-Wilk)
   - Outlier detection (IQR)
   - Exports to Excel

---

## Power BI

A **Dashboard** is available in Power BI:

**File**: `data/powerbi_summary.pbix`

>*Open `.pbix` file in [Power BI Desktop](https://powerbi.microsoft.com/desktop/)

---

## Exploratory Notebook (Google Colab)

The folder **`notebooks/`** contains a **Google Colab** notebook:

**File**: `notebooks/sbanational.ipynb`

> The notebook is fully executable in **Google Colab** – just open the notebook in colab, upload `data/SBAnational.csv`, and run all cells.

---

## How to Run

### 1. Clone the repo
```bash
git clone https://github.com/anujkaran027/SBA-Loan-Analysis.git
```

### 2. (Optional) create a virtual environment
```bash
python -m venv venv
# mac & linux
source venv/bin/activate
# Windows 
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run pipeline
```bash
python src/data_cleaning.py
python src/EDA.py
python src/statistical_summary.py
```