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

import plotly
import plotly.graph_objects as go

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

# Appending web path
webPath = os.path.join(joinRepoPath, 'web')
webAbsPath = os.path.abspath(webPath)
sys.path.append(webAbsPath)
sys.path.insert(0, webAbsPath)

# Appending plots path
plotsPath = os.path.join(webPath, 'plots')
plotsAbsPath = os.path.abspath(plotsPath)
sys.path.append(plotsAbsPath)
sys.path.insert(0, plotsAbsPath)

# Importing available constants
from sheets import *

file_name = "mimbcdui_uta7_uta11_results_curated_abimid_times"

# plotly.offline.init_notebook_mode()

fig = go.Figure()

fig.add_trace(go.Box(
    x=arr_concat003,
    y=arr_concat012,
    name='Conventional: High BIRADS',
    marker_color='#ff9944'
))
fig.add_trace(go.Box(
    x=arr_concat006,
    y=arr_concat015,
    name='Assertiveness-based: High BIRADS',
    marker_color='#eec400'
))
fig.add_trace(go.Box(
    x=arr_concat002,
    y=arr_concat011,
    name='Conventional: Medium BIRADS',
    marker_color='#0048ba'
))
fig.add_trace(go.Box(
    x=arr_concat005,
    y=arr_concat014,
    name='Assertiveness-based: Medium BIRADS',
    marker_color='#5ba8ff'
))
fig.add_trace(go.Box(
    x=arr_concat001,
    y=arr_concat010,
    name='Conventional: Low BIRADS',
    marker_color='#166461'
))
fig.add_trace(go.Box(
    x=arr_concat004,
    y=arr_concat013,
    name='Assertiveness-based: Low BIRADS',
    marker_color='#77aa77'
))

fig.update_layout(
    xaxis=dict(title='Diagnosing Time Performance (seconds)', zeroline=False),
    yaxis=dict(
        autorange=True,
        dtick=1,
    ),
    margin=dict(
        l=4,
        r=3,
        b=8,
        t=10,
    ),
    font=dict(
        size=18,
    ),
    legend=dict(font=dict(size = 18)),
    legend_title=dict(font=dict(size = 18)),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=True,
    boxmode='group'
)

fig.update_traces(orientation='h') # horizontal box plots
# fig.show()

print(plotsAbsPath)

fn_to_save = plotsAbsPath + '/' + file_name + '.html'
plotly.offline.plot(fig, filename = fn_to_save, auto_open = False)

# ==================== END File ==================== #