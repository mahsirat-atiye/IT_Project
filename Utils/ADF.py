import random

import statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd


class ADFTest:
    def __init__(self, significance=.05):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None

    def ADF_Stationarity_Test(self, timeseries, stock):
        # Dickey-Fuller test:
        adfTest = adfuller(timeseries, autolag='AIC')

        self.pValue = adfTest[1]

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = True
        else:
            self.isStationary = False
        ADFResult = dict()

        ADFResult['Stock Name'] = stock
        ADFResult['Is Stationary'] = self.isStationary
        ADFResult['ADF Test Statistic'] = adfTest[0]
        ADFResult['P-Value'] = adfTest[1]
        ADFResult['# Lags Used'] = adfTest[2]
        ADFResult['# Observations Used'] = adfTest[3]

        for key, value in adfTest[4].items():
            ADFResult['Critical Value (%s)' % key] = value

        return ADFResult

