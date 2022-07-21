#!/usr/bin/env python
#coding=utf-8

"""
accuracies.py: metrics for accuracy analysis.
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

from sheets import *

file_name_preferences = "mimbcdui_uta7_uta11_results_curated_abimid_preferences"

# ============================== #
# ============================== #
# ============================== #
# ============================== #

top_labels = ['Totally<br>Conventional',
              'Much<br>More',
              'Slightly<br>More',
              'Neutral',
              'Slightly<br>More',
              'Much<br>More',
              'Totally<br>Assertiveness-based']

colors = ['rgba(144, 12, 63, 1.0)',
          'rgba(142, 26, 71, 1.0)',
          'rgba(140, 41, 79, 1.0)',
          'rgba(130, 113, 119, 1.0)',
          'rgba(73, 172, 133, 1.0)',
          'rgba(42, 158, 113, 1.0)',
          'rgba(12, 144, 93, 1.0)']

x_data = [[arr_p_q9_1, arr_p_q9_2, arr_p_q9_3, arr_p_q9_4, arr_p_q9_5, arr_p_q9_6, arr_p_q9_7],
          [arr_p_q8_1, arr_p_q8_2, arr_p_q8_3, arr_p_q8_4, arr_p_q8_5, arr_p_q8_6, arr_p_q8_7],
          [arr_p_q7_1, arr_p_q7_2, arr_p_q7_3, arr_p_q7_4, arr_p_q7_5, arr_p_q7_6, arr_p_q7_7]]

y_data = ['Which agent did<br>you prefer overall?',
          'Which agent<br>was more capable?',
          'Which agent<br>was more reliable?']

fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=12, r=10, t=480, b=80),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=22,
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=22,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.2,
                                text=top_labels[0],
                                font=dict(family='Arial', size=18,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=22,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.2,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=18,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)

# fig.show()

fn_to_save_html = plotsAbsPath + '/' + file_name_preferences + '.html'
fn_to_save_png = visAbsPath + '/' + file_name_preferences + '.png'
plotly.offline.plot(fig, filename=fn_to_save_html, auto_open=False)
pio.write_image(fig, fn_to_save_png)

# ========== END File ========== #