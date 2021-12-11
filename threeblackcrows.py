from yahoofinancials import YahooFinancials as yf
from datetime import datetime as dt
from datetime import date as date
from datetime import timedelta as td
import pandas as pd
import numpy as np


#### User Inputs ####
ticker = 'NET'         # ticker
percentRed = .5        # how much of the candle needs to be body for it to be considered "solid red"
pastDays = 1000       # ** MUST BE > 10 ** how many past days for dataframe ** MUST BE > 10 **
#### End User Inputs ####

past_Days = td(pastDays)
yf_aapl = yf(ticker)

# get the "10" most recent days; will only return weekdays, so will be less than 10
hist_price_date = yf_aapl.get_historical_price_data(str(date.today()-past_Days), str(date.today()), 'daily')

# create a dataframe from historical price dictionary
x = 0
df = pd.DataFrame()
for dates in hist_price_date[ticker]['prices']:
    df.loc[x, 0] = dates['formatted_date']
    df.loc[x, 1] = dates['open']
    df.loc[x, 2] = dates['close']
    df.loc[x, 3] = dates['high']
    df.loc[x, 4] = dates['low']
    x += 1

# set column names of dataframe
df = df.set_axis(['Date', 'Open', 'Close', 'High', 'Low'], axis=1, inplace = False)

# reverse dataframe so most recent date is row 0
df = df.iloc[::-1]
df = df.reset_index()
df = df.drop(columns='index')

# add a calculated column of open - close difference and high - low difference
df['OpenCloseDiff'] = df.Close - df.Open
df['HighLowDiff'] = df.High - df.Low

# Create "Solid Red?" column and set to true if candle is "solid red"
df['Solid Red?'] = np.where(df['OpenCloseDiff'] < percentRed * -1 *(df['HighLowDiff']), True, False)

# if last three days are solid red, set 3BC to true
df['3BC'] = (df['Solid Red?'] == True) & (df['Solid Red?'].shift(-1) == True) & (df['Solid Red?'].shift(-2) == True)

# is the next day negative?
df['NextDayNegative?'] = df['OpenCloseDiff'].shift(1) < 0


pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 0)

print(df)


