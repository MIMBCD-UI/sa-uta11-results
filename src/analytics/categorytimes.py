#!/usr/bin/env python
#coding=utf-8

"""
categorytimes.py: metrics for time analysis per clinician's category level.
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "0.1.1"
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
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.offline as pyo

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
# Add the directory containing the module to the Python path (wants absolute paths).
sys.path.append(pathRepoAbsPath)

# The path to the repository "src" folder.
joinRepoSrcPath = os.path.join(joinRepoPath, 'src')
pathRepoSrcAbsPath = os.path.abspath(joinRepoSrcPath)
# Add the directory containing the module to the Python path (wants absolute paths).
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

# File names
file_name_times = "mimbcdui_uta7_uta11_results_curated_abimid_times.csv"
file_name_category_times = "mimbcdui_uta7_uta11_results_curated_abimid_category_times"

# Load the data
file_path = os.path.join(pathRepoAbsPath, 'data', file_name_times)
print(f"Looking for the file at: {file_path}")
if not os.path.isfile(file_path):
    print(f"Error: The file '{file_path}' does not exist.")
    sys.exit(1)

data = pd.read_csv(file_path)

# Create a combined category for plotting
data['category_assistance'] = data['category_level'].astype(str) + ' - No AI'
fig = go.Figure()

# Plotting the data
fig.add_trace(go.Box(
    name='No AI',
    y=data['uta4_time_on_task_no_ai'],
    x=data['category_level'],
    marker_color='rgb(158,202,225)',
    marker_line_color='rgb(8,48,107)',
    marker_line_width=1.5,
    opacity=0.6,
    boxpoints='all',
    jitter=0.3
))

fig.add_trace(go.Box(
    name='Physician Assistant',
    y=data['uta7_time_on_task_physician_assistant'],
    x=data['category_level'],
    marker_color='rgb(255,127,14)',
    marker_line_color='rgb(8,48,107)',
    marker_line_width=1.5,
    opacity=0.6,
    boxpoints='all',
    jitter=0.3
))

fig.add_trace(go.Box(
    name='Personalized Physician Assistant',
    y=data['uta11_time_on_task_pysician_assistant_personalized'],
    x=data['category_level'],
    marker_color='rgb(44,160,44)',
    marker_line_color='rgb(8,48,107)',
    marker_line_width=1.5,
    opacity=0.6,
    boxpoints='all',
    jitter=0.3
))

fig.update_layout(
    title='Time on Task by Category Level and Assistance Type',
    xaxis=dict(title='Category Level', tickangle=-45),
    yaxis=dict(title='Time on Task (seconds)'),
    boxmode='group',
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)'
)

# Save the plot
fn_to_save_html = os.path.join(plotsAbsPath, file_name_category_times + '.html')
fn_to_save_png = os.path.join(visAbsPath, file_name_category_times + '.png')
pyo.plot(fig, filename=fn_to_save_html, auto_open=False)
pio.write_image(fig, fn_to_save_png)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ========== END File ========== #