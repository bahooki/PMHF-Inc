# >>> import os
# >>> os.getcwd()
# 'C:\\Python'
# >>> os.chdir('C:\\code')
# >>> os.getcwd()
# 'C:\\code'
# >>>exec(open("fincorr.py").read())
## To receive two ticker inputs and a date range in 'MM/DD/YYYY - MM/DD/YYYY' format and calculate ##
## their Pearson Product Moment Correlation (PPMC) coefficient. ##

## PPMC = covariance(X, Y) / (stdv(X) * stdv(Y))

from yahoofinancials import YahooFinancials

# print()
# print("Let's calculate how correlated two tickers are!")
# ticker1 = input("Please enter the 1st ticker: ")
# print("Ticker 1 is " + ticker1)
# print()
# ticker2 = input("Please enter the 2nd ticker: ")
# print("Ticker 2 is " + ticker2)
# print()
# # daterange = input("Please enter the correlation timeframe (format is YYYY-MM-DD to YYYY-MM-DD): ")
# # print("The Date Range is " + daterange)
# startdate = input("Please enter the start date of the period you want to see (format is YYYY-MM-DD): ")
# print("The Start Date is " + startdate)
# print()
# enddate = input("Please enter the end date of the period you want to see (format is YYYY-MM-DD): ")
# print("The End Date is " + enddate)

ticker1 = 'PATH'
ticker2 = 'RNG'
startdate = '2021-12-01'
enddate = '2021-12-08'

yahooticker1 = YahooFinancials(ticker1)
yahooticker2 = YahooFinancials(ticker2)

prices = yahooticker1.get_historical_price_data(startdate, enddate, 'daily') #outputs as a Python Dictionary datatype!
prices2 = yahooticker2.get_historical_price_data(startdate, enddate, 'daily') #outputs as a Python Dictionary datatype!

day1high = prices[ticker1]['prices'][0]['close'] #outputs this one value I'm referencing; since it's a List within a series of
#dictionaries, need to specify the list position of the final set of dictionary variables representing each day

print(day1high * 2)

# print(pyprices)
# print(pyprices2)

#User table, this is where the user orders a material
# tab_user = {
 # 'USER1': 'MAT1',
 # 'USER2': 'MAT1',
 # 'USER3': 'MAT3',
 # 'USER4': 'MAT4' }

# #Type table, this determine the material type
# tab_type = {
 # 'MAT1': 'FERT',
 # 'MAT2': 'ROH',
 # 'MAT3': 'FERT',
 # 'MAT4': 'ZZZ1' 
# }

# while True:
    # ticker1 = input("Please enter the 1st ticker: ")
    # if ticker1 == "quit": break
    # print(ticker1)
    
    # ticker2 = input("Please enter the 2nd ticker: ")
    # if ticker2 == "quit": break
    # print(ticker2)



