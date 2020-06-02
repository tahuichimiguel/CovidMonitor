import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

#Counties adjacent to Allegheny: ["Washington","Beaver","Butler","Armstrong","Westmoreland"]
#relevant_counties = ["Allegheny County","Washington","Beaver","Butler","Armstrong","Westmoreland"]

state = "PA"
county = ["Allegheny County"]
week_window = 5
first_relevant_week = '3/2/20'

relevant_county_names = county
days_window = week_window*7

pa_phase_yellow_date = '5/15/20'

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m/%d/%Y")
    d2 = datetime.strptime(d2, "%m/%d/%Y")
    return abs((d2 - d1).days)

# Data Load
covid_df = pd.read_csv("covid_confirmed_usafacts.csv")
pa_covid_df = covid_df[covid_df["State"] == state]

# Data Processing

## Data Filtering
county_covid_df = pa_covid_df[pa_covid_df["County Name"].isin(relevant_county_names)]

## Data Transformation
contained_dates = [a for a in county_covid_df.columns[4:]]
transformed_county_covid_df = county_covid_df[contained_dates].transpose()
transformed_county_covid_df = transformed_county_covid_df.rename(
    columns = {transformed_county_covid_df.columns[0]:"cases"}
)
relevant_county_covid_df = transformed_county_covid_df[transformed_county_covid_df.index > first_relevant_week]

# Plot Total Cases
relevant_county_covid_df.plot(y="cases",
                                 figsize = (10,5),
                                 title = "Total Cases in " + str(relevant_county_names)
)

plt.grid()
plt.savefig('TotalCases.png')

# Plot New Cases
diff_df = relevant_county_covid_df.diff()
diff_df = diff_df.tail(days_window).rename(columns = {"cases":"new-covid-cases"})

ymax = diff_df["new-covid-cases"].max()
xmax = diff_df.shape[0]

diff_df.plot(y = "new-covid-cases",
             kind = "bar", figsize = (20,8),
             title = "New Cases in " + str(county) + " (Last " + str(days_window) + " Days)")
plt.ylim(0,ymax+1)

#hacky fix for year - fix at later point
phase_yellow_location = days_between(pa_phase_yellow_date+str(20),diff_df.index[-1]+str(20)) - 1
plt.vlines(x = xmax-phase_yellow_location,
           ymin = 0,
           ymax = ymax+1,
           colors='y')

plt.grid()
plt.savefig('NewCases.png')


# In[ ]:




