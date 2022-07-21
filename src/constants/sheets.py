#!/usr/bin/env python
#coding=utf-8

"""
sheets.py: to read our data, we are using several datasets. For that,
           we need to read a bunch of xls and csv files. The presented file,
           will serve this purpose. It is here, where we are reading
           our datasets, provinding several variables to be used.
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "João Fernandes"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "0.1.0"
__status__      = "Development"
__copyright__   = "Copyright 2022, Instituto Superior Técnico (IST)"
__credits__     = [
  "João Fernandes",
  "Miguel Bastos",
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Nuno Nunes",
  "Pedro Miraldo"
]

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

severities_dir = os.path.join(srcDataAbsPath, 'mimbcdui_uta7_uta11_results_curated_abimid_severities.csv')
sys.path.append(severities_dir)
severities_abs_path = os.path.abspath(severities_dir)

preferences_dir = os.path.join(srcDataAbsPath, 'mimbcdui_uta7_uta11_results_curated_abimid_preferences.csv')
sys.path.append(preferences_dir)
preferences_abs_path = os.path.abspath(preferences_dir)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#           ACCURACIES           #
# ============================== #
# ============================== #

data_severities_df = pd.read_csv(severities_abs_path, header=None)
data_severities = data_severities_df.to_numpy()

arr_birads_real = data_severities[1:, 5]
arr_uta7_birads_physician_assistant = data_severities[1:, 7]
arr_uta11_birads_pysician_assistant_personalized = data_severities[1:, 8]

data_actual_df_br = arr_birads_real
data_predicted_df_bpa = arr_uta7_birads_physician_assistant
data_predicted_df_bpap = arr_uta11_birads_pysician_assistant_personalized

ds_df001 = np.array(data_actual_df_br, dtype=int)
ds_df002 = np.array(data_predicted_df_bpa, dtype=int)
ds_df003 = np.array(data_predicted_df_bpap, dtype=int)

# print(data_actual_df_br)
# print(data_predicted_df_bpa)
# print(data_predicted_df_bpap)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#              TIMES             #
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

# print(arr001)
# print(arr002)
# print(arr003)
# print(arr004)
# print(arr005)
# print(arr006)
# print(arr007)
# print(arr008)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#            CONDITIONS          #
# ============================== #
# ============================== #

data_times_df_el_novice = data_times_df.loc[data_times_df[3] == 'Novice']
data_times_df_el_expert = data_times_df.loc[data_times_df[3] == 'Expert']

data_times_df_el_novice_low = data_times_df_el_novice.loc[data_times_df_el_novice[4] == 'low']
data_times_df_el_novice_medium = data_times_df_el_novice.loc[data_times_df_el_novice[4] == 'medium']
data_times_df_el_novice_high = data_times_df_el_novice.loc[data_times_df_el_novice[4] == 'high']

data_times_df_el_expert_low = data_times_df_el_expert.loc[data_times_df_el_expert[4] == 'low']
data_times_df_el_expert_medium = data_times_df_el_expert.loc[data_times_df_el_expert[4] == 'medium']
data_times_df_el_expert_high = data_times_df_el_expert.loc[data_times_df_el_expert[4] == 'high']

dt_df_enl_uta7 = data_times_df_el_novice_low[6]
dt_df_enm_uta7 = data_times_df_el_novice_medium[6]
dt_df_enh_uta7 = data_times_df_el_novice_high[6]

dt_df_eel_uta7 = data_times_df_el_expert_low[6]
dt_df_eem_uta7 = data_times_df_el_expert_medium[6]
dt_df_eeh_uta7 = data_times_df_el_expert_high[6]

dt_df_enl_uta11 = data_times_df_el_novice_low[7]
dt_df_enm_uta11 = data_times_df_el_novice_medium[7]
dt_df_enh_uta11 = data_times_df_el_novice_high[7]

dt_df_eel_uta11 = data_times_df_el_expert_low[7]
dt_df_eem_uta11 = data_times_df_el_expert_medium[7]
dt_df_eeh_uta11 = data_times_df_el_expert_high[7]

dt_df001 = np.array(dt_df_enl_uta7.to_numpy(), dtype=float)
dt_df002 = np.array(dt_df_enm_uta7.to_numpy(), dtype=float)
dt_df003 = np.array(dt_df_enh_uta7.to_numpy(), dtype=float)

dt_df004 = np.array(dt_df_eel_uta7.to_numpy(), dtype=float)
dt_df005 = np.array(dt_df_eem_uta7.to_numpy(), dtype=float)
dt_df006 = np.array(dt_df_eeh_uta7.to_numpy(), dtype=float)

dt_df007 = np.array(dt_df_enl_uta11.to_numpy(), dtype=float)
dt_df008 = np.array(dt_df_enm_uta11.to_numpy(), dtype=float)
dt_df009 = np.array(dt_df_enh_uta11.to_numpy(), dtype=float)

dt_df010 = np.array(dt_df_eel_uta11.to_numpy(), dtype=float)
dt_df011 = np.array(dt_df_eem_uta11.to_numpy(), dtype=float)
dt_df012 = np.array(dt_df_eeh_uta11.to_numpy(), dtype=float)

arr_concat001 = np.concatenate((dt_df001, dt_df004))
arr_concat002 = np.concatenate((dt_df002, dt_df005))
arr_concat003 = np.concatenate((dt_df003, dt_df006))

arr_concat004 = np.concatenate((dt_df007, dt_df010))
arr_concat005 = np.concatenate((dt_df008, dt_df011))
arr_concat006 = np.concatenate((dt_df009, dt_df012))

arr_concat007 = np.concatenate((arr_concat001, arr_concat004))
arr_concat008 = np.concatenate((arr_concat002, arr_concat005))
arr_concat009 = np.concatenate((arr_concat003, arr_concat006))

dt_df_enl_uta7_n = data_times_df_el_novice_low[3]
dt_df_enm_uta7_n = data_times_df_el_novice_medium[3]
dt_df_enh_uta7_n = data_times_df_el_novice_high[3]

dt_df_eel_uta7_e = data_times_df_el_expert_low[3]
dt_df_eem_uta7_e = data_times_df_el_expert_medium[3]
dt_df_eeh_uta7_e = data_times_df_el_expert_high[3]

dt_df_enl_uta11_n = data_times_df_el_novice_low[3]
dt_df_enm_uta11_n = data_times_df_el_novice_medium[3]
dt_df_enh_uta11_n = data_times_df_el_novice_high[3]

dt_df_eel_uta11_e = data_times_df_el_expert_low[3]
dt_df_eem_uta11_e = data_times_df_el_expert_medium[3]
dt_df_eeh_uta11_e = data_times_df_el_expert_high[3]

dt_df013 = dt_df_enl_uta7_n.to_numpy()
dt_df014 = dt_df_enm_uta7_n.to_numpy()
dt_df015 = dt_df_enh_uta7_n.to_numpy()

dt_df016 = dt_df_eel_uta7_e.to_numpy()
dt_df017 = dt_df_eem_uta7_e.to_numpy()
dt_df018 = dt_df_eeh_uta7_e.to_numpy()

dt_df019 = dt_df_enl_uta11_n.to_numpy()
dt_df020 = dt_df_enm_uta11_n.to_numpy()
dt_df021 = dt_df_enh_uta11_n.to_numpy()

dt_df022 = dt_df_eel_uta11_e.to_numpy()
dt_df023 = dt_df_eem_uta11_e.to_numpy()
dt_df024 = dt_df_eeh_uta11_e.to_numpy()

arr_concat010 = np.concatenate((dt_df013, dt_df016))
arr_concat011 = np.concatenate((dt_df014, dt_df017))
arr_concat012 = np.concatenate((dt_df015, dt_df018))

arr_concat013 = np.concatenate((dt_df019, dt_df022))
arr_concat014 = np.concatenate((dt_df020, dt_df023))
arr_concat015 = np.concatenate((dt_df021, dt_df024))

arr_concat016 = np.concatenate((arr_concat010, arr_concat013))
arr_concat017 = np.concatenate((arr_concat011, arr_concat014))
arr_concat018 = np.concatenate((arr_concat012, arr_concat015))

# print(dt_df001)
# print(dt_df002)
# print(dt_df003)

# print(dt_df004)
# print(dt_df005)
# print(dt_df006)

# print(dt_df007)
# print(dt_df008)
# print(dt_df009)

# print(dt_df010)
# print(dt_df011)
# print(dt_df012)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#           PREFERENCES          #
# ============================== #
# ============================== #

data_preferences_df = pd.read_csv(preferences_abs_path, header=None)
data_preferences = data_preferences_df.to_numpy()

arr_uta11_preferences_q7 = data_preferences[1:, 11]
arr_uta11_preferences_q8 = data_preferences[1:, 12]
arr_uta11_preferences_q9 = data_preferences[1:, 13]

arr_p_q7 = np.array(arr_uta11_preferences_q7, dtype=int)
arr_p_q8 = np.array(arr_uta11_preferences_q8, dtype=int)
arr_p_q9 = np.array(arr_uta11_preferences_q9, dtype=int)

arr_p_q7_1 = (arr_p_q7 == 1).sum()
arr_p_q7_2 = (arr_p_q7 == 2).sum()
arr_p_q7_3 = (arr_p_q7 == 3).sum()
arr_p_q7_4 = (arr_p_q7 == 4).sum()
arr_p_q7_5 = (arr_p_q7 == 5).sum()
arr_p_q7_6 = (arr_p_q7 == 6).sum()
arr_p_q7_7 = (arr_p_q7 == 7).sum()

# print(arr_p_q7_1)
# print(arr_p_q7_2)
# print(arr_p_q7_3)
# print(arr_p_q7_4)
# print(arr_p_q7_5)
# print(arr_p_q7_6)
# print(arr_p_q7_7)

# print("==============================")

arr_p_q8_1 = (arr_p_q8 == 1).sum()
arr_p_q8_2 = (arr_p_q8 == 2).sum()
arr_p_q8_3 = (arr_p_q8 == 3).sum()
arr_p_q8_4 = (arr_p_q8 == 4).sum()
arr_p_q8_5 = (arr_p_q8 == 5).sum()
arr_p_q8_6 = (arr_p_q8 == 6).sum()
arr_p_q8_7 = (arr_p_q8 == 7).sum()

# print(arr_p_q8_1)
# print(arr_p_q8_2)
# print(arr_p_q8_3)
# print(arr_p_q8_4)
# print(arr_p_q8_5)
# print(arr_p_q8_6)
# print(arr_p_q8_7)

# print("==============================")

arr_p_q9_1 = (arr_p_q9 == 1).sum()
arr_p_q9_2 = (arr_p_q9 == 2).sum()
arr_p_q9_3 = (arr_p_q9 == 3).sum()
arr_p_q9_4 = (arr_p_q9 == 4).sum()
arr_p_q9_5 = (arr_p_q9 == 5).sum()
arr_p_q9_6 = (arr_p_q9 == 6).sum()
arr_p_q9_7 = (arr_p_q9 == 7).sum()

# print(arr_p_q9_1)
# print(arr_p_q9_2)
# print(arr_p_q9_3)
# print(arr_p_q9_4)
# print(arr_p_q9_5)
# print(arr_p_q9_6)
# print(arr_p_q9_7)

# print("==============================")

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ========== END File ========== #