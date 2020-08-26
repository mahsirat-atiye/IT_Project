import json

import pandas
import os
import matplotlib.pyplot as plt

from Utils.ADF import ADFTest
from Utils.KPSS import KPSSTest
from Utils.PP import PPTest
from Utils.Variance_Ratio import VarianceRatioTest
from Utils.Zivot_Andrews import ZivotAndrewsTest

DAILY_DATA_DIR = "Data/DailyData/"
RESULT_DIR = "Result/"
"""
'<TICKER>', '<DTYYYYMMDD>', '<FIRST>', '<HIGH>', '<LOW>', '<CLOSE>',
       '<VALUE>', '<VOL>', '<OPENINT>', '<PER>', '<OPEN>', '<LAST>'
"""
stocks = []
for name in os.listdir(DAILY_DATA_DIR):
    stocks.append(name)


def change(row):
    return (row['<CLOSE>'] - row['<OPEN>']) / row['<OPEN>']


ADFTester = ADFTest()
ADFTestResults = []

PPTester = PPTest()
PPTestResults = []

KPSSTester = KPSSTest()
KPSSTestResults = []

VarianceRatioTester = VarianceRatioTest()
VarianceRatioTestResults = []

ZivotAndrewsTester = ZivotAndrewsTest()
ZivotAndrewsTestResults = []

plt.style.use('ggplot')
fig, axs = plt.subplots(len(stocks))
for i, stock in enumerate(stocks):
    df = pandas.read_csv(DAILY_DATA_DIR + stock)
    df['Change'] = df.apply(lambda row: change(row), axis=1)
    axs[i].plot(df['Change'])
    axs[i].set_title(stock)

    temp = ADFTester.ADF_Stationarity_Test(df['Change'], stock)
    ADFTestResults.append(temp)

    temp = PPTester.PP_Stationarity_Test(df['Change'], stock)
    PPTestResults.append(temp)

    temp = KPSSTester.KPSS_Stationarity_Test(df['Change'], stock)
    KPSSTestResults.append(temp)

    temp = VarianceRatioTester.VarianceRatio_Stationarity_Test(df['Change'], stock)
    VarianceRatioTestResults.append(temp)

    temp = ZivotAndrewsTester.ZivotAndrews_Stationarity_Test(df['Change'], stock)
    ZivotAndrewsTestResults.append(temp)

# Exporting results

ADF_content = pandas.read_json(str(json.dumps(ADFTestResults)))
ADF_content.to_excel(RESULT_DIR + 'ADF.xlsx', index=True)

PP_content = pandas.read_json(str(json.dumps(PPTestResults)))
PP_content.to_excel(RESULT_DIR + 'PP.xlsx', index=True)


KPSS_content = pandas.read_json(str(json.dumps(KPSSTestResults)))
KPSS_content.to_excel(RESULT_DIR +'KPSS.xlsx', index=True)

VarianceRatio_content = pandas.read_json(str(json.dumps(VarianceRatioTestResults)))
VarianceRatio_content.to_excel(RESULT_DIR +'VarianceRatio.xlsx', index=True)

ZivotAndrews_content = pandas.read_json(str(json.dumps(ZivotAndrewsTestResults)))
ZivotAndrews_content.to_excel(RESULT_DIR +'ZivotAndrews.xlsx', index=True)

plt.show()
