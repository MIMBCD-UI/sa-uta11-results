
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

from sheets import data, scenarios, getScenariosPatients
from groups import interns, juniors, seniors, assertive, non_assertive, proactive, reactive, getScenarios
from outliers import reject_outliers, lower_bound, upper_bound
from birads import assistant_birads, real_birads

def  binomialTest(sample_data, iteration, birads_level):
    intern = getScenarios(interns)
    junior = getScenarios(juniors)
    senior = getScenarios(seniors)

    scenarios_patients = np.int32(getScenariosPatients())

    proactive_scenarios = np.subtract(proactive, 1)
    reactive_scenarios = np.subtract(reactive, 1)

    intern_proactive = 0
    intern_reactive = 0
    junior_proactive = 0
    junior_reactive = 0
    senior_proactive = 0
    senior_reactive = 0

    intern_proactive_total = 0
    intern_reactive_total = 0
    junior_proactive_total = 0
    junior_reactive_total = 0
    senior_proactive_total = 0
    senior_reactive_total = 0

    for j,b in enumerate(sample_data[birads_level::iteration]):
        i = j* iteration + birads_level
        print(int(b), assistant_birads[scenarios_patients[i]], int(b) == assistant_birads[scenarios_patients[i]])
        if(i in intern and i in proactive_scenarios):
            intern_proactive_total += 1
        elif (i in intern and i in reactive_scenarios):
            intern_reactive_total += 1
        elif (i in junior and i in proactive_scenarios):
            junior_proactive_total += 1
        elif (i in junior and i in reactive_scenarios):
            junior_reactive_total += 1
        elif (i in senior and i in proactive_scenarios):
            senior_proactive_total += 1
        elif (i in senior and i in reactive_scenarios):
            senior_reactive_total += 1
        if(int(b) == assistant_birads[scenarios_patients[i]]):
            if(i in intern and i in proactive_scenarios):
                intern_proactive += 1
            elif (i in intern and i in reactive_scenarios):
                intern_reactive += 1
            elif (i in junior and i in proactive_scenarios):
                junior_proactive += 1
            elif (i in junior and i in reactive_scenarios):
                junior_reactive += 1
            elif (i in senior and i in proactive_scenarios):
                senior_proactive += 1
            elif (i in senior and i in reactive_scenarios):
                senior_reactive += 1

    print(sp.stats.binomtest(intern_proactive, intern_proactive_total, 1/5), sp.stats.binomtest(intern_reactive, intern_reactive_total, 1/5))
    print(sp.stats.binomtest(junior_proactive, junior_proactive_total, 1/5), sp.stats.binomtest(junior_reactive, junior_reactive_total, 1/5))
    print(sp.stats.binomtest(senior_proactive, senior_proactive_total, 1/5), sp.stats.binomtest(senior_reactive, senior_reactive_total, 1/5))

def basicStatisticInfluence(index, birads):

    if birads == 1:
        birads = real_birads
    else:
        birads = assistant_birads

    sample_data = np.float64(data[2:,index])

    for i in range(3):
        binomialTest(sample_data, 3, i)

    binomialTest(sample_data, 1,0)

def basicStatisticPreference(firstIndex, lastIndex):

    lastIndex += 1
    interval = lastIndex - firstIndex
    sample_data = np.float64(data[2:,firstIndex:lastIndex])
    sample_data = sample_data[~np.isnan(sample_data)]

    if(interval == 1):
        intern = np.subtract(interns, 1)
        junior = np.subtract(juniors, 1)
        senior = np.subtract(seniors, 1)
    else:
        intern = getScenarios(interns)
        junior = getScenarios(juniors)
        senior = getScenarios(seniors)

    #Mean
    print("--------- MEAN -------------")
    print("--------- Intern ------------")
    print(np.mean(np.take(sample_data,intern)))

    print("--------- Junior ------------")
    print(np.mean(np.take(sample_data,junior)))

    print("--------- Senior ------------")
    print(np.mean(np.take(sample_data,senior)))


    #Standard Deviation
    print("--------- STANDARD DEVIATION -------------")
    print("--------- Intern ------------")
    print(np.std(np.take(sample_data,intern)))

    print("--------- Junior ------------")
    print(np.std(np.take(sample_data,junior)))

    print("--------- Senior ------------")
    print(np.std(np.take(sample_data,senior)))

    #Interval
    print("--------- INTERVAL -------------")
    print("--------- Intern ------------")
    print("(" + str(np.amin(np.take(sample_data,intern))) + "." + str(np.amax(np.take(sample_data,intern))) + ")")

    print("--------- Junior ------------")
    print("(" + str(np.amin(np.take(sample_data,junior))) + "." + str(np.amax(np.take(sample_data,junior))) + ")")

    print("--------- Senior ------------")
    print("(" + str(np.amin(np.take(sample_data,senior))) + "." + str(np.amax(np.take(sample_data,senior))) + ")")

    #Lower Bound
    print("--------- LOWER BOUND -------------")
    print("--------- Intern ------------")
    print(lower_bound(np.take(sample_data,intern)))

    print("--------- Junior ------------")
    print(lower_bound(np.take(sample_data,junior)))
    print("--------- Senior ------------")
    print(lower_bound(np.take(sample_data,senior)))

    #Upper Bound
    print("--------- UPPER BOUND -------------")
    print("--------- Intern ------------")
    print(upper_bound(np.take(sample_data,intern)))

    print("--------- Junior ------------")
    print(upper_bound(np.take(sample_data,junior)))

    print("--------- Senior ------------")
    print(upper_bound(np.take(sample_data,senior)))


def basicStatistic(firstIndex, lastIndex):

    lastIndex += 1
    sample_data = np.float64(data[2:,firstIndex:lastIndex])

    intern_assertive = np.intersect1d(getScenarios(interns), np.subtract(assertive, 1))
    intern_non_assertive = np.intersect1d(getScenarios(interns), np.subtract(non_assertive, 1))
    junior_assertive = np.intersect1d(getScenarios(juniors), np.subtract(assertive, 1))
    junior_non_assertive = np.intersect1d(getScenarios(juniors), np.subtract(non_assertive, 1))
    senior_assertive = np.intersect1d(getScenarios(seniors), np.subtract(assertive, 1))
    senior_non_assertive = np.intersect1d(getScenarios(seniors), np.subtract(non_assertive, 1))

    intern_proactive = np.intersect1d(getScenarios(interns), np.subtract(proactive, 1))
    intern_reactive = np.intersect1d(getScenarios(interns), np.subtract(reactive, 1))
    junior_proactive = np.intersect1d(getScenarios(juniors), np.subtract(proactive, 1))
    junior_reactive = np.intersect1d(getScenarios(juniors), np.subtract(reactive, 1))
    senior_proactive = np.intersect1d(getScenarios(seniors), np.subtract(proactive, 1))
    senior_reactive = np.intersect1d(getScenarios(seniors), np.subtract(reactive, 1))


    #Mean
    print("--------- MEAN -------------")
    print("--------- Intern Assertive ------------")
    print(np.mean(np.take(sample_data,intern_assertive)))
    print("--------- Intern Non Assertive ------------")
    print(np.mean(np.take(sample_data,intern_non_assertive)))
    print("--------- Intern Proactive ------------")
    print(np.mean(np.take(sample_data,intern_proactive)))
    print("--------- Intern Reactive ------------")
    print(np.mean(np.take(sample_data,intern_reactive)))

    print("--------- Junior Assertive ------------")
    print(np.mean(np.take(sample_data,junior_assertive)))
    print("--------- Junior Non Assertive ------------")
    print(np.mean(np.take(sample_data,junior_non_assertive)))
    print("--------- Junior Proactive ------------")
    print(np.mean(np.take(sample_data,junior_proactive)))
    print("--------- Junior Reactive ------------")
    print(np.mean(np.take(sample_data,junior_reactive)))

    print("--------- Senior Assertive ------------")
    print(np.mean(np.take(sample_data,senior_assertive)))
    print("--------- Senior Non Assertive ------------")
    print(np.mean(np.take(sample_data,senior_non_assertive)))
    print("--------- Senior Proactive ------------")
    print(np.mean(np.take(sample_data,senior_proactive)))
    print("--------- Senior Reactive ------------")
    print(np.mean(np.take(sample_data,senior_reactive)))


    #Standard Deviation
    print("--------- STANDARD DEVIATION -------------")
    print("--------- Intern Assertive ------------")
    print(np.std(np.take(sample_data,intern_assertive)))
    print("--------- Intern Non Assertive ------------")
    print(np.std(np.take(sample_data,intern_non_assertive)))
    print("--------- Intern Proactive ------------")
    print(np.std(np.take(sample_data,intern_proactive)))
    print("--------- Intern Reactive ------------")
    print(np.std(np.take(sample_data,intern_reactive)))

    print("--------- Junior Assertive ------------")
    print(np.std(np.take(sample_data,junior_assertive)))
    print("--------- Junior Non Assertive ------------")
    print(np.std(np.take(sample_data,junior_non_assertive)))
    print("--------- Junior Proactive ------------")
    print(np.std(np.take(sample_data,junior_proactive)))
    print("--------- Junior Reactive ------------")
    print(np.std(np.take(sample_data,junior_reactive)))

    print("--------- Senior Assertive ------------")
    print(np.std(np.take(sample_data,senior_assertive)))
    print("--------- Senior Non Assertive ------------")
    print(np.std(np.take(sample_data,senior_non_assertive)))
    print("--------- Senior Proactive ------------")
    print(np.std(np.take(sample_data,senior_proactive)))
    print("--------- Senior Reactive ------------")
    print(np.std(np.take(sample_data,senior_reactive)))

    #Interval
    print("--------- INTERVAL -------------")
    print("--------- Intern Assertive ------------")
    print("(" + str(np.amin(np.take(sample_data,intern_assertive))) + "." + str(np.amax(np.take(sample_data,intern_assertive))) + ")")
    print("--------- Intern Non Assertive ------------")
    print("(" + str(np.amin(np.take(sample_data,intern_non_assertive))) + "." + str(np.amax(np.take(sample_data,intern_non_assertive))) + ")")
    print("--------- Intern Proactive ------------")
    print("(" + str(np.amin(np.take(sample_data,intern_proactive))) + "." + str(np.amax(np.take(sample_data,intern_proactive))) + ")")
    print("--------- Intern Reactive ------------")
    print("(" + str(np.amin(np.take(sample_data,intern_reactive))) + "." + str(np.amax(np.take(sample_data,intern_reactive))) + ")")

    print("--------- Junior Assertive ------------")
    print("(" + str(np.amin(np.take(sample_data,junior_assertive))) + "." + str(np.amax(np.take(sample_data,junior_assertive))) + ")")
    print("--------- Junior Non Assertive ------------")
    print("(" + str(np.amin(np.take(sample_data,junior_non_assertive))) + "." + str(np.amax(np.take(sample_data,junior_non_assertive))) + ")")
    print("--------- Junior Proactive ------------")
    print("(" + str(np.amin(np.take(sample_data,junior_proactive))) + "." + str(np.amax(np.take(sample_data,junior_proactive))) + ")")
    print("--------- Junior Reactive ------------")
    print("(" + str(np.amin(np.take(sample_data,junior_reactive))) + "." + str(np.amax(np.take(sample_data,junior_reactive))) + ")")

    print("--------- Senior Assertive ------------")
    print("(" + str(np.amin(np.take(sample_data,senior_assertive))) + "." + str(np.amax(np.take(sample_data,senior_assertive))) + ")")
    print("--------- Senior Non Assertive ------------")
    print("(" + str(np.amin(np.take(sample_data,senior_non_assertive))) + "." + str(np.amax(np.take(sample_data,senior_non_assertive))) + ")")
    print("--------- Senior Proactive ------------")
    print("(" + str(np.amin(np.take(sample_data,senior_proactive))) + "." + str(np.amax(np.take(sample_data,senior_proactive))) + ")")
    print("--------- Senior Reactive ------------")
    print("(" + str(np.amin(np.take(sample_data,senior_reactive))) + "." + str(np.amax(np.take(sample_data,senior_reactive))) + ")")

    #Lower Bound
    print("--------- LOWER BOUND -------------")
    print("--------- Intern Assertive ------------")
    print(lower_bound(np.take(sample_data,intern_assertive)))
    print("--------- Intern Non Assertive ------------")
    print(lower_bound(np.take(sample_data,intern_non_assertive)))
    print("--------- Intern Proactive ------------")
    print(lower_bound(np.take(sample_data,intern_proactive)))
    print("--------- Intern Reactive ------------")
    print(lower_bound(np.take(sample_data,intern_reactive)))

    print("--------- Junior Assertive ------------")
    print(lower_bound(np.take(sample_data,junior_assertive)))
    print("--------- Junior Non Assertive ------------")
    print(lower_bound(np.take(sample_data,junior_non_assertive)))
    print("--------- Junior Proactive ------------")
    print(lower_bound(np.take(sample_data,junior_proactive)))
    print("--------- Junior Reactive ------------")
    print(lower_bound(np.take(sample_data,junior_reactive)))

    print("--------- Senior Assertive ------------")
    print(lower_bound(np.take(sample_data,senior_assertive)))
    print("--------- Senior Non Assertive ------------")
    print(lower_bound(np.take(sample_data,senior_non_assertive)))
    print("--------- Senior Proactive ------------")
    print(lower_bound(np.take(sample_data,senior_proactive)))
    print("--------- Senior Reactive ------------")
    print(lower_bound(np.take(sample_data,senior_reactive)))

    #Upper Bound
    print("--------- UPPER BOUND -------------")
    print("--------- Intern Assertive ------------")
    print(upper_bound(np.take(sample_data,intern_assertive)))
    print("--------- Intern Non Assertive ------------")
    print(upper_bound(np.take(sample_data,intern_non_assertive)))
    print("--------- Intern Proactive ------------")
    print(upper_bound(np.take(sample_data,intern_proactive)))
    print("--------- Intern Reactive ------------")
    print(upper_bound(np.take(sample_data,intern_reactive)))

    print("--------- Junior Assertive ------------")
    print(upper_bound(np.take(sample_data,junior_assertive)))
    print("--------- Junior Non Assertive ------------")
    print(upper_bound(np.take(sample_data,junior_non_assertive)))
    print("--------- Junior Proactive ------------")
    print(upper_bound(np.take(sample_data,junior_proactive)))
    print("--------- Junior Reactive ------------")
    print(upper_bound(np.take(sample_data,junior_reactive)))

    print("--------- Senior Assertive ------------")
    print(upper_bound(np.take(sample_data,senior_assertive)))
    print("--------- Senior Non Assertive ------------")
    print(upper_bound(np.take(sample_data,senior_non_assertive)))
    print("--------- Senior Proactive ------------")
    print(upper_bound(np.take(sample_data,senior_proactive)))
    print("--------- Senior Reactive ------------")
    print(upper_bound(np.take(sample_data,senior_reactive)))



def main():

    # #BIRADS
    # print("-------------- BIRADS ---------------")
    # basicStatistic(3)

    # #Time
    # print("-------------- TIME ---------------")
    # basicStatistic(4,4)


    # print("-------------- UX ---------------")

    # #DOTS
    print("-------------- DOTS ---------------")
    # basicStatistic(5,5)
    # basicStatistic(6,6)
    # basicStatistic(7,7)
    basicStatistic(5,7)

    # #SUS
    # print("-------------- SUS ---------------")
    # basicStatistic(8,8)
    # basicStatistic(9,9)
    # basicStatistic(10,10)
    # basicStatistic(11,11)
    # basicStatistic(12,12)
    # basicStatistic(13,13)
    # basicStatistic(14,14)
    # basicStatistic(15,15)
    # basicStatistic(16,16)
    # basicStatistic(17,17)
    # basicStatistic(8,17)

    # #NASA-TLX
    print("-------------- NASA-TLX ---------------")
    # basicStatistic(18,18)
    # basicStatistic(19,19)
    # basicStatistic(20,20)
    # basicStatistic(21,21)
    # basicStatistic(22,22)
    # basicStatistic(23,23)
    basicStatistic(18,23)

    
    # #Q3
    print("-------------- PREFERENCE ---------------")

    print("-------------- Assertiveness ---------------")
    # basicStatisticPreference(24,24)
    # basicStatisticPreference(25,25)
    # basicStatisticPreference(26,26)
    basicStatisticPreference(24,26)

    print("-------------- Behaviour ---------------")
    # basicStatisticPreference(27,27)
    # basicStatisticPreference(28,28)
    # basicStatisticPreference(29,29)
    basicStatisticPreference(27,29)

    # #Q4
    # print("-------------- INFLUENCE ---------------")

    # basicStatisticInfluence(3,2)


if __name__ == "__main__":
    main()
