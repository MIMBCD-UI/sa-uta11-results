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
from outliers import reject_outliers

def my_histogram(data):
    fig = px.histogram(data)
    fig.show()

def qq_plot(data):
    
    sm.qqplot(data)
    pylab.show()

def isNormal(index):
    sample_data = np.float64(data[2:,index])
    # print(sample_data)
    # sample_data = reject_outliers(sample_data)
    # print(sample_data)
    print(sp.stats.shapiro(sample_data))
    print(sp.stats.kstest(sample_data, 'norm'))
    print(sp.stats.anderson(sample_data))

    my_histogram(sample_data)
    # qq_plot(sample_data)
    
def main():

    #BIRADS
    print("-------------- BIRADS ---------------")
    isNormal(3)

    #Time
    print("-------------- TIME ---------------")
    isNormal(4)

    #DOTS
    print("-------------- DOTS ---------------")
    isNormal(5)
    isNormal(6)
    isNormal(7)

    #SUS
    print("-------------- SUS ---------------")
    isNormal(8)
    isNormal(9)
    isNormal(10)
    isNormal(11)
    isNormal(12)
    isNormal(13)
    isNormal(14)
    isNormal(15)
    isNormal(16)
    isNormal(17)

    #NASA-TLX
    print("-------------- NASA-TLX ---------------")
    isNormal(18)
    isNormal(19)
    isNormal(20)
    isNormal(21)
    isNormal(22)
    isNormal(23)

    

if __name__ == "__main__":
    main()
