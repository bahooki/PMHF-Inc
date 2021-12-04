import json
import datetime
from yahoofinancials import YahooFinancials

ticker = 'SNOW'
yahoo_financials = YahooFinancials(ticker)

e = datetime.datetime.now() - timedelta(days=1)
s = e - timedelta(days=7)

e.strftime('%y-%m-%d') # not working when passed to yahoo financials
s.strftime('%y-%m-%d') # not working when passed to yahoo financials

prices = yahoo_financials.get_historical_price_data('2021-11-29', '2021-12-04', 'daily') #filters weekends on it's own. Nice!

json_string = json.dumps(prices) # converts dict to string

p_obj = json.loads(json_string) # converts json string to python object
	
api_data = json.dumps(p_obj, indent=2) # pretty print

print(api_data)

#print(yahoo_financials.get_market_cap())
#print(yahoo_financials.get_daily_low())