#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import norm
import statsmodels.api as sm
from statsmodels.tsa.arima_process import arma_generate_sample
import seaborn as sns
import pandas as pd

# Example Time Series - weekly sales
y = np.zeros(52)
for i in range(1, 52):
    y[i] = y[i - 1] + norm.rvs(size=1, scale=5)
x = np.arange(1, 53, 1)
sales_df = pd.DataFrame(np.stack([x, y], axis=1), columns=["week", "volume"])
sales_df.to_csv("data/weekly-sales.csv", index=False)
