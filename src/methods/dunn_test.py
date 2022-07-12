#!/usr/bin/env python
#coding=utf-8

"""
dunn_test.py: this file has post hoc test (Dunn's Test)
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

def dunnTestPreference(firstIndex, lastIndex):
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

    print("---Intern vs Junior vs Senior---")
    mean_sample_data = [mean_sample_data_intern, mean_sample_data_junior,mean_sample_data_senior]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))

    print("---Novice vs Expert---")
    mean_sample_data = [mean_sample_data_novice,mean_sample_data_senior]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))

def dunnTestBehaviour(firstIndex, lastIndex):
    lastIndex += 1

    mean_sample_data_intern_proactive = []
    mean_sample_data_intern_reactive = []
    mean_sample_data_junior_proactive = []
    mean_sample_data_junior_reactive = []
    mean_sample_data_senior_proactive = []
    mean_sample_data_senior_reactive = []

    for i in getScenarios(interns):

        if(i+1 in proactive):

            nan_outliers_sample_data_intern_proactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_intern_proactive_i = nan_outliers_sample_data_intern_proactive_i[~np.isnan(nan_outliers_sample_data_intern_proactive_i)]
            sample_data_intern_proactive_i = outliers_sample_data_intern_proactive_i

            mean_sample_data_intern_proactive.append(np.mean(sample_data_intern_proactive_i))

        if(i+1 in reactive):

            nan_outliers_sample_data_intern_reactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_intern_reactive_i = nan_outliers_sample_data_intern_reactive_i[~np.isnan(nan_outliers_sample_data_intern_reactive_i)]
            sample_data_intern_reactive_i = outliers_sample_data_intern_reactive_i

            mean_sample_data_intern_reactive.append(np.mean(sample_data_intern_reactive_i))

    for i in getScenarios(juniors):

        if(i+1 in proactive):

            nan_outliers_sample_data_junior_proactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_proactive_i = nan_outliers_sample_data_junior_proactive_i[~np.isnan(nan_outliers_sample_data_junior_proactive_i)]
            sample_data_junior_proactive_i = outliers_sample_data_junior_proactive_i

            mean_sample_data_junior_proactive.append(np.mean(sample_data_junior_proactive_i))

        if(i+1 in reactive):

            nan_outliers_sample_data_junior_reactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_reactive_i = nan_outliers_sample_data_junior_reactive_i[~np.isnan(nan_outliers_sample_data_junior_reactive_i)]
            sample_data_junior_reactive_i = outliers_sample_data_junior_reactive_i

            mean_sample_data_junior_reactive.append(np.mean(sample_data_junior_reactive_i))

    for i in getScenarios(seniors):

        if(i+1 in proactive):

            nan_outliers_sample_data_senior_proactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_proactive_i = nan_outliers_sample_data_senior_proactive_i[~np.isnan(nan_outliers_sample_data_senior_proactive_i)]
            sample_data_senior_proactive_i = outliers_sample_data_senior_proactive_i

            mean_sample_data_senior_proactive.append(np.mean(sample_data_senior_proactive_i))

        if(i+1 in reactive):

            nan_outliers_sample_data_senior_reactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_reactive_i = nan_outliers_sample_data_senior_reactive_i[~np.isnan(nan_outliers_sample_data_senior_reactive_i)]
            sample_data_senior_reactive_i = outliers_sample_data_senior_reactive_i

            mean_sample_data_senior_reactive.append(np.mean(sample_data_senior_reactive_i))
    
    print(mean_sample_data_intern_proactive)
    print(mean_sample_data_intern_reactive)
    print(mean_sample_data_junior_proactive)
    print(mean_sample_data_junior_reactive)
    print(mean_sample_data_senior_proactive)
    print(mean_sample_data_senior_reactive)

    print("---Intern Proactive vs Reactive---")
    mean_sample_data = [mean_sample_data_intern_proactive, mean_sample_data_intern_reactive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))
    print("---Junior Proactive vs Reactive---")
    mean_sample_data = [mean_sample_data_junior_proactive, mean_sample_data_junior_reactive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))
    print("---Senior Proactive vs Reactive---")
    mean_sample_data = [mean_sample_data_senior_proactive, mean_sample_data_senior_reactive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))

    print("---Intern Proactive vs Junior Proactive vs Senior Proactive---")
    mean_sample_data = [mean_sample_data_intern_proactive, mean_sample_data_junior_proactive, mean_sample_data_senior_proactive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))
    
    print("---Intern Reactive vs Junior Reactive vs Senior Reactive---")
    mean_sample_data = [mean_sample_data_intern_reactive, mean_sample_data_junior_reactive, mean_sample_data_senior_reactive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))

def dunnTestAssertiveness(firstIndex, lastIndex):
    lastIndex += 1

    mean_sample_data_intern_assertive = []
    mean_sample_data_intern_non_assertive = []
    mean_sample_data_junior_assertive = []
    mean_sample_data_junior_non_assertive = []
    mean_sample_data_senior_assertive = []
    mean_sample_data_senior_non_assertive = []

    for i in getScenarios(interns):

        if(i+1 in assertive):

            nan_outliers_sample_data_intern_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_intern_assertive_i = nan_outliers_sample_data_intern_assertive_i[~np.isnan(nan_outliers_sample_data_intern_assertive_i)]
            sample_data_intern_assertive_i = outliers_sample_data_intern_assertive_i

            mean_sample_data_intern_assertive.append(np.mean(sample_data_intern_assertive_i))

        if(i+1 in non_assertive):

            nan_outliers_sample_data_intern_non_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_intern_non_assertive_i = nan_outliers_sample_data_intern_non_assertive_i[~np.isnan(nan_outliers_sample_data_intern_non_assertive_i)]
            sample_data_intern_non_assertive_i = outliers_sample_data_intern_non_assertive_i

            mean_sample_data_intern_non_assertive.append(np.mean(sample_data_intern_non_assertive_i))

    for i in getScenarios(juniors):

        if(i+1 in assertive):

            nan_outliers_sample_data_junior_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_assertive_i = nan_outliers_sample_data_junior_assertive_i[~np.isnan(nan_outliers_sample_data_junior_assertive_i)]
            sample_data_junior_assertive_i = outliers_sample_data_junior_assertive_i

            mean_sample_data_junior_assertive.append(np.mean(sample_data_junior_assertive_i))

        if(i+1 in non_assertive):

            nan_outliers_sample_data_junior_non_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_non_assertive_i = nan_outliers_sample_data_junior_non_assertive_i[~np.isnan(nan_outliers_sample_data_junior_non_assertive_i)]
            sample_data_junior_non_assertive_i = outliers_sample_data_junior_non_assertive_i

            mean_sample_data_junior_non_assertive.append(np.mean(sample_data_junior_non_assertive_i))

    for i in getScenarios(seniors):

        if(i+1 in assertive):

            nan_outliers_sample_data_senior_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_assertive_i = nan_outliers_sample_data_senior_assertive_i[~np.isnan(nan_outliers_sample_data_senior_assertive_i)]
            sample_data_senior_assertive_i = outliers_sample_data_senior_assertive_i

            mean_sample_data_senior_assertive.append(np.mean(sample_data_senior_assertive_i))

        if(i+1 in non_assertive):

            nan_outliers_sample_data_senior_non_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_non_assertive_i = nan_outliers_sample_data_senior_non_assertive_i[~np.isnan(nan_outliers_sample_data_senior_non_assertive_i)]
            sample_data_senior_non_assertive_i = outliers_sample_data_senior_non_assertive_i

            mean_sample_data_senior_non_assertive.append(np.mean(sample_data_senior_non_assertive_i))
    
    print(mean_sample_data_intern_assertive)
    print(mean_sample_data_intern_non_assertive)
    print(mean_sample_data_junior_assertive)
    print(mean_sample_data_junior_non_assertive)
    print(mean_sample_data_senior_assertive)
    print(mean_sample_data_senior_non_assertive)

    print("---Intern Assertive vs Non Assertive---")
    mean_sample_data = [mean_sample_data_intern_assertive, mean_sample_data_intern_non_assertive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))
    print("---Junior Assertive vs Non Assertive---")
    mean_sample_data = [mean_sample_data_junior_assertive, mean_sample_data_junior_non_assertive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))
    print("---Senior Assertive vs Non Assertive---")
    mean_sample_data = [mean_sample_data_senior_assertive, mean_sample_data_senior_non_assertive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))

    print("---Intern Assertive vs Junior Assertive vs Senior Assertive---")
    mean_sample_data = [mean_sample_data_intern_assertive, mean_sample_data_junior_assertive,mean_sample_data_senior_assertive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))
    
    print("---Intern Non Assertive vs Junior Non Assertive vs Senior Non Assertive---")
    mean_sample_data = [mean_sample_data_intern_non_assertive, mean_sample_data_junior_non_assertive, mean_sample_data_senior_non_assertive]
    print(sk.posthoc_dunn(mean_sample_data, sort=True))
    


    
def main():

    # #BIRADS
    # print("-------------- BIRADS ---------------")
    # kruskalWallis(3)

    # #Time
    # print("-------------- TIME ---------------")
    # print("-------------- ASSERTIVENESS ---------------")
    # dunnTestAssertiveness(4,4)
    # print("-------------- BEHAVIOUR ---------------")
    # dunnTestBehaviour(4,4)

    # print("-------------- UX ---------------")

    # print("-------------- ASSERTIVENESS ---------------")

    # #DOTS
    # print("-------------- DOTS ---------------")
    # dunnTestAssertiveness(5,7)

    # #SUS
    # print("-------------- SUS ---------------")
    # dunnTestAssertiveness(8,17)

    # #NASA-TLX
    # print("-------------- NASA-TLX ---------------")
    # dunnTestAssertiveness(18,23)

    # print("-------------- BEHAVIOUR ---------------")
    # #DOTS
    # print("-------------- DOTS ---------------")
    # dunnTestBehaviour(5,7)

    # #SUS
    # print("-------------- SUS ---------------")
    # dunnTestBehaviour(8,17)

    # #NASA-TLX
    # print("-------------- NASA-TLX ---------------")
    # dunnTestBehaviour(18,23)
    

    print("-------------- PREFERENCE ---------------")

    print("-------------- ASSERTIVENESS ---------------")
    dunnTestPreference(24,26)

    print("-------------- BEHAVIOUR ---------------")
    dunnTestPreference(27,29)


    # #Q4
    # print("-------------- INFLUENCE ---------------")

    # dunnTestBehaviour(3,3)

if __name__ == "__main__":
    main()
