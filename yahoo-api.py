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
=======
from yahoofinancials import YahooFinancials

ticker = 'NQ=F'
yahoo_financials = YahooFinancials(ticker)

# balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
# income_statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income')
# all_statement_data_qt =  yahoo_financials.get_financial_stmts('quarterly', ['income', 'cash', 'balance'])
# apple_earnings_data = yahoo_financials.get_stock_earnings_data()
# apple_net_income = yahoo_financials.get_net_income()
historical_stock_prices = yahoo_financials.get_historical_price_data('2020-09-01', '2020-10-01', 'monthly')
print(historical_stock_prices)
print(get_market_cap())
