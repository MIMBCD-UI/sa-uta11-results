#!/usr/bin/env python
#coding=utf-8

"""
paths.py: will serve the purpose of bringing the paths to the
          different folders and files.
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

# ==================== END File ==================== #