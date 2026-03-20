# DS4002_Project2
## This repository contains the dataset, EDA, Kruskall-Wallis/Chi square tests, and a logistic regression model used to analyze S&P 500 volatility across the three most recent presidential administrations. 
## Software and Platform
This project was developed and tested using the following  environment:

Operating System: macOS

Programming Language: Python

Developed Environment: Jupyter Notebook, Visual Studio Code

Required Python Packages:
- pandas
- numpy
- matplotlib
- statsmodels
- scipy
- scikit-learn

## Documentation
### Data Folder
&emsp;Data appendix.pdf\
&emsp;SP500.csv\
&emsp;sp500_clean.csv
### Output Folder
EDA Folder\
&emsp;Price_over_time.png\
&emsp;Volatility_over_time.png\
Data Appendix Folder\
&emsp;Closing_prices_bxplt.png\
&emsp;Closing_prices_hist.png\
&emsp;Returns_boxplt.png\
&emsp;Returns_hist.png\
sp500_volatility_analysis Folder\
&emsp;Rate_of_Extreme_Volatility.png\
&emsp;SP500_Level_By_Administration.png\
&emsp;Weekly_Volatility.png
### Scripts Folder
&emsp;EDA.py\
&emsp;data_appendix.py\
&emsp;sp500_volatility_analysis.py
## Reproducibility
### Step 1: Download or Clone the Repository

Download this repository as a ZIP file or clone it:

```
git clone https://github.com/kaleigh-west/DS4002_Project2.git
cd DS4002_Project2
```

All commands below must be run from the project root directory: `DS4002_Project2`

---

### Step 2: Install Required Packages

This project was developed using Python 3.11.

Install dependencies:

```
pip install pandas numpy scikit-learn matplotlib jupyter statsmodels scipy
```

---

### Step 3: Download the Original Dataset

The project uses the **S&P 500 Dataset** from Federal Reserve Bank of St. Louis (FRED) :

For up-to date data, go to the following website, adjust time window, and download as CSV (or use SP500.csv provided in DATA folder)

https://fred.stlouisfed.org/series/SP500 

After downloading, unzip the folder and place the following files into:

`DATA/`

Files required:
```
DATA/SP500.csv
```

---

### Step 4: Run the Exploratory Data Analysis (EDA)

Run:

```
python SCRIPTS/EDA.py
```

This recreates the exploratory visualizations used in the report and sp500_clean.csv.

Pre-generated figures are also included in the `OUTPUT/` folder for reference.

---

### Step 5: Train the Model and Create the Analysis Dataset

Run:

```
python SCRIPTS/sp500_volatility_analysis.py
```

This script will:

- Load sp500_clean.csv
- Compute daily log returns and absolute returns to measure volatility
- Define high-volatility days
- Convert daily data into weekly periods
- Plot rolling volatility
- Create daily summary metrics including volatility and extreme-event rates
- Complete a Kruskal–Wallis test
- Use a chi-aquare test to test whether frequency of extreme-volatility days differs across administrations
- Perform logistic regression
- Output Rate_of_Extreme_Volatility.png, SP500_Level_By_Administration.png, Weekly_Volatility.png

---

### Step 6: Generate the Data Appendix Outputs

Run:

```
python SCRIPTS/data_appendix.py
```

This script uses `DATA/sp500_clean.csv` to recreate the summary statistics and visualizations included in the Data Appendix.

---

### Output Files

All figures and outputs in the `OUTPUT/` folder are reproducible.  
They will be regenerated automatically when the scripts above are executed.
