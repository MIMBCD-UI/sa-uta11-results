#!/usr/bin/env python
#coding=utf-8

"""
metrics.py: metrics for accuracy analysis.
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
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# ============================== #
# ============================== #
#              PATHS             #
# ============================== #
# ============================== #

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository base folder.
joinRepoPath = os.path.join(basePath, '..', '..')
pathRepoAbsPath = os.path.abspath(joinRepoPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathRepoAbsPath)

# The path to the repository "src" folder.
joinRepoSrcPath = os.path.join(joinRepoPath, 'src')
pathRepoSrcAbsPath = os.path.abspath(joinRepoSrcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathRepoSrcAbsPath)

# Appending constants path
constantsPath = os.path.join(joinRepoSrcPath, 'constants')
constantsAbsPath = os.path.abspath(constantsPath)
sys.path.append(constantsAbsPath)
sys.path.insert(0, constantsAbsPath)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# Importing available constants
from sheets import *

# ============================== #
# ============================== #
#           METRICS              #
# ============================== #
# ============================== #

# Define the correct headers
headers = [
    'uta7_uta11_scenario_id', 'uta11_id_clinician', 'category_level', 'expertise_level',
    'patient_severity_real_level', 'birads_real', 'uta4_birads_no_ai', 'uta7_birads_physician_assistant',
    'uta11_birads_pysician_assistant_personalized', 'uta11_birads_assistant_personalized',
    'uta11_birads_physician_reactive_assistant_personalized', 'uta7_id', 'uta11_assertiveness_level'
]

# Read the CSV file with the correct headers
data_severities_df = pd.read_csv(severities_abs_path, names=headers)

# Extract actual and predicted BIRADS scores
y_true = data_severities_df['birads_real']
y_pred_no_ai = data_severities_df['uta4_birads_no_ai']
y_pred_pa = data_severities_df['uta7_birads_physician_assistant']
y_pred_pa_pers = data_severities_df['uta11_birads_pysician_assistant_personalized']
y_pred_assist_pers = data_severities_df['uta11_birads_assistant_personalized']

# Remove any potential non-integer values
y_true = y_true[y_true.str.isdigit()].astype(int)
y_pred_no_ai = y_pred_no_ai[y_pred_no_ai.str.isdigit()].astype(int)
y_pred_pa = y_pred_pa[y_pred_pa.str.isdigit()].astype(int)
y_pred_pa_pers = y_pred_pa_pers[y_pred_pa_pers.str.isdigit()].astype(int)
y_pred_assist_pers = y_pred_assist_pers[y_pred_assist_pers.str.isdigit()].astype(int)

# Calculate overall accuracy
accuracy_no_ai = accuracy_score(y_true, y_pred_no_ai)
accuracy_pa = accuracy_score(y_true, y_pred_pa)
accuracy_pa_pers = accuracy_score(y_true, y_pred_pa_pers)
accuracy_assist_pers = accuracy_score(y_true, y_pred_assist_pers)

# Calculate precision, recall, and F1 score
metrics_no_ai = precision_recall_fscore_support(y_true, y_pred_no_ai, average=None, zero_division=1)
metrics_pa = precision_recall_fscore_support(y_true, y_pred_pa, average=None, zero_division=1)
metrics_pa_pers = precision_recall_fscore_support(y_true, y_pred_pa_pers, average=None, zero_division=1)
metrics_assist_pers = precision_recall_fscore_support(y_true, y_pred_assist_pers, average=None, zero_division=1)

# Print lengths for debugging
print("Unique BIRADS Classes:", np.unique(y_true))
print("Length of metrics_no_ai:", len(metrics_no_ai[0]))
print("Length of metrics_pa:", len(metrics_pa[0]))
print("Length of metrics_pa_pers:", len(metrics_pa_pers[0]))
print("Length of metrics_assist_pers:", len(metrics_assist_pers[0]))

# Combine metrics into a DataFrame for visualization
metrics_df = pd.DataFrame({
    'Precision No AI': metrics_no_ai[0],
    'Recall No AI': metrics_no_ai[1],
    'F1 Score No AI': metrics_no_ai[2],
    'Precision PA': metrics_pa[0],
    'Recall PA': metrics_pa[1],
    'F1 Score PA': metrics_pa[2],
    'Precision PA Pers': metrics_pa_pers[0],
    'Recall PA Pers': metrics_pa_pers[1],
    'F1 Score PA Pers': metrics_pa_pers[2],
    'Precision Assist Pers': metrics_assist_pers[0],
    'Recall Assist Pers': metrics_assist_pers[1],
    'F1 Score Assist Pers': metrics_assist_pers[2]
}, index=np.unique(y_true))

# Plot overall accuracy
plt.figure(figsize=(10, 6))
accuracy_scores = [accuracy_no_ai, accuracy_pa, accuracy_pa_pers, accuracy_assist_pers]
models = ['No AI', 'Physician Assistant', 'PA Personalized', 'Assistant Personalized']
plt.bar(models, accuracy_scores, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.title('Overall Accuracy for Different Models')
plt.ylim(0, 1)
plt.show()

# Plot precision, recall, and F1 score for each class
metrics_df.plot(kind='bar', figsize=(14, 8))
plt.xlabel('BIRADS Class')
plt.ylabel('Score')
plt.title('Precision, Recall, and F1 Score for Different Models')
plt.xticks(rotation=0)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ========== END File ========== #