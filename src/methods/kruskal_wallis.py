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

def kruskalWallisPreference(firstIndex, lastIndex):
    lastIndex += 1

    mean_sample_data_intern = []
    mean_sample_data_junior = []
    mean_sample_data_senior = []

    for i in getScenarios(interns)[::3]:

        nan_outliers_sample_data_intern_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        outliers_sample_data_intern_i = nan_outliers_sample_data_intern_i[~np.isnan(nan_outliers_sample_data_intern_i)]
        sample_data_intern_i = outliers_sample_data_intern_i
        mean_sample_data_intern.append(np.mean(sample_data_intern_i))

    for i in getScenarios(juniors)[::3]:

        nan_outliers_sample_data_junior_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        outliers_sample_data_junior_i = nan_outliers_sample_data_junior_i[~np.isnan(nan_outliers_sample_data_junior_i)]
        sample_data_junior_i = outliers_sample_data_junior_i

        mean_sample_data_junior.append(np.mean(sample_data_junior_i))

    for i in getScenarios(seniors)[::3]:

        nan_outliers_sample_data_senior_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
        outliers_sample_data_senior_i = nan_outliers_sample_data_senior_i[~np.isnan(nan_outliers_sample_data_senior_i)]
        sample_data_senior_i = outliers_sample_data_senior_i

        mean_sample_data_senior.append(np.mean(sample_data_senior_i))
    
    print(mean_sample_data_intern)
    print(mean_sample_data_junior)
    print(mean_sample_data_senior)

    print("---Intern vs Junior---")
    print(sp.stats.kruskal(mean_sample_data_intern, mean_sample_data_junior))
    print("---Intern vs Senior---")
    print(sp.stats.kruskal(mean_sample_data_intern, mean_sample_data_senior))
    print("---Junior vs Senior---")
    print(sp.stats.kruskal(mean_sample_data_junior, mean_sample_data_senior))


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

            for k,y in enumerate(sample_data_intern_proactive_i):
                if(k % 2 == 1):
                    sample_data_intern_proactive_i[k] = 6 - y

            mean_sample_data_intern_proactive.append(np.mean(sample_data_intern_proactive_i))

        if(i+1 in reactive):

            nan_outliers_sample_data_intern_reactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_intern_reactive_i = nan_outliers_sample_data_intern_reactive_i[~np.isnan(nan_outliers_sample_data_intern_reactive_i)]
            sample_data_intern_reactive_i = outliers_sample_data_intern_reactive_i

            for k,y in enumerate(sample_data_intern_reactive_i):
                if(k % 2 == 1):
                    sample_data_intern_reactive_i[k] = 6 - y

            mean_sample_data_intern_reactive.append(np.mean(sample_data_intern_reactive_i))

    for i in getScenarios(juniors):

        if(i+1 in proactive):

            nan_outliers_sample_data_junior_proactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_proactive_i = nan_outliers_sample_data_junior_proactive_i[~np.isnan(nan_outliers_sample_data_junior_proactive_i)]
            sample_data_junior_proactive_i = outliers_sample_data_junior_proactive_i

            for k,y in enumerate(sample_data_junior_proactive_i):
                if(k % 2 == 1):
                    sample_data_junior_proactive_i[k] = 6 - y

            mean_sample_data_junior_proactive.append(np.mean(sample_data_junior_proactive_i))

        if(i+1 in reactive):

            nan_outliers_sample_data_junior_reactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_reactive_i = nan_outliers_sample_data_junior_reactive_i[~np.isnan(nan_outliers_sample_data_junior_reactive_i)]
            sample_data_junior_reactive_i = outliers_sample_data_junior_reactive_i

            for k,y in enumerate(sample_data_junior_reactive_i):
                if(k % 2 == 1):
                    sample_data_junior_reactive_i[k] = 6 - y

            mean_sample_data_junior_reactive.append(np.mean(sample_data_junior_reactive_i))

    for i in getScenarios(seniors):

        if(i+1 in proactive):

            nan_outliers_sample_data_senior_proactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_proactive_i = nan_outliers_sample_data_senior_proactive_i[~np.isnan(nan_outliers_sample_data_senior_proactive_i)]
            sample_data_senior_proactive_i = outliers_sample_data_senior_proactive_i

            for k,y in enumerate(sample_data_senior_proactive_i):
                if(k % 2 == 1):
                    sample_data_senior_proactive_i[k] = 6 - y

            mean_sample_data_senior_proactive.append(np.mean(sample_data_senior_proactive_i))

        if(i+1 in reactive):

            nan_outliers_sample_data_senior_reactive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_reactive_i = nan_outliers_sample_data_senior_reactive_i[~np.isnan(nan_outliers_sample_data_senior_reactive_i)]
            sample_data_senior_reactive_i = outliers_sample_data_senior_reactive_i

            for k,y in enumerate(sample_data_senior_reactive_i):
                if(k % 2 == 1):
                    sample_data_senior_reactive_i[k] = 6 - y

            mean_sample_data_senior_reactive.append(np.mean(sample_data_senior_reactive_i))
    
    mean_sample_data_novice_proactive = np.append(mean_sample_data_intern_proactive, mean_sample_data_junior_proactive)
    mean_sample_data_novice_reactive = np.append(mean_sample_data_intern_reactive, mean_sample_data_junior_reactive)

    print(mean_sample_data_intern_proactive)
    print(mean_sample_data_intern_reactive)
    print(mean_sample_data_junior_proactive)
    print(mean_sample_data_junior_reactive)
    print(mean_sample_data_senior_proactive)
    print(mean_sample_data_senior_reactive)

    print("---Novice Proactive vs Reactive---")
    print(sp.stats.kruskal(mean_sample_data_novice_proactive, mean_sample_data_novice_reactive))
    print("---Senior Proactive vs Reactive---")
    print(sp.stats.kruskal(mean_sample_data_senior_proactive, mean_sample_data_senior_reactive))

    

    # print("---Intern Proactive vs Reactive---")
    # print(sp.stats.kruskal(mean_sample_data_intern_proactive, mean_sample_data_intern_reactive))
    # print("---Junior Proactive vs Reactive---")
    # print(sp.stats.kruskal(mean_sample_data_junior_proactive, mean_sample_data_junior_reactive))
    # print("---Senior Proactive vs Reactive---")
    # print(sp.stats.kruskal(mean_sample_data_senior_proactive, mean_sample_data_senior_reactive))

    # print("---Intern Proactive vs Junior Proactive vs Senior Proactive---")
    # print(sp.stats.kruskal(mean_sample_data_intern_proactive, mean_sample_data_junior_proactive, mean_sample_data_senior_proactive))
    
    # print("---Intern Reactive vs Junior Reactive vs Senior Reactive---")
    # print(sp.stats.kruskal(mean_sample_data_intern_reactive, mean_sample_data_junior_reactive, mean_sample_data_senior_reactive))

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

            for k,y in enumerate(sample_data_intern_assertive_i):
                if(k % 2 == 1):
                    sample_data_intern_assertive_i[k] = 6 - y

            mean_sample_data_intern_assertive.append(np.mean(sample_data_intern_assertive_i))

        if(i+1 in non_assertive):

            nan_outliers_sample_data_intern_non_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_intern_non_assertive_i = nan_outliers_sample_data_intern_non_assertive_i[~np.isnan(nan_outliers_sample_data_intern_non_assertive_i)]
            sample_data_intern_non_assertive_i = outliers_sample_data_intern_non_assertive_i

            for k,y in enumerate(sample_data_intern_non_assertive_i):
                if(k % 2 == 1):
                    sample_data_intern_non_assertive_i[k] = 6 - y

            mean_sample_data_intern_non_assertive.append(np.mean(sample_data_intern_non_assertive_i))

    for i in getScenarios(juniors):

        if(i+1 in assertive):

            nan_outliers_sample_data_junior_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_assertive_i = nan_outliers_sample_data_junior_assertive_i[~np.isnan(nan_outliers_sample_data_junior_assertive_i)]
            sample_data_junior_assertive_i = outliers_sample_data_junior_assertive_i

            for k,y in enumerate(sample_data_junior_assertive_i):
                if(k % 2 == 1):
                    sample_data_junior_assertive_i[k] = 6 - y
        
            mean_sample_data_junior_assertive.append(np.mean(sample_data_junior_assertive_i))

        if(i+1 in non_assertive):

            nan_outliers_sample_data_junior_non_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_junior_non_assertive_i = nan_outliers_sample_data_junior_non_assertive_i[~np.isnan(nan_outliers_sample_data_junior_non_assertive_i)]
            sample_data_junior_non_assertive_i = outliers_sample_data_junior_non_assertive_i

            for k,y in enumerate(sample_data_junior_non_assertive_i):
                if(k % 2 == 1):
                    sample_data_junior_non_assertive_i[k] = 6 - y

            mean_sample_data_junior_non_assertive.append(np.mean(sample_data_junior_non_assertive_i))

    for i in getScenarios(seniors):

        if(i+1 in assertive):

            nan_outliers_sample_data_senior_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_assertive_i = nan_outliers_sample_data_senior_assertive_i[~np.isnan(nan_outliers_sample_data_senior_assertive_i)]
            sample_data_senior_assertive_i = outliers_sample_data_senior_assertive_i

            for k,y in enumerate(sample_data_senior_assertive_i):
                if(k % 2 == 1):
                    sample_data_senior_assertive_i[k] = 6 - y

            mean_sample_data_senior_assertive.append(np.mean(sample_data_senior_assertive_i))

        if(i+1 in non_assertive):

            nan_outliers_sample_data_senior_non_assertive_i = (np.float64(data[2:,firstIndex:lastIndex]))[i]
            outliers_sample_data_senior_non_assertive_i = nan_outliers_sample_data_senior_non_assertive_i[~np.isnan(nan_outliers_sample_data_senior_non_assertive_i)]
            sample_data_senior_non_assertive_i = outliers_sample_data_senior_non_assertive_i

            for k,y in enumerate(sample_data_senior_non_assertive_i):
                if(k % 2 == 1):
                    sample_data_senior_non_assertive_i[k] = 6 - y

            mean_sample_data_senior_non_assertive.append(np.mean(sample_data_senior_non_assertive_i))
    
    mean_sample_data_novice_assertive = np.append(mean_sample_data_intern_assertive, mean_sample_data_junior_assertive)
    mean_sample_data_novice_non_assertive = np.append(mean_sample_data_intern_non_assertive, mean_sample_data_junior_non_assertive)

    print(mean_sample_data_intern_assertive)
    print(mean_sample_data_intern_non_assertive)
    print(mean_sample_data_junior_assertive)
    print(mean_sample_data_junior_non_assertive)
    print(mean_sample_data_senior_assertive)
    print(mean_sample_data_senior_non_assertive)

    print("---Novice Assertive vs Non Assertive---")
    print(sp.stats.kruskal(mean_sample_data_novice_assertive, mean_sample_data_novice_non_assertive))
    print("---Senior Assertive vs Non Assertive---")
    print(sp.stats.kruskal(mean_sample_data_senior_assertive, mean_sample_data_senior_non_assertive))

    print("---Novice vs Senior---")
    print(sp.stats.kruskal(np.append(mean_sample_data_novice_assertive, mean_sample_data_novice_non_assertive), 
                            np.append(mean_sample_data_senior_assertive, mean_sample_data_senior_non_assertive)))

    # print("---Intern Assertive vs Junior Assertive vs Senior Assertive---")
    # print(sp.stats.kruskal(mean_sample_data_intern_assertive, mean_sample_data_junior_assertive, mean_sample_data_senior_assertive))
    
    # print("---Intern Non Assertive vs Junior Non Assertive vs Senior Non Assertive---")
    # print(sp.stats.kruskal(mean_sample_data_intern_non_assertive, mean_sample_data_junior_non_assertive))
    

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
    # print("-------------- ASSERTIVENESS ---------------")
    kruskalWallisAssertiveness(4,4)
    # print("-------------- BEHAVIOUR ---------------")
    kruskalWallisBehaviour(4,4)


    # print("-------------- UX ---------------")

    # print("-------------- ASSERTIVENESS ---------------")

    # #DOTS
    # print("-------------- DOTS ---------------")
    # kruskalWallisAssertiveness(5,5)
    # kruskalWallisAssertiveness(6,6)
    # kruskalWallisAssertiveness(7,7)
    # kruskalWallisAssertiveness(5,7)

    # #SUS
    # print("-------------- SUS ---------------")
    # kruskalWallisAssertiveness(8,8)
    # kruskalWallisAssertiveness(9,9)
    # kruskalWallisAssertiveness(10,10)
    # kruskalWallisAssertiveness(11,11)
    # kruskalWallisAssertiveness(12,12)
    # kruskalWallisAssertiveness(13,13)
    # kruskalWallisAssertiveness(14,14)
    # kruskalWallisAssertiveness(15,15)
    # kruskalWallisAssertiveness(16,16)
    # kruskalWallisAssertiveness(17,17)
    # kruskalWallisAssertiveness(8,17)

    # #NASA-TLX
    # print("-------------- NASA-TLX ---------------")
    # kruskalWallisAssertiveness(18,18)
    # kruskalWallisAssertiveness(19,19)
    # kruskalWallisAssertiveness(20,20)
    # kruskalWallisAssertiveness(21,21)
    # kruskalWallisAssertiveness(22,22)
    # kruskalWallisAssertiveness(23,23)
    # kruskalWallisAssertiveness(18,23)

    # print("-------------- BEHAVIOUR ---------------")
    # #DOTS
    # print("-------------- DOTS ---------------")
    # kruskalWallisBehaviour(5,5)
    # kruskalWallisBehaviour(6,6)
    # kruskalWallisBehaviour(7,7)
    # kruskalWallisBehaviour(5,7)

    # #SUS
    # print("-------------- SUS ---------------")
    # kruskalWallisBehaviour(8,8)
    # kruskalWallisBehaviour(9,9)
    # kruskalWallisBehaviour(10,10)
    # kruskalWallisBehaviour(11,11)
    # kruskalWallisBehaviour(12,12)
    # kruskalWallisBehaviour(13,13)
    # kruskalWallisBehaviour(14,14)
    # kruskalWallisBehaviour(15,15)
    # kruskalWallisBehaviour(16,16)
    # kruskalWallisBehaviour(17,17)
    # kruskalWallisBehaviour(8,17)

    # #NASA-TLX
    # print("-------------- NASA-TLX ---------------")
    # kruskalWallisBehaviour(18,18)
    # kruskalWallisBehaviour(19,19)
    # kruskalWallisBehaviour(20,20)
    # kruskalWallisBehaviour(21,21)
    # kruskalWallisBehaviour(22,22)
    # kruskalWallisBehaviour(23,23)
    # kruskalWallisBehaviour(18,23)
    

    # #Q3
    # print("-------------- PREFERENCE ---------------")

    # print("-------------- ASSERTIVENESS ---------------")
    # kruskalWallisPreference(24,26)

    # print("-------------- BEHAVIOUR ---------------")
    # kruskalWallisPreference(27,29)


    # #Q4
    # print("-------------- INFLUENCE ---------------")

    # kruskalWallisBehaviour(3,3)



if __name__ == "__main__":
    main()
