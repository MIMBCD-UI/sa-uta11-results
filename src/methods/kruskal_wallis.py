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

import sys
# sys.path is a list of absolute path strings
sys.path.append('../constants')
sys.path.append('../methods')

from sheets import data
from groups import interns, juniors, seniors, assertive, non_assertive, proactive, reactive, getScenarios
from outliers import reject_outliers

def kruskalWallisBehaviour(firstIndex, lastIndex):
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
    print(sp.stats.kruskal(mean_sample_data_intern_proactive, mean_sample_data_intern_reactive))
    print("---Junior Proactive vs Reactive---")
    print(sp.stats.kruskal(mean_sample_data_junior_proactive, mean_sample_data_junior_reactive))
    print("---Senior Proactive vs Reactive---")
    print(sp.stats.kruskal(mean_sample_data_senior_proactive, mean_sample_data_senior_reactive))

    print("---Intern Proactive vs Junior Proactive---")
    print(sp.stats.kruskal(mean_sample_data_intern_proactive, mean_sample_data_junior_proactive))
    print("---Intern Proactive vs Senior Proactive---")
    print(sp.stats.kruskal(mean_sample_data_intern_proactive, mean_sample_data_senior_proactive))
    print("---Junior Proactive vs Senior Proactive---")
    print(sp.stats.kruskal(mean_sample_data_junior_proactive, mean_sample_data_senior_proactive))
    
    print("---Intern Reactive vs Junior Reactive---")
    print(sp.stats.kruskal(mean_sample_data_intern_reactive, mean_sample_data_junior_reactive))
    print("---Intern Reactive vs Senior Reactive---")
    print(sp.stats.kruskal(mean_sample_data_intern_reactive, mean_sample_data_senior_reactive))
    print("---Junior Reactive vs Senior Reactive---")
    print(sp.stats.kruskal(mean_sample_data_junior_reactive, mean_sample_data_senior_reactive))

def kruskalWallisAssertiveness(firstIndex, lastIndex):
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
    print(sp.stats.kruskal(mean_sample_data_intern_assertive, mean_sample_data_intern_non_assertive))
    print("---Junior Assertive vs Non Assertive---")
    print(sp.stats.kruskal(mean_sample_data_junior_assertive, mean_sample_data_junior_non_assertive))
    print("---Senior Assertive vs Non Assertive---")
    print(sp.stats.kruskal(mean_sample_data_senior_assertive, mean_sample_data_senior_non_assertive))

    print("---Intern Assertive vs Junior Assertive---")
    print(sp.stats.kruskal(mean_sample_data_intern_assertive, mean_sample_data_junior_assertive))
    print("---Intern Assertive vs Senior Assertive---")
    print(sp.stats.kruskal(mean_sample_data_intern_assertive, mean_sample_data_senior_assertive))
    print("---Junior Assertive vs Senior Assertive---")
    print(sp.stats.kruskal(mean_sample_data_junior_assertive, mean_sample_data_senior_assertive))
    
    print("---Intern Non Assertive vs Junior Non Assertive---")
    print(sp.stats.kruskal(mean_sample_data_intern_non_assertive, mean_sample_data_junior_non_assertive))
    print("---Intern Non Assertive vs Senior Non Assertive---")
    print(sp.stats.kruskal(mean_sample_data_intern_non_assertive, mean_sample_data_senior_non_assertive))
    print("---Junior Non Assertive vs Senior Non Assertive---")
    print(sp.stats.kruskal(mean_sample_data_junior_non_assertive, mean_sample_data_senior_non_assertive))
    

def kruskalWallisInterval(firstIndex, lastIndex):
    lastIndex += 1

    mean_sample_data_intern = []
    mean_sample_data_junior = []
    mean_sample_data_senior = []

    for i in getScenarios(interns):
        nan_outliers_sample_data_intern_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        outliers_sample_data_intern_i = nan_outliers_sample_data_intern_i[~np.isnan(nan_outliers_sample_data_intern_i)]
        sample_data_intern_i = outliers_sample_data_intern_i

        mean_sample_data_intern.append(np.mean(sample_data_intern_i))

    for i in getScenarios(juniors):
        nan_outliers_sample_data_junior_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        outliers_sample_data_junior_i = nan_outliers_sample_data_junior_i[~np.isnan(nan_outliers_sample_data_junior_i)]
        sample_data_junior_i = outliers_sample_data_junior_i

        mean_sample_data_junior.append(np.mean(sample_data_junior_i))

    for i in getScenarios(seniors):
        nan_outliers_sample_data_senior_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        outliers_sample_data_senior_i = nan_outliers_sample_data_senior_i[~np.isnan(nan_outliers_sample_data_senior_i)]
        sample_data_senior_i = outliers_sample_data_senior_i

        mean_sample_data_senior.append(np.mean(sample_data_senior_i))
    
    print(mean_sample_data_intern)
    print(mean_sample_data_junior)
    print(mean_sample_data_senior)
    

    print(sp.stats.kruskal(mean_sample_data_intern, mean_sample_data_junior,mean_sample_data_senior))
    print(sp.stats.kruskal(mean_sample_data_intern, mean_sample_data_senior))
    print(sp.stats.kruskal(mean_sample_data_junior, mean_sample_data_senior))

def kruskalWallis(index):
    nan_outliers_sample_data_intern = np.float64(np.take(data[2:,index], getScenarios(interns)))
    nan_outliers_sample_data_junior = np.float64(np.take(data[2:,index], getScenarios(juniors)))
    nan_outliers_sample_data_senior = np.float64(np.take(data[2:,index], getScenarios(seniors)))

    outliers_sample_data_intern = nan_outliers_sample_data_intern[~np.isnan(nan_outliers_sample_data_intern)]
    outliers_sample_data_junior = nan_outliers_sample_data_junior[~np.isnan(nan_outliers_sample_data_junior)]
    outliers_sample_data_senior = nan_outliers_sample_data_senior[~np.isnan(nan_outliers_sample_data_senior)]

    sample_data_intern = outliers_sample_data_intern
    sample_data_junior = outliers_sample_data_junior
    sample_data_senior = outliers_sample_data_senior

    # sample_data_intern = reject_outliers(outliers_sample_data_intern)
    # sample_data_junior = reject_outliers(outliers_sample_data_junior)
    # sample_data_senior = reject_outliers(outliers_sample_data_senior)
    
    print(sample_data_intern)
    print(sample_data_junior)
    print(sample_data_senior)
    

    print(sp.stats.kruskal(sample_data_intern, sample_data_junior,sample_data_senior))

    
def main():

    # #BIRADS
    # print("-------------- BIRADS ---------------")
    # kruskalWallis(3)

    # #Time
    # print("-------------- TIME ---------------")
    # kruskalWallis(4)

    # # #DOTS
    # print("-------------- DOTS ---------------")
    # kruskalWallis(5)
    # kruskalWallis(6)
    # kruskalWallis(7)

    # #SUS
    # print("-------------- SUS ---------------")
    # kruskalWallis(8)
    # kruskalWallis(9)
    # kruskalWallis(10)
    # kruskalWallis(11)
    # kruskalWallis(12)
    # kruskalWallis(13)
    # kruskalWallis(14)
    # kruskalWallis(15)
    # kruskalWallis(16)
    # kruskalWallis(17)

    # #NASA-TLX
    # print("-------------- NASA-TLX ---------------")
    # kruskalWallis(18)
    # kruskalWallis(19)
    # kruskalWallis(20)
    # kruskalWallis(21)
    # kruskalWallis(22)
    # kruskalWallis(23)


    # #Preference
    # print("-------------- Preference ---------------")
    # kruskalWallis(24)
    # kruskalWallis(25)
    # kruskalWallis(26)
    # kruskalWallis(27)
    # kruskalWallis(28)
    # kruskalWallis(29)
    # kruskalWallis(30)
    # kruskalWallis(31)
    # kruskalWallis(32)

    print("-------------- ASSERTIVENESS ---------------")

    #DOTS
    print("-------------- DOTS ---------------")
    kruskalWallisAssertiveness(5,7)

    #SUS
    print("-------------- SUS ---------------")
    kruskalWallisAssertiveness(8,17)

    #NASA-TLX
    print("-------------- NASA-TLX ---------------")
    kruskalWallisAssertiveness(18,23)

    print("-------------- BEHAVIOUR ---------------")
    #DOTS
    print("-------------- DOTS ---------------")
    kruskalWallisBehaviour(5,7)

    #SUS
    print("-------------- SUS ---------------")
    kruskalWallisBehaviour(8,17)

    #NASA-TLX
    print("-------------- NASA-TLX ---------------")
    kruskalWallisBehaviour(18,23)
    




if __name__ == "__main__":
    main()
