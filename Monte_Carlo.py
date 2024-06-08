# Implementing Monte Carlo Simulation of a Stock Portfolio with Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
# from pandas_datareader import data as pdr  # module to can get Yahoo data
# more robust and frequently updated library to fetch Yahoo finance data


# Import data
# covariance matrix get mean returns of selected stocks during a defined period of time
def get_data(stocks, start, end):
    stockData = yf.download(stocks, start=start, end=end)
    stockData = stockData['Close']  # only interested in daily changes
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix


# just some random Austrlian stocks
stockList = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC']
# Add '.AX' suffix for Australian stocks
stocks = [stock + '.AX' for stock in stockList] 
endDate = dt.datetime.now()
# the time range determines the covMatrix, super crucial
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

# print(meanReturns)

# Define weights for the portfolio
weights = np.random.random(len(meanReturns))    # random gives values btw [0,1]
weights /= np.sum(weights)  # normalise all weights so that they sum up to 1

print(weights)

# Monte Carlo Method
# number of simulations
mc_sims = 100
T = 100 # timeframe in days

# define arrays to store and access information
meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)   # shape depends on number of days and number of stocks
meanM = meanM.T     # Transpose for computation, why?

portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)    # 0.0 is so that we can take in float values

# Initialise an initial portfolio value
initialPortfolio = 10000

# Assumption: daily returns follows a Multivariate Normal Distribition -> use Cholesky Decomposition to determine Lower Triangle Matrix
for m in range(0, mc_sims):
    # MC loops
    z = np.random.normal(size=(T, len(weights)))   # uncorrelated random variables from the normal dist
    L = np.linalg.cholesky(covMatrix)
    dailyReturns = meanM + np.inner(L, z)              # np.inner() is the dot prod of all the stocks in the portfolio. notice that the meanM = meanM.T allows for matrix addition in this step since matrix size is now correct
    portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio

# plot the portfolio simulation
plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($S)')
plt.xlabel('Days')
plt.title('MC simulation of a stock portfolio')
plt.show()
