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

    #BIRADS
    print("-------------- BIRADS ---------------")
    kruskalWallis(3)

    #Time
    print("-------------- TIME ---------------")
    kruskalWallis(4)

    #DOTS
    print("-------------- DOTS ---------------")
    kruskalWallis(5)
    kruskalWallis(6)
    kruskalWallis(7)

    #SUS
    print("-------------- SUS ---------------")
    kruskalWallis(8)
    kruskalWallis(9)
    kruskalWallis(10)
    kruskalWallis(11)
    kruskalWallis(12)
    kruskalWallis(13)
    kruskalWallis(14)
    kruskalWallis(15)
    kruskalWallis(16)
    kruskalWallis(17)

    #NASA-TLX
    print("-------------- NASA-TLX ---------------")
    kruskalWallis(18)
    kruskalWallis(19)
    kruskalWallis(20)
    kruskalWallis(21)
    kruskalWallis(22)
    kruskalWallis(23)


    #NASA-TLX
    print("-------------- Preference ---------------")
    kruskalWallis(24)
    kruskalWallis(25)
    kruskalWallis(26)
    kruskalWallis(27)
    kruskalWallis(28)
    kruskalWallis(29)
    kruskalWallis(30)
    kruskalWallis(31)
    kruskalWallis(32)

if __name__ == "__main__":
    main()
