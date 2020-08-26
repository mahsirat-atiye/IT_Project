import random
from arch.unitroot import ZivotAndrews
import statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd


class ZivotAndrewsTest:
    def __init__(self, significance=.05):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None

    def ZivotAndrews_Stationarity_Test(self, timeseries, stock):
        # ZivotAndrews Testing:
        zivot_andrews_test = ZivotAndrews(timeseries)

        self.pValue = zivot_andrews_test.pvalue

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = True
        else:
            self.isStationary = False
        ZivotAndrewsTestResult = dict()

        ZivotAndrewsTestResult['Stock Name'] = stock
        ZivotAndrewsTestResult['Is Stationary'] = self.isStationary
        ZivotAndrewsTestResult['Zivot Andrews Test Statistic'] = zivot_andrews_test.stat
        ZivotAndrewsTestResult['P-Value'] = zivot_andrews_test.pvalue
        ZivotAndrewsTestResult['# Lags Used'] = int(zivot_andrews_test.lags)

        for key, value in zivot_andrews_test.critical_values.items():
            ZivotAndrewsTestResult['Critical Value (%s)' % key] = value

        return ZivotAndrewsTestResult

