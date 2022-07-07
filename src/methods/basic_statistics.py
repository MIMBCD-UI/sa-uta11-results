
from cmath import nan
import enum
from glob import glob
from xml.etree.ElementTree import QName
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime as dt
from statsmodels.stats.contingency_tables import mcnemar
import pylab

import sys
# sys.path is a list of absolute path strings
sys.path.append('../constants')
sys.path.append('../methods')

from sheets import data, scenarios, getScenariosPatients
from groups import interns, juniors, seniors, assertive, non_assertive, proactive, reactive, groups_assertiveness, groups_behaviour, getScenarios
from outliers import reject_outliers, lower_bound, upper_bound
from birads import assistant_birads, real_birads

table_assertive = ""
table_non_assertive = ""
table_proactive = ""
table_reactive = ""
question = 1

def getAccuracy(array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    if(TP+FP+FN+TN == 0):
        return nan
    return (TP+TN)/(TP+FP+FN+TN)

def getPrecision(array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    if(TP + FP == 0):
        return nan
    return TP/(TP+FP)

def getRecall (array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    if(TP+FN == 0):
        return nan
    return TP/(TP+FN)

def getSpecificity(array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    if(TN+FP == 0):
        return nan
    return TN/(TN+FP)

def getF1Score(array):
    return 2*((getPrecision(array)*getRecall(array))/(getPrecision(array)+getRecall(array)))

def getPPV(array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    if(TP+FP == 0):
        return nan
    return TP/(TP+FP)

def getNPV(array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    if(TN+FN == 0):
        return nan
    return TN/(TN+FN)

def getLRplus(array):
    return getRecall(array) / (1-getSpecificity(array)) 

def getLRminus(array):
    if(getSpecificity(array) == 0):
        return nan
    return (1-getRecall(array)) / getSpecificity(array) 

def getDOR(array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    if(FN == 0 or TN == 0 or (FP/TN) == 0):
        return nan
    return (TP/FN)/(FP/TN)

def getYouden(array):
    return (getRecall(array) + getSpecificity(array) ) - 1

def contingency_table(array_1, array_2):
    TP1 = array_1[0]
    TN1 = array_1[1]
    FP1 = array_1[2]
    FN1 = array_1[3]
    TP2 = array_2[0]
    TN2 = array_2[1]
    FP2 = array_2[2]
    FN2 = array_2[3]
    return [[TP1 + TN1 + TP2 + TN2, TP1 + TN1 + FP2 + FN2],
            [FP1 + FN1 + TP2 + TN2, FP1 + FN1 + FP2 + FN2]]

def confusion_matrix(array):
    TP = array[0]
    TN = array[1]
    FP = array[2]
    FN = array[3]
    fig = px.imshow([[TP, FP],
                     [FN, TN]])
    fig.show()

def fpAndFnChart(data, groups):
    fig = go.Figure()
    fig.update_layout(
    font_family = "Helvetica",
    font_size=50
    )
    fig.add_trace(go.Histogram(histfunc="sum", y=data.loc[[2]].values[0], x=groups, name="False Positives"))
    fig.add_trace(go.Histogram(histfunc="sum", y=data.loc[[3]].values[0], x=groups, name="False Negatives"))
    fig.show()

def biradsPrediction(real_birads, clincian_birads):
    if(real_birads == 1):
        return 4
    # ------- 1,2,3,4,5 BI-RADS -------
    # if(real_birads > 1 and clincian_birads == real_birads and clincian_birads != 0):
    #     return 0 #True Positive
    # elif(real_birads <= 1 and clincian_birads == real_birads and clincian_birads != 0):
    #     return 1 #True Negative
    # elif(clincian_birads > real_birads and clincian_birads != 0):
    #     return 2 #False Positive
    # elif(clincian_birads < real_birads and clincian_birads != 0):
    #     return 3 #False Negative
        
    # ------- Low, Medium, High BI-RADS -------
    if(real_birads > 1 and (((real_birads == 2 or real_birads == 3) and real_birads == clincian_birads) 
    or ((real_birads == 4 or real_birads == 5) and real_birads == clincian_birads)) and clincian_birads != 0):
        return 0 #True Positive
    elif(real_birads <= 1 and clincian_birads == real_birads and clincian_birads != 0):
        return 1 #True Negative
    elif((real_birads == 1 and clincian_birads > 1) or
        (((real_birads == 2 or real_birads == 3) and clincian_birads > 3))  and clincian_birads != 0):
        return 2 #False Positive
    elif(((real_birads == 4 or real_birads == 5) and clincian_birads < 4) or
        (((real_birads == 2 or real_birads == 3) and clincian_birads < 2))  and clincian_birads != 0):
        return 3 #False Negative


    #------ Findings / No Findings ------
    # if(real_birads > 1 and clincian_birads > 1 and clincian_birads != 0):
    #     return 0 #True Positive
    # elif(real_birads <= 1 and clincian_birads <= 1 and clincian_birads != 0):
    #     return 1 #True Negative
    # elif(real_birads <= 1 and clincian_birads > 1 and clincian_birads != 0):
    #     return 2 #False Positive
    # elif(real_birads > 1 and clincian_birads <= 1 and clincian_birads != 0):
    #     return 3 #False Negative
    return 4

def performanceMetrics(sample_data, iteration, birads_level):
    intern = getScenarios(interns)
    junior = getScenarios(juniors)
    intern = np.append(intern,junior)
    senior = getScenarios(seniors)

    scenarios_patients = np.int32(getScenariosPatients())

    assertive_scenarios = np.subtract(proactive, 1)
    non_assertive_scenarios = np.subtract(reactive, 1)
    proactive_scenarios = np.subtract(proactive, 1)
    reactive_scenarios = np.subtract(reactive, 1)

    intern_assertive = [0,0,0,0,0]
    intern_non_assertive = [0,0,0,0,0]
    junior_assertive = [0,0,0,0,0]
    junior_non_assertive = [0,0,0,0,0]
    senior_assertive = [0,0,0,0,0]
    senior_non_assertive = [0,0,0,0,0]

    intern_proactive = [0,0,0,0,0]
    intern_reactive = [0,0,0,0,0]
    junior_proactive = [0,0,0,0,0]
    junior_reactive = [0,0,0,0,0]
    senior_proactive = [0,0,0,0,0]
    senior_reactive = [0,0,0,0,0]

    for j,b in enumerate(sample_data[birads_level::iteration]):
        i = j* iteration + birads_level
        real_birads_patient = real_birads[scenarios_patients[i]]
        predcited_birads_patient = int(b)
        if(i in intern and i in assertive_scenarios):
            intern_assertive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in intern and i in non_assertive_scenarios):
            intern_non_assertive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in junior and i in assertive_scenarios):
            junior_assertive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in junior and i in non_assertive_scenarios):
            junior_non_assertive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in senior and i in assertive_scenarios):
            senior_assertive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in senior and i in non_assertive_scenarios):
            senior_non_assertive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        if(i in intern and i in proactive_scenarios):
            intern_proactive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in intern and i in reactive_scenarios):
            intern_reactive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in junior and i in proactive_scenarios):
            junior_proactive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in junior and i in reactive_scenarios):
            junior_reactive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in senior and i in proactive_scenarios):
            senior_proactive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1
        elif (i in senior and i in reactive_scenarios):
            senior_reactive[biradsPrediction(real_birads_patient,predcited_birads_patient)] += 1



    if(iteration == 1):
        fpAndFnChart(pd.DataFrame(data={nums:l for l, nums in zip(np.vstack((intern_assertive, intern_non_assertive, 
        senior_assertive, senior_non_assertive)), 
        groups_assertiveness)}), groups_assertiveness)
        fpAndFnChart(pd.DataFrame(data={nums:l for l, nums in zip(np.vstack((intern_proactive, intern_reactive, 
        senior_proactive, senior_reactive)), 
        groups_behaviour)}), groups_behaviour)

        # confusion_matrix(intern_assertive)
        # confusion_matrix(intern_non_assertive)
        # confusion_matrix(junior_assertive)
        # confusion_matrix(junior_non_assertive)
        # confusion_matrix(senior_assertive)
        # confusion_matrix(senior_non_assertive)

        # confusion_matrix(intern_proactive)
        # confusion_matrix(intern_reactive)
        # confusion_matrix(junior_proactive)
        # confusion_matrix(junior_reactive)
        # confusion_matrix(senior_proactive)
        # confusion_matrix(senior_reactive)
        

    print("Accuracy: ", getAccuracy(intern_assertive), getAccuracy(intern_non_assertive),
                        getAccuracy(senior_assertive), getAccuracy(senior_non_assertive))
    print("Precision: ", getPrecision(intern_assertive), getPrecision(intern_non_assertive),
                        getPrecision(senior_assertive), getPrecision(senior_non_assertive))
    print("Sensitivity/Recall: ", getRecall(intern_assertive), getRecall(intern_non_assertive),
                        getRecall(senior_assertive), getRecall(senior_non_assertive))
    print("Specificity: ", getSpecificity(intern_assertive), getSpecificity(intern_non_assertive),
                        getSpecificity(senior_assertive), getSpecificity(senior_non_assertive))
    print("F1 Score: ", getF1Score(intern_assertive), getF1Score(intern_non_assertive),
                        getF1Score(senior_assertive), getF1Score(senior_non_assertive))
    print("Positive predictive value: ", getPPV(intern_assertive), getPPV(intern_non_assertive),
                        getPPV(senior_assertive), getPPV(senior_non_assertive))
    print("Negative predictive valu: ", getNPV(intern_assertive), getNPV(intern_non_assertive),
                        getNPV(senior_assertive), getNPV(senior_non_assertive))
    print("Likelihood+: ", getLRplus(intern_assertive), getLRplus(intern_non_assertive),
                        getLRplus(senior_assertive), getLRplus(senior_non_assertive))
    print("Likelihood-: ", getLRminus(intern_assertive), getLRminus(intern_non_assertive),
                        getLRminus(senior_assertive), getLRminus(senior_non_assertive))
    print("Diagnostic odds ratio: ", getDOR(intern_assertive), getDOR(intern_non_assertive),
                        getDOR(senior_assertive), getDOR(senior_non_assertive))
    print("Youden Index: ", getYouden(intern_assertive), getYouden(intern_non_assertive),
                        getYouden(senior_assertive), getYouden(senior_non_assertive))

    print(contingency_table(intern_assertive, intern_non_assertive))
    print(contingency_table(senior_assertive, senior_non_assertive))
    print(mcnemar(contingency_table(intern_assertive, intern_non_assertive), exact=True))
    print(mcnemar(contingency_table(senior_assertive, senior_non_assertive), exact=True))


    print("Accuracy: ", getAccuracy(intern_proactive), getAccuracy(intern_reactive),
                        getAccuracy(senior_proactive), getAccuracy(senior_reactive))
    print("Precision: ", getPrecision(intern_proactive), getPrecision(intern_reactive),
                        getPrecision(senior_proactive), getPrecision(senior_reactive))
    print("Sensitivity/Recall: ", getRecall(intern_proactive), getRecall(intern_reactive),
                        getRecall(senior_proactive), getRecall(senior_reactive))
    print("Specificity: ", getSpecificity(intern_proactive), getSpecificity(intern_reactive),
                        getSpecificity(senior_proactive), getSpecificity(senior_reactive))
    print("F1 Score: ", getF1Score(intern_proactive), getF1Score(intern_reactive),
                        getF1Score(senior_proactive), getF1Score(senior_reactive))
    print("Positive predictive value: ", getPPV(intern_proactive), getPPV(intern_reactive),
                        getPPV(senior_proactive), getPPV(senior_reactive))
    print("Negative predictive valu: ", getNPV(intern_proactive), getNPV(intern_reactive),
                        getNPV(senior_proactive), getNPV(senior_reactive))
    print("Likelihood+: ", getLRplus(intern_proactive), getLRplus(intern_reactive),
                        getLRplus(senior_proactive), getLRplus(senior_reactive))
    print("Likelihood-: ", getLRminus(intern_proactive), getLRminus(intern_reactive),
                        getLRminus(senior_proactive), getLRminus(senior_reactive))
    print("Diagnostic odds ratio: ", getDOR(intern_proactive), getDOR(intern_reactive),
                        getDOR(senior_proactive), getDOR(senior_reactive))
    print("Youden Index: ", getYouden(intern_proactive), getYouden(intern_reactive),
                        getYouden(senior_proactive), getYouden(senior_reactive))

    print(contingency_table(intern_proactive, intern_reactive))
    print(contingency_table(senior_proactive, senior_reactive))
    print(mcnemar(contingency_table(intern_proactive, intern_reactive), exact=True))
    print(mcnemar(contingency_table(senior_proactive, senior_reactive), exact=True))


def basicStatisticBirads(index):

    sample_data = np.float64(data[2:,index])

    # for i in range(3):
    #     performanceMetrics(sample_data, 3, i)

    # performanceMetrics(sample_data, 3, 1)
    performanceMetrics(sample_data, 1,0)
    

def binomialTest(sample_data, iteration, birads_level):
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

    intern_proactive_total = np.intersect1d(intern, proactive_scenarios).size
    intern_reactive_total = np.intersect1d(intern, reactive_scenarios).size
    junior_proactive_total = np.intersect1d(junior, proactive_scenarios).size
    junior_reactive_total = np.intersect1d(junior, reactive_scenarios).size
    senior_proactive_total = np.intersect1d(senior, proactive_scenarios).size
    senior_reactive_total = np.intersect1d(senior, reactive_scenarios).size

    for j,b in enumerate(sample_data[birads_level::iteration]):
        i = j* iteration + birads_level
        print(int(b), assistant_birads[scenarios_patients[i]], int(b) == assistant_birads[scenarios_patients[i]])
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

def basicStatisticInfluence(index):

    sample_data = np.float64(data[2:,index])

    for i in range(3):
        binomialTest(sample_data, 3, i)

    binomialTest(sample_data, 1,0)

def likertChart(top_labels, colors, x_data, y_data):

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        legendBool = False
        for xd, yd in zip(x_data, y_data):
            if legendBool:
                fig.add_trace(go.Bar(
                    x=[xd[i]], y=[yd],
                    orientation='h',
                    showlegend = False,
                    width = 0.4,
                    marker=dict(
                        color=colors[i],
                        line=dict(color='rgb(248, 248, 249)', width=1)
                    )
                ))
            else:
                fig.add_trace(go.Bar(
                    x=[xd[i]], y=[yd],
                    orientation='h',
                    name = top_labels[i],
                    showlegend = True,
                    width = 0.4,
                    marker=dict(
                        color=colors[i],
                        line=dict(color='rgb(248, 248, 249)', width=1)
                    )
                ))
                legendBool = True

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
        margin=dict(l=120, r=10, t=140, b=80),
        showlegend=True,
        legend=dict(
            orientation="h",
            font_size = 25,
            font_family = "Helvetica",
            traceorder = "reversed"
        )
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Helvetica', size=40,
                                        color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
    fig.update_layout(annotations=annotations)

    fig.show()

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


    if(firstIndex != lastIndex):
        for j in range(2):
            if(firstIndex == 24):
                top_labels = ['Totally Non Assertive', 'Much more Non Assertive than Assertive', 'Slightly more Non Assertive than Assertive', 'Neutral', 
                'Slightly more Assertive than Non Assertive','Much more Assertive than Non Assertive', 'Totally Assertive']

                y_data = ['Which level<br>of assertiveness<br>was more reliable?',
                    'Which level<br>of assertiveness<br>was more capable?',
                    'Which level<br>of assertiveness<br>did you prefer overall?']
            else:
                top_labels = ['Totally Reactive', 'Much more Reactive than Proactive', 'Slightly more Reactive than Proactive', 'Neutral', 
                'Slightly more Proactive than Reactive','Much more Proactive than Reactive', 'Totally Proactive']

                y_data = ['Which behaviour<br>was more reliable?',
                    'Which behaviour<br>was more capable?',
                    'Which behaviour<br>did you prefer overall?']

            colors = ['rgb(84,39,136)', 'rgb(153,142,195)',
                    'rgb(216,218,235)','rgb(223,223,223)','rgb(254,254,182)',
                    'rgb(241,163,64)','rgb(179,88,6)']

            
            x_data = []
            for i in range(firstIndex, lastIndex):
                data_tmp = np.float64(data[2:,i])
                data_tmp = data_tmp[~np.isnan(data_tmp)]
                if(j == 0):
                    novices = np.subtract(interns, 1)
                    novices = np.append(novices, np.subtract(juniors,1))
                    sample_data_tmp = np.take(data_tmp, novices)
                else:
                    sample_data_tmp = np.take(data_tmp, np.subtract(seniors, 1))
                x_data.append([np.count_nonzero(sample_data_tmp == a) for a in range(1,8)])


            

            x_data.reverse()
            y_data.reverse()

            likertChart(top_labels, colors, x_data, y_data)


def basicStatistic(firstIndex, lastIndex):

    lastIndex += 1
    sample_data = np.float64(data[2:,firstIndex:lastIndex])

    intern_assertive = np.intersect1d(getScenarios(interns), np.subtract(assertive, 1))
    intern_non_assertive = np.intersect1d(getScenarios(interns), np.subtract(non_assertive, 1))
    junior_assertive = np.intersect1d(getScenarios(juniors), np.subtract(assertive, 1))
    junior_non_assertive = np.intersect1d(getScenarios(juniors), np.subtract(non_assertive, 1))
    #Novice
    intern_assertive = np.append(intern_assertive, junior_assertive)
    intern_non_assertive = np.append(intern_non_assertive, junior_non_assertive)
    #-------
    senior_assertive = np.intersect1d(getScenarios(seniors), np.subtract(assertive, 1))
    senior_non_assertive = np.intersect1d(getScenarios(seniors), np.subtract(non_assertive, 1))

    intern_proactive = np.intersect1d(getScenarios(interns), np.subtract(proactive, 1))
    intern_reactive = np.intersect1d(getScenarios(interns), np.subtract(reactive, 1))
    junior_proactive = np.intersect1d(getScenarios(juniors), np.subtract(proactive, 1))
    junior_reactive = np.intersect1d(getScenarios(juniors), np.subtract(reactive, 1))
    #Novice
    intern_proactive = np.append(intern_proactive, junior_proactive)
    intern_reactive = np.append(intern_reactive, junior_reactive)
    #-------
    senior_proactive = np.intersect1d(getScenarios(seniors), np.subtract(proactive, 1))
    senior_reactive = np.intersect1d(getScenarios(seniors), np.subtract(reactive, 1))

    # #Mean
    print("--------- MEAN -------------")
    print("--------- Intern Assertive ------------")
    print(np.nanmean(np.take(sample_data,intern_assertive, axis=0)))
    print("--------- Intern Non Assertive ------------")
    print(np.nanmean(np.take(sample_data,intern_non_assertive, axis=0)))
    print("--------- Intern Proactive ------------")
    print(np.nanmean(np.take(sample_data,intern_proactive, axis=0)))
    print("--------- Intern Reactive ------------")
    print(np.nanmean(np.take(sample_data,intern_reactive, axis=0)))

    print("--------- Junior Assertive ------------")
    print(np.mean(np.take(sample_data,junior_assertive, axis=0)))
    print("--------- Junior Non Assertive ------------")
    print(np.mean(np.take(sample_data,junior_non_assertive, axis=0)))
    print("--------- Junior Proactive ------------")
    print(np.mean(np.take(sample_data,junior_proactive, axis=0)))
    print("--------- Junior Reactive ------------")
    print(np.mean(np.take(sample_data,junior_reactive, axis=0)))

    print("--------- Senior Assertive ------------")
    print(np.mean(np.take(sample_data,senior_assertive, axis=0)))
    print("--------- Senior Non Assertive ------------")
    print(np.mean(np.take(sample_data,senior_non_assertive, axis=0)))
    print("--------- Senior Proactive ------------")
    print(np.mean(np.take(sample_data,senior_proactive, axis=0)))
    print("--------- Senior Reactive ------------")
    print(np.mean(np.take(sample_data,senior_reactive, axis=0)))


    #Standard Deviation
    print("--------- STANDARD DEVIATION -------------")
    print("--------- Intern Assertive ------------")
    print(np.nanstd(np.take(sample_data,intern_assertive, axis=0)))
    print("--------- Intern Non Assertive ------------")
    print(np.nanstd(np.take(sample_data,intern_non_assertive, axis=0)))
    print("--------- Intern Proactive ------------")
    print(np.nanstd(np.take(sample_data,intern_proactive, axis=0)))
    print("--------- Intern Reactive ------------")
    print(np.nanstd(np.take(sample_data,intern_reactive, axis=0)))

    print("--------- Junior Assertive ------------")
    print(np.std(np.take(sample_data,junior_assertive, axis=0)))
    print("--------- Junior Non Assertive ------------")
    print(np.std(np.take(sample_data,junior_non_assertive, axis=0)))
    print("--------- Junior Proactive ------------")
    print(np.std(np.take(sample_data,junior_proactive, axis=0)))
    print("--------- Junior Reactive ------------")
    print(np.std(np.take(sample_data,junior_reactive, axis=0)))

    print("--------- Senior Assertive ------------")
    print(np.std(np.take(sample_data,senior_assertive, axis=0)))
    print("--------- Senior Non Assertive ------------")
    print(np.std(np.take(sample_data,senior_non_assertive, axis=0)))
    print("--------- Senior Proactive ------------")
    print(np.std(np.take(sample_data,senior_proactive, axis=0)))
    print("--------- Senior Reactive ------------")
    print(np.std(np.take(sample_data,senior_reactive, axis=0)))

    # #Interval
    # print("--------- INTERVAL -------------")
    # print("--------- Intern Assertive ------------")
    # print("(" + str(np.amin(np.take(sample_data,intern_assertive, axis=0))) + "." + str(np.amax(np.take(sample_data,intern_assertive, axis=0))) + ")")
    # print("--------- Intern Non Assertive ------------")
    # print("(" + str(np.amin(np.take(sample_data,intern_non_assertive, axis=0))) + "." + str(np.amax(np.take(sample_data,intern_non_assertive, axis=0))) + ")")
    # print("--------- Intern Proactive ------------")
    # print("(" + str(np.amin(np.take(sample_data,intern_proactive, axis=0))) + "." + str(np.amax(np.take(sample_data,intern_proactive, axis=0))) + ")")
    # print("--------- Intern Reactive ------------")
    # print("(" + str(np.amin(np.take(sample_data,intern_reactive, axis=0))) + "." + str(np.amax(np.take(sample_data,intern_reactive, axis=0))) + ")")

    # print("--------- Junior Assertive ------------")
    # print("(" + str(np.amin(np.take(sample_data,junior_assertive, axis=0))) + "." + str(np.amax(np.take(sample_data,junior_assertive, axis=0))) + ")")
    # print("--------- Junior Non Assertive ------------")
    # print("(" + str(np.amin(np.take(sample_data,junior_non_assertive, axis=0))) + "." + str(np.amax(np.take(sample_data,junior_non_assertive, axis=0))) + ")")
    # print("--------- Junior Proactive ------------")
    # print("(" + str(np.amin(np.take(sample_data,junior_proactive, axis=0))) + "." + str(np.amax(np.take(sample_data,junior_proactive, axis=0))) + ")")
    # print("--------- Junior Reactive ------------")
    # print("(" + str(np.amin(np.take(sample_data,junior_reactive, axis=0))) + "." + str(np.amax(np.take(sample_data,junior_reactive, axis=0))) + ")")

    # print("--------- Senior Assertive ------------")
    # print("(" + str(np.amin(np.take(sample_data,senior_assertive, axis=0))) + "." + str(np.amax(np.take(sample_data,senior_assertive, axis=0))) + ")")
    # print("--------- Senior Non Assertive ------------")
    # print("(" + str(np.amin(np.take(sample_data,senior_non_assertive, axis=0))) + "." + str(np.amax(np.take(sample_data,senior_non_assertive, axis=0))) + ")")
    # print("--------- Senior Proactive ------------")
    # print("(" + str(np.amin(np.take(sample_data,senior_proactive, axis=0))) + "." + str(np.amax(np.take(sample_data,senior_proactive, axis=0))) + ")")
    # print("--------- Senior Reactive ------------")
    # print("(" + str(np.amin(np.take(sample_data,senior_reactive, axis=0))) + "." + str(np.amax(np.take(sample_data,senior_reactive, axis=0))) + ")")

    # #Lower Bound
    # print("--------- LOWER BOUND -------------")
    # print("--------- Intern Assertive ------------")
    # print(lower_bound(np.take(sample_data,intern_assertive, axis=0)))
    # print("--------- Intern Non Assertive ------------")
    # print(lower_bound(np.take(sample_data,intern_non_assertive, axis=0)))
    # print("--------- Intern Proactive ------------")
    # print(lower_bound(np.take(sample_data,intern_proactive, axis=0)))
    # print("--------- Intern Reactive ------------")
    # print(lower_bound(np.take(sample_data,intern_reactive, axis=0)))

    # print("--------- Junior Assertive ------------")
    # print(lower_bound(np.take(sample_data,junior_assertive, axis=0)))
    # print("--------- Junior Non Assertive ------------")
    # print(lower_bound(np.take(sample_data,junior_non_assertive, axis=0)))
    # print("--------- Junior Proactive ------------")
    # print(lower_bound(np.take(sample_data,junior_proactive, axis=0)))
    # print("--------- Junior Reactive ------------")
    # print(lower_bound(np.take(sample_data,junior_reactive, axis=0)))

    # print("--------- Senior Assertive ------------")
    # print(lower_bound(np.take(sample_data,senior_assertive, axis=0)))
    # print("--------- Senior Non Assertive ------------")
    # print(lower_bound(np.take(sample_data,senior_non_assertive, axis=0)))
    # print("--------- Senior Proactive ------------")
    # print(lower_bound(np.take(sample_data,senior_proactive, axis=0)))
    # print("--------- Senior Reactive ------------")
    # print(lower_bound(np.take(sample_data,senior_reactive, axis=0)))

    # #Upper Bound
    # print("--------- UPPER BOUND -------------")
    # print("--------- Intern Assertive ------------")
    # print(upper_bound(np.take(sample_data,intern_assertive, axis=0)))
    # print("--------- Intern Non Assertive ------------")
    # print(upper_bound(np.take(sample_data,intern_non_assertive, axis=0)))
    # print("--------- Intern Proactive ------------")
    # print(upper_bound(np.take(sample_data,intern_proactive, axis=0)))
    # print("--------- Intern Reactive ------------")
    # print(upper_bound(np.take(sample_data,intern_reactive, axis=0)))

    # print("--------- Junior Assertive ------------")
    # print(upper_bound(np.take(sample_data,junior_assertive, axis=0)))
    # print("--------- Junior Non Assertive ------------")
    # print(upper_bound(np.take(sample_data,junior_non_assertive, axis=0)))
    # print("--------- Junior Proactive ------------")
    # print(upper_bound(np.take(sample_data,junior_proactive, axis=0)))
    # print("--------- Junior Reactive ------------")
    # print(upper_bound(np.take(sample_data,junior_reactive, axis=0)))

    # print("--------- Senior Assertive ------------")
    # print(upper_bound(np.take(sample_data,senior_assertive, axis=0)))
    # print("--------- Senior Non Assertive ------------")
    # print(upper_bound(np.take(sample_data,senior_non_assertive, axis=0)))
    # print("--------- Senior Proactive ------------")
    # print(upper_bound(np.take(sample_data,senior_proactive, axis=0)))
    # print("--------- Senior Reactive ------------")
    # print(upper_bound(np.take(sample_data,senior_reactive, axis=0)))

    # global table_proactive, table_assertive, table_non_assertive, table_reactive, question

    # table_assertive += "\n\\hline\n\\textbf{Total} & %.2f & %.2f & %.2f & %.2f \\\\" % ( np.nanmean(np.take(sample_data,intern_assertive, axis=0)), 
    # np.nanstd(np.take(sample_data,intern_assertive, axis=0)), np.nanmean(np.take(sample_data,senior_assertive, axis=0)),
    # np.nanstd(np.take(sample_data,senior_assertive, axis=0)))

    # table_non_assertive += "\n\\hline\n\\textbf{Total} & %.2f & %.2f & %.2f & %.2f \\\\" % ( np.nanmean(np.take(sample_data,intern_non_assertive, axis=0)), 
    # np.nanstd(np.take(sample_data,intern_non_assertive, axis=0)), np.nanmean(np.take(sample_data,senior_non_assertive, axis=0)),
    # np.nanstd(np.take(sample_data,senior_non_assertive, axis=0)))

    # table_proactive += "\n\\hline\n\\textbf{Total} & %.2f & %.2f & %.2f & %.2f \\\\" % ( np.nanmean(np.take(sample_data,intern_proactive, axis=0)), 
    # np.nanstd(np.take(sample_data,intern_proactive, axis=0)), np.nanmean(np.take(sample_data,senior_proactive, axis=0)),
    # np.nanstd(np.take(sample_data,senior_proactive, axis=0)))

    # table_reactive += "\n\\hline\n\\textbf{Total} & %.2f & %.2f & %.2f & %.2f \\\\" % ( np.nanmean(np.take(sample_data,intern_reactive, axis=0)), 
    # np.nanstd(np.take(sample_data,intern_reactive, axis=0)), np.nanmean(np.take(sample_data,senior_reactive, axis=0)),
    # np.nanstd(np.take(sample_data,senior_reactive, axis=0)))

    # question += 1

def main():

    #BIRADS
    # print("-------------- BIRADS ---------------")
    basicStatisticBirads(3)

    # # Time
    # print("-------------- TIME ---------------")
    # basicStatistic(4,4)


    # print("-------------- UX ---------------")

    # #DOTS
    # print("-------------- DOTS ---------------")
    # basicStatistic(5,5)
    # basicStatistic(6,6)
    # basicStatistic(7,7)
    # basicStatistic(5,7)

    #SUS
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

    # print(table_assertive)
    # print(table_non_assertive)
    # print(table_proactive)
    # print(table_reactive)

    # # #NASA-TLX
    # print("-------------- NASA-TLX ---------------")
    # basicStatistic(18,18)
    # basicStatistic(19,19)
    # basicStatistic(20,20)
    # basicStatistic(21,21)
    # basicStatistic(22,22)
    # basicStatistic(23,23)
    # basicStatistic(18,23)

    
    #Q3
    # print("-------------- PREFERENCE ---------------")

    # print("-------------- Assertiveness ---------------")
    # basicStatisticPreference(24,24)
    # basicStatisticPreference(25,25)
    # basicStatisticPreference(26,26)
    # basicStatisticPreference(24,26)

    # print("-------------- Behaviour ---------------")
    # basicStatisticPreference(27,27)
    # basicStatisticPreference(28,28)
    # basicStatisticPreference(29,29)
    # basicStatisticPreference(27,29)



    # #Q4
    # print("-------------- INFLUENCE ---------------")

    # basicStatisticInfluence(3)


if __name__ == "__main__":
    main()
