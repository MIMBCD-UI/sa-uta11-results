#!/usr/bin/env python
#coding=utf-8

"""
basic_statistics.py: this file has one sample Wilcoxon signed rank test
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

from cmath import nan
from glob import glob
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import pandas as pd
import plotly.express as px
import datetime as dt
import statsmodels.api as sm
import pylab
import scikit_posthocs as sk

import sys
# sys.path is a list of absolute path strings
sys.path.append('../constants')
sys.path.append('../methods')

from sheets import data
from groups import interns, juniors, seniors, assertive, non_assertive, proactive, reactive, getScenarios
from outliers import reject_outliers

def arrayMedianDifference(a, subtraction):
    return [x - subtraction for x in a]

def wilcoxonPreference(firstIndex, lastIndex, medHypNovice, medHypSenior):
    lastIndex += 1

    mean_sample_data_intern = []
    mean_sample_data_junior = []
    mean_sample_data_novice = []
    mean_sample_data_senior = []

    scenarios_novices = getScenarios(interns)[::3]

    scenarios_novices.extend(getScenarios(juniors)[::3])

    for i in getScenarios(interns)[::3]:

        sample_data_intern_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        mean_sample_data_intern.append(np.nanmean(sample_data_intern_i))

    for i in getScenarios(juniors)[::3]:

        sample_data_junior_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        mean_sample_data_junior.append(np.nanmean(sample_data_junior_i))

    for i in scenarios_novices:

        sample_data_novice_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        mean_sample_data_novice.append(np.nanmean(sample_data_novice_i))

    for i in getScenarios(seniors)[::3]:

        sample_data_senior_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        mean_sample_data_senior.append(np.nanmean(sample_data_senior_i))
    
    mean_sample_data_intern = [x for x in mean_sample_data_intern if str(x) != 'nan']
    mean_sample_data_junior = [x for x in mean_sample_data_junior if str(x) != 'nan']
    mean_sample_data_novice = [x for x in mean_sample_data_novice if str(x) != 'nan']
    mean_sample_data_senior = [x for x in mean_sample_data_senior if str(x) != 'nan']

    print(mean_sample_data_intern)
    print(mean_sample_data_junior)
    print(mean_sample_data_novice)
    print(mean_sample_data_senior)

    # print("---Intern---")
    # print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_intern, medHypNovice)))

    # print("---Junior---")
    # print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_junior, medHypNovice)))

    print(arrayMedianDifference(mean_sample_data_novice, medHypNovice))
    print(arrayMedianDifference(mean_sample_data_senior, medHypSenior))

    print("---Novice---")
    # print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_novice, medHypNovice)))
    print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_novice, medHypNovice), alternative="greater"))
    # print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_novice, medHypNovice), alternative="less"))

    print("---Senior---")
    # print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_senior, medHypSenior)))
    print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_senior, medHypSenior), alternative="less"))
    # print(sp.stats.wilcoxon(arrayMedianDifference(mean_sample_data_novice, medHypNovice), alternative="greater"))


    
def main():

    print("-------------- PREFERENCE ---------------")

    print("-------------- ASSERTIVENESS ---------------")
    # wilcoxonPreference(24,26, 1, 7)
    # wilcoxonPreference(24,26, 2, 6)
    wilcoxonPreference(24,26, 3, 5)
    # wilcoxonPreference(24,26, 4, 4)
    # wilcoxonPreference(26,26, 5, 3)
    # wilcoxonPreference(24,26, 6, 2)
    # wilcoxonPreference(24,26, 7, 1)

    print("-------------- BEHAVIOUR ---------------")
    # wilcoxonPreference(27,29, 1, 7)
    # wilcoxonPreference(27,29, 2, 6)
    # wilcoxonPreference(27,29, 3, 5)
    # wilcoxonPreference(27,29, 4, 4)
    # wilcoxonPreference(27,29, 5, 3)
    # wilcoxonPreference(27,29, 6, 2)
    # wilcoxonPreference(27,29, 7, 1)

if __name__ == "__main__":
    main()
