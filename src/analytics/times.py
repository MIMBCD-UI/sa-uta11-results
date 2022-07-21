#!/usr/bin/env python
#coding=utf-8

"""
times.py: metrics for time analysis.
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

import plotly
import plotly.graph_objects as go
import plotly.io as pio

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

# Appending stats path
statsPath = os.path.join(joinRepoPath, 'stats')
statsAbsPath = os.path.abspath(statsPath)
sys.path.append(statsAbsPath)
sys.path.insert(0, statsAbsPath)

# Appending visualizations path
visPath = os.path.join(statsPath, 'visualizations')
visAbsPath = os.path.abspath(visPath)
sys.path.append(visAbsPath)
sys.path.insert(0, visAbsPath)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# Importing available constants
from sheets import *

file_name_times = "mimbcdui_uta7_uta11_results_curated_abimid_times"

# ============================== #
# ============================== #
#              TIMES             #
# ============================== #
# ============================== #

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
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    font=dict(
        size=18,
    ),
    legend=dict(font=dict(size = 12)),
    legend_title=dict(font=dict(size = 18)),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=True,
    boxmode='group'
)

fig.update_traces(orientation='h', boxpoints='suspectedoutliers') # horizontal box plots
# fig.show()

fn_to_save_html = plotsAbsPath + '/' + file_name_times + '.html'
fn_to_save_png = visAbsPath + '/' + file_name_times + '.png'
plotly.offline.plot(fig, filename=fn_to_save_html, auto_open=False)
pio.write_image(fig, fn_to_save_png)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ========== END File ========== #