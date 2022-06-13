import numpy as np

def lower_bound(data):

    percentile25 = np.quantile(data, 0.25)
    percentile75 = np.quantile(data, 0.75)

    iqr = percentile75 - percentile25

    lower_limit = percentile25 - 1.5 * iqr

    return lower_limit

def upper_bound(data):

    percentile25 = np.quantile(data, 0.25)
    percentile75 = np.quantile(data, 0.75)

    iqr = percentile75 - percentile25

    upper_limit = percentile75 + 1.5 * iqr

    return upper_limit

def reject_outliers(data):

    upper_limit = upper_bound(data)
    lower_limit = lower_bound(data)

    data = np.delete(data, np.argwhere(data > upper_limit))
    data = np.delete(data, np.argwhere(data < lower_limit))

    return data