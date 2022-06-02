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
from groups import interns, juniors, seniors, getScenarios
from outliers import reject_outliers

def my_histogram(data):
    fig = px.histogram(data)
    fig.show()

def qq_plot(data):
    
    sm.qqplot(data)
    pylab.show()

def isSameDistribution(index):
    sample_data_intern = np.float64(np.take(data[2:,index], getScenarios(interns)))
    sample_data_junior = np.float64(np.take(data[2:,index], getScenarios(juniors)))
    sample_data_senior = np.float64(np.take(data[2:,index], getScenarios(seniors)))
    print(sample_data_intern)
    print(sample_data_junior)
    print(sample_data_senior)
    # sample_data = reject_outliers(sample_data)

    print(sp.stats.kstest(sample_data_intern, sample_data_junior))
    print(sp.stats.kstest(sample_data_intern, sample_data_senior))
    print(sp.stats.kstest(sample_data_junior, sample_data_senior))

    # my_histogram(sample_data_intern)
    # my_histogram(sample_data_junior)
    # my_histogram(sample_data_senior)
    # qq_plot(sample_data)
    
def main():

    #BIRADS
    print("-------------- BIRADS ---------------")
    isSameDistribution(3)

    #Time
    print("-------------- TIME ---------------")
    isSameDistribution(4)

    #DOTS
    print("-------------- DOTS ---------------")
    isSameDistribution(5)
    isSameDistribution(6)
    isSameDistribution(7)

    #SUS
    print("-------------- SUS ---------------")
    isSameDistribution(8)
    isSameDistribution(9)
    isSameDistribution(10)
    isSameDistribution(11)
    isSameDistribution(12)
    isSameDistribution(13)
    isSameDistribution(14)
    isSameDistribution(15)
    isSameDistribution(16)
    isSameDistribution(17)

    #NASA-TLX
    print("-------------- NASA-TLX ---------------")
    isSameDistribution(18)
    isSameDistribution(19)
    isSameDistribution(20)
    isSameDistribution(21)
    isSameDistribution(22)
    isSameDistribution(23)

if __name__ == "__main__":
    main()
