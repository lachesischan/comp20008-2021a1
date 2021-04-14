import pandas as pd
import argparse
import sys


url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
df = pd.read_csv(url)

#add 'month' column into dataframe
df['date']= pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

#Select range of dates and columns needed and create a new dataframe
select_row = df.query("date >= '2020-02-24' and date <='2020-12-31'")
df1 = select_row[['location','month','total_cases','new_cases','total_deaths','new_deaths']]

# group the dataframe by location and month
pa1= df1.groupby(['location','month']).sum()



#Part A Task 1/2

pa1['case_fatality_rate'] = pa1['new_deaths']/pa1['new_cases'] 
cols = pa1.columns.tolist()

cols = cols[-1:] + cols[:-1]
pa1 = pa1[cols]

pa2 = pa1.head(5)



pa1.to_csv(sys.stdout)

filename = sys.argv[-1]

pa1.to_csv(filename)
print(pa2)
