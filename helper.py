import numpy as np
from scipy.stats import norm
import pandas as pd

def revert_diff(diff_values, start_values, period):
    x = np.r_[start_values, diff_values]
    for t in range(period, len(diff_values) + period):
        x[t] = sum(diff_values[np.arange(t % period, t, period)]) + \
             start_values[t % period]
    return x

# Example Time Series - weekly sales
y = np.zeros(52)
for i in range(1, 52):
    y[i] = y[i - 1] + norm.rvs(size=1, scale=5)
x = np.arange(1, 53, 1)
sales_df = pd.DataFrame(np.stack([x, y], axis=1), columns=["week", "volume"])
sales_df.to_csv("data/weekly-sales.csv", index=False)