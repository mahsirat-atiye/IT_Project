import random
from arch.unitroot import PhillipsPerron
import statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd


class PPTest:
    def __init__(self, significance=.05):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None

    def PP_Stationarity_Test(self, timeseries, stock):
        # Phillips-Perron Testing:
        ppTest = PhillipsPerron(timeseries)

        self.pValue = ppTest.pvalue

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = True
        else:
            self.isStationary = False
        PPResult = dict()

        PPResult['Stock Name'] = stock
        PPResult['Is Stationary'] = self.isStationary
        PPResult['PP Test Statistic'] = ppTest.stat
        PPResult['P-Value'] = ppTest.pvalue
        PPResult['# Lags Used'] = ppTest.lags

        for key, value in ppTest.critical_values.items():
            PPResult['Critical Value (%s)' % key] = value

        return PPResult

