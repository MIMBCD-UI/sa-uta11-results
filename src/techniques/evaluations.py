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

# Appending constants path
constantsPath = os.path.join(joinRepoSrcPath, 'constants')
constantsAbsPath = os.path.abspath(constantsPath)
sys.path.append(constantsAbsPath)
sys.path.insert(0, constantsAbsPath)

# Importing available constants
from sheets import *

import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Box(
    x=arr_concat007,
    y=arr_concat016,
    name='Low',
    marker_color='#3D9970'
))
fig.add_trace(go.Box(
    x=arr_concat008,
    y=arr_concat017,
    name='Medium',
    marker_color='#FF4136'
))
fig.add_trace(go.Box(
    x=arr_concat009,
    y=arr_concat018,
    name='High',
    marker_color='#FF851B'
))

fig.update_layout(
    xaxis=dict(title='normalized moisture', zeroline=False),
    boxmode='group'
)

fig.update_traces(orientation='h') # horizontal box plots
fig.show()

# ==================== END File ==================== #