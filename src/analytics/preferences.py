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

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

# ========== END File ========== #