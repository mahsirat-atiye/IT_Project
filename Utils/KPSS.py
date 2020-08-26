import random
from arch.unitroot import KPSS
import statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd


class KPSSTest:
    def __init__(self, significance=.05):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None

    def KPSS_Stationarity_Test(self, timeseries, stock):
        # KPSS Testing:
        kpssTest = KPSS(timeseries)

        self.pValue = kpssTest.pvalue

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = True
        else:
            self.isStationary = False
        KPSSResult = dict()

        KPSSResult['Stock Name'] = stock
        KPSSResult['Is Stationary'] = self.isStationary
        KPSSResult['KPSS Test Statistic'] = kpssTest.stat
        KPSSResult['P-Value'] = kpssTest.pvalue
        KPSSResult['# Lags Used'] = int(kpssTest.lags)

        for key, value in kpssTest.critical_values.items():
            KPSSResult['Critical Value (%s)' % key] = value

        return KPSSResult

