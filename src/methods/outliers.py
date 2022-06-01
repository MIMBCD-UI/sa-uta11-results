import numpy as np

def reject_outliers(data):
    percentile25 = np.quantile(data, 0.25)
    percentile75 = np.quantile(data, 0.75)

    iqr = percentile75 - percentile25

    upper_limit = percentile75 + 1.5 * iqr
    lower_limit = percentile25 - 1.5 * iqr

    data = np.delete(data, np.argwhere(data > upper_limit))
    data = np.delete(data, np.argwhere(data < lower_limit))

    return data