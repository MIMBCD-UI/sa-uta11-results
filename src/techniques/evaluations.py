#!/usr/bin/env python
#coding=utf-8

"""
evaluations.py: evaluate the models using both plots and
                performance metrics.
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.0"
__status__      = "Development"
__copyright__   = "Copyright 2022, Instituto Superior Técnico (IST)"
__credits__     = [
  "João Fernandes",
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

import os
import sys
import logging

from os import path

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinRepoSrcPath = os.path.join(basePath, '..')
pathRepoSrcAbsPath = os.path.abspath(joinRepoSrcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathRepoSrcAbsPath)

# Appending methods path
methodsPath = os.path.join(joinRepoSrcPath, 'methods')
methodsAbsPath = os.path.abspath(methodsPath)
sys.path.append(methodsAbsPath)
sys.path.insert(0, methodsAbsPath)

# Importing available methods
from classifiers import *

def evalModelSpecific(df_real, df_pred):
	ccm = classConfusionMatrix(df_real, df_pred)
	cr = classReport(df_real, df_pred)
	return cr, ccm

# ==================== END File ==================== #