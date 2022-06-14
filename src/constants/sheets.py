from cmath import nan
import pandas as pd
import numpy as np
import datetime as dt


loadData = pd.read_excel ("../../data/mimbcdui_uta11_scenarios.xlsx", sheet_name="results_before", header=None)

data = np.array(loadData)

# loadDataArray = np.delete(loadDataArray, np.argwhere(np.isnan(loadDataArray)))

# loadDataArray = np.delete(loadDataArray, np.argwhere(isinstance(loadDataArray, str)))

for i,x in enumerate(data):
    for(j,y) in enumerate(x):
        if isinstance(y, dt.time):
            data[i][j] = y.hour * 60 + y.minute

loadScenarios = pd.read_excel ("../../data/mimbcdui_uta11_scenarios.xlsx", sheet_name="scenarios", header=None)
scenarios = np.array(loadScenarios)

def getScenariosPatients():
    new_scenarios_patients = np.array([])
    for p in scenarios[1:,3]:
        p = p.replace("p", "")
        new_scenarios_patients = np.append(new_scenarios_patients, int(p) - 1)
    return new_scenarios_patients
