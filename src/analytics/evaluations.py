#!/usr/bin/env python
#coding=utf-8

"""
evaluations.py: evaluate the models using both plots and
                performance metrics.
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

from os import path

import plotly
import plotly.graph_objects as go
import plotly.io as pio

import seaborn as sn
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from pretty_confusion_matrix import pp_matrix

# ============================== #
# ============================== #
#               PATH             #
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

# ============================== #
# ============================== #
#           EVALUATIONS          #
# ============================== #
# ============================== #

# TODO: Add evaluations

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ========== END File ========== #