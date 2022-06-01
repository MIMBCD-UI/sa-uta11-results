from cmath import nan
import pandas as pd
import numpy as np
import datetime as dt


loadData = pd.read_excel ("../results/mimbcdui_uta11_scenarios.xlsx", sheet_name="results_before", header=None)

data = np.array(loadData)

# loadDataArray = np.delete(loadDataArray, np.argwhere(np.isnan(loadDataArray)))

# loadDataArray = np.delete(loadDataArray, np.argwhere(isinstance(loadDataArray, str)))

for i,x in enumerate(data):
    for(j,y) in enumerate(x):
        if isinstance(y, dt.time):
            data[i][j] = y.hour * 60 + y.minute

print(data)