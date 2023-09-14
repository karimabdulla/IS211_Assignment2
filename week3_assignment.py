import pandas as pd
import numpy as np
cum_miles = np.array([55, 120, 160, 210, 280, 320])
cum_series = pd.Series(cum_miles)
each_Day = np.array([cum_series[0]])
for i in range(1, len(cum_series)):
    each_Day = np.append(each_Day, cum_series[i] - cum_series[i - 1])
print("Miles each day:")
print(pd.Series(each_Day))