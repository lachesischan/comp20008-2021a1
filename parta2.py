import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys


filename1 = sys.argv[-2]
filename2 = sys.argv[-1]
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df=pd.read_csv(url)

select_row = df.query("date >= '2020-02-24' and date <='2020-12-31'")

df1 = select_row[['location','new_cases','new_deaths']]
df2 = df1.groupby(['location']).sum()
df2['case_fatality_rate'] = df2['new_deaths']/df2['new_cases']



x = df2['new_cases']
y = df2['case_fatality_rate']


plt.scatter(x, y)
plt.xlabel('new cases')
plt.ylabel('case fatality rate')
plt.savefig(filename1)
plt.close()




plt.scatter(np.log(x), y)
plt.xlabel('new cases with log scale')
plt.ylabel('case fatality rate')
plt.savefig(filename2)
plt.close()
