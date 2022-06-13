
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
from outliers import reject_outliers, lower_bound, upper_bound


def basicStatisticPreference(firstIndex, lastIndex):

    lastIndex += 1
    sample_data = np.float64(data[2:,firstIndex:lastIndex])
    sample_data = sample_data[~np.isnan(sample_data)]

    intern = np.subtract(interns, 1)
    junior = np.subtract(juniors, 1)
    senior = np.subtract(seniors, 1)

    #Mean
    print("--------- MEAN -------------")
    print("--------- Intern Assertiveveness ------------")
    print(np.mean(np.take(sample_data,intern)))

    print("--------- Junior Assertiveveness ------------")
    print(np.mean(np.take(sample_data,junior)))

    print("--------- Senior Assertiveveness ------------")
    print(np.mean(np.take(sample_data,senior)))


    #Standard Deviation
    print("--------- STANDARD DEVIATION -------------")
    print("--------- Intern Assertiveveness ------------")
    print(np.std(np.take(sample_data,intern)))

    print("--------- Junior Assertiveveness ------------")
    print(np.std(np.take(sample_data,junior)))

    print("--------- Senior Assertiveveness ------------")
    print(np.std(np.take(sample_data,senior)))

    #Interval
    print("--------- INTERVAL -------------")
    print("--------- Intern Assertiveveness ------------")
    print("(" + str(np.amin(np.take(sample_data,intern))) + "." + str(np.amax(np.take(sample_data,intern))) + ")")

    print("--------- Junior Assertiveveness ------------")
    print("(" + str(np.amin(np.take(sample_data,junior))) + "." + str(np.amax(np.take(sample_data,junior))) + ")")

    print("--------- Senior Assertiveveness ------------")
    print("(" + str(np.amin(np.take(sample_data,senior))) + "." + str(np.amax(np.take(sample_data,senior))) + ")")

    #Lower Bound
    print("--------- LOWER BOUND -------------")
    print("--------- Intern Assertiveveness ------------")
    print(lower_bound(np.take(sample_data,intern)))

    print("--------- Junior Assertiveveness ------------")
    print(lower_bound(np.take(sample_data,junior)))
    print("--------- Senior Assertiveveness ------------")
    print(lower_bound(np.take(sample_data,senior)))

    #Upper Bound
    print("--------- UPPER BOUND -------------")
    print("--------- Intern Assertiveveness ------------")
    print(upper_bound(np.take(sample_data,intern)))

    print("--------- Junior Assertiveveness ------------")
    print(upper_bound(np.take(sample_data,junior)))

    print("--------- Senior Assertiveveness ------------")
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
    # print("-------------- DOTS ---------------")
    # basicStatistic(5,5)
    # basicStatistic(6,6)
    # basicStatistic(7,7)

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

    # #NASA-TLX
    # print("-------------- NASA-TLX ---------------")
    # basicStatistic(18,18)
    # basicStatistic(19,19)
    # basicStatistic(20,20)
    # basicStatistic(21,21)
    # basicStatistic(22,22)
    # basicStatistic(23,23)

    
    #Q3
    print("-------------- PREFERENCE ---------------")

    # print("-------------- Assertiveness ---------------")
    # basicStatisticPreference(24,24)
    # basicStatisticPreference(25,25)
    # basicStatisticPreference(26,26)

    print("-------------- Behaviour ---------------")
    basicStatisticPreference(27,27)
    basicStatisticPreference(28,28)
    basicStatisticPreference(29,29)

    # #Q4
    # print("-------------- INFLUENCE ---------------")

    # # basicStatisticBehaviour(3,3)


if __name__ == "__main__":
    main()
