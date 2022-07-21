#!/usr/bin/env python
#coding=utf-8

"""
accuracies.py: metrics for accuracy analysis.
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
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

from os import path

import seaborn as sn
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from pretty_confusion_matrix import pp_matrix

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
#            ACCURACY            #
# ============================== #
# ============================== #

# print(ds_df001)
# print(ds_df002)

confusion_matrix_bpa = confusion_matrix(ds_df001, ds_df002, normalize='all')
confusion_matrix_bpap = confusion_matrix(ds_df001, ds_df003, normalize='all')

# print(confusion_matrix_bpa)
# print(confusion_matrix_bpa[0:, 0])

# print(confusion_matrix_bpap)
# print(confusion_matrix_bpap[0:, 0])

df_cm_bpa = pd.DataFrame(confusion_matrix_bpa, columns=np.unique(ds_df001), index = np.unique(ds_df001))
df_cm_bpa.index.name = 'Actual'
df_cm_bpa.columns.name = 'Predicted'
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm_bpa, vmin=0, vmax=1, cmap="Blues", annot=True,annot_kws={"size": 16})# font size
plt.show()

df_cm_bpap = pd.DataFrame(confusion_matrix_bpap, columns=np.unique(ds_df001), index = np.unique(ds_df001))
df_cm_bpap.index.name = 'Actual'
df_cm_bpap.columns.name = 'Predicted'
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm_bpap, vmin=0, vmax=1, cmap="Blues", annot=True,annot_kws={"size": 16})# font size
plt.show()

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ==================== END File ==================== #