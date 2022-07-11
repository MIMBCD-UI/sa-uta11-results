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
import openpyxl
import csv

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

# loadData = pd.read_excel(scenarios_abs_path, engine='openpyxl', sheet_name="results_before", header=None)

# data = np.array(loadData)

# loadDataArray = np.delete(loadDataArray, np.argwhere(np.isnan(loadDataArray)))

# loadDataArray = np.delete(loadDataArray, np.argwhere(isinstance(loadDataArray, str)))

# for i,x in enumerate(data):
#     for(j,y) in enumerate(x):
#         if isinstance(y, dt.time):
#             data[i][j] = y.hour * 60 + y.minute

# loadScenarios = pd.read_excel (scenarios_abs_path, sheet_name="scenarios", header=None)
# scenarios = np.array(loadScenarios)

# def getScenariosPatients():
#     new_scenarios_patients = np.array([])
#     for p in scenarios[1:,3]:
#         p = p.replace("p", "")
#         new_scenarios_patients = np.append(new_scenarios_patients, int(p) - 1)
#     return new_scenarios_patients

# ============================== #
# ============================== #
#            VARIABLES           #
# ============================== #
# ============================== #

data_times_df = pd.read_csv(times_abs_path, header=None)
data_times = data_times_df.to_numpy()

arr_uta7_uta11_scenario_id = data_times[1:, 0]
arr_uta11_id_clinician = data_times[1:, 1]
arr_category_level = data_times[1:, 2]
arr_expertise_level = data_times[1:, 3]
arr_patient_severity_real_level = data_times[1:, 4]
arr_uta4_time_on_task_no_ai = data_times[1:, 5]
arr_uta7_time_on_task_physician_assistant = data_times[1:, 6]
arr_uta11_time_on_task_pysician_assistant_personalized = data_times[1:, 7]

arr001 = arr_uta7_uta11_scenario_id
arr002 = arr_uta11_id_clinician
arr003 = arr_category_level
arr004 = arr_expertise_level
arr005 = arr_patient_severity_real_level
arr006 = arr_uta4_time_on_task_no_ai
arr007 = arr_uta7_time_on_task_physician_assistant
arr008 = arr_uta11_time_on_task_pysician_assistant_personalized

print(arr001)
print(arr002)
print(arr003)
print(arr004)
print(arr005)
print(arr006)
print(arr007)
print(arr008)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#            CONDITIONS          #
# ============================== #
# ============================== #

print(data_times_df)

data_times_df = data_times_df.set_index('expertise_level')

df['price (kg)'] = np.where(
  df['supplier'] == 'T & C Bro', 
  tc_price.loc[df.index]['price (kg)'], 
  jm_price.loc[df.index]['price (kg)']
)

#args = df_price.loc[df_3.index]

# ============================== #
# ============================== #
# ============================== #
# ============================== #