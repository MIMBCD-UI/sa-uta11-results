#!/usr/bin/env python
#coding=utf-8

"""
sheets.py: to read our data, we are using several datasets. For that,
           we need to read a bunch of xls and csv files. The presented file,
           will serve this purpose. It is here, where we are reading
           our datasets, provinding several variables to be used.
"""

import os
import sys

from os import path

from cmath import nan
import pandas as pd
import numpy as np
import datetime as dt

# The current folder path.
basePath = os.path.dirname(__file__)

pathReposDirname = os.path.dirname(__file__)
joinReposPath = os.path.join(pathReposDirname, '..', '..')
pathReposAbsPath = os.path.abspath(joinReposPath)

src_data_dir = os.path.join(pathReposAbsPath, 'data')
sys.path.append(src_data_dir)
srcDataAbsPath = os.path.abspath(src_data_dir)

# ============================== #
# ============================== #

import pandas as pd

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#               PATH             #
# ============================== #
# ============================== #

scenarios_dir = os.path.join(srcDataAbsPath, 'mimbcdui_uta11_scenarios.xlsx')
sys.path.append(scenarios_dir)
scenarios_abs_path = os.path.abspath(scenarios_dir)

times_dir = os.path.join(srcDataAbsPath, 'mimbcdui_uta7_uta11_results_curated_abimid_times.csv')
sys.path.append(times_dir)
times_abs_path = os.path.abspath(times_dir)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

loadData = pd.read_excel (scenarios_abs_path, sheet_name="results_before", header=None)

data = np.array(loadData)

# loadDataArray = np.delete(loadDataArray, np.argwhere(np.isnan(loadDataArray)))

# loadDataArray = np.delete(loadDataArray, np.argwhere(isinstance(loadDataArray, str)))

for i,x in enumerate(data):
    for(j,y) in enumerate(x):
        if isinstance(y, dt.time):
            data[i][j] = y.hour * 60 + y.minute

loadScenarios = pd.read_excel (scenarios_abs_path, sheet_name="scenarios", header=None)
scenarios = np.array(loadScenarios)

def getScenariosPatients():
    new_scenarios_patients = np.array([])
    for p in scenarios[1:,3]:
        p = p.replace("p", "")
        new_scenarios_patients = np.append(new_scenarios_patients, int(p) - 1)
    return new_scenarios_patients
