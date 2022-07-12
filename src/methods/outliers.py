#!/usr/bin/env python
#coding=utf-8

"""
basic_statistics.py: this file has auxiliar functions to get outliers mathematically
"""

__author__      = "João Fernandes"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.0"
__status__      = "Development"
__copyright__   = "Copyright 2022, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

import numpy as np

def lower_bound(data):

    percentile25 = np.quantile(data, 0.25)
    percentile75 = np.quantile(data, 0.75)

    iqr = percentile75 - percentile25

    lower_limit = percentile25 - 1.5 * iqr

    return lower_limit

def upper_bound(data):

    percentile25 = np.quantile(data, 0.25)
    percentile75 = np.quantile(data, 0.75)

    iqr = percentile75 - percentile25

    upper_limit = percentile75 + 1.5 * iqr

    return upper_limit

def reject_outliers(data):

    upper_limit = upper_bound(data)
    lower_limit = lower_bound(data)

    data = np.delete(data, np.argwhere(data > upper_limit))
    data = np.delete(data, np.argwhere(data < lower_limit))

    return data