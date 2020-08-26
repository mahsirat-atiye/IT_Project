import random
from arch.unitroot import VarianceRatio
import statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd


class VarianceRatioTest:
    def __init__(self, significance=.05):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None

    def VarianceRatio_Stationarity_Test(self, timeseries, stock):
        # Variance Ratio Testing:
        variance_ratio_test = VarianceRatio(timeseries)

        self.pValue = variance_ratio_test.pvalue

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = True
        else:
            self.isStationary = False
        VarianceRatioTestResult = dict()

        VarianceRatioTestResult['Stock Name'] = stock
        VarianceRatioTestResult['Is Stationary'] = self.isStationary
        VarianceRatioTestResult['Variance Ratio Andrews Test Statistic'] = variance_ratio_test.stat
        VarianceRatioTestResult['P-Value'] = variance_ratio_test.pvalue
        VarianceRatioTestResult['# Lags Used'] = int(variance_ratio_test.lags)

        for key, value in variance_ratio_test.critical_values.items():
            VarianceRatioTestResult['Critical Value (%s)' % key] = value

        return VarianceRatioTestResult

