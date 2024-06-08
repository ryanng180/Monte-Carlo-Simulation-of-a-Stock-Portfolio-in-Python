# Monte-Carlo-Simulation-of-a-Stock-Portfolio-in-Python

This project implements a Monte Carlo simulation to model the future value of a stock portfolio over a given timeframe. The simulation is based on historical stock data and generates multiple potential outcomes to assess the risk and return of the portfolio. And is by no means robust.

## Project Overview
Monte Carlo simulation is a powerful statistical technique used to understand the impact of risk and uncertainty in prediction and forecasting models. In the context of financial portfolios, it helps in modeling the behavior of asset returns and portfolio value under different scenarios.

This Python script performs the following tasks:
<ol>Fetches historical stock data: Using the Yahoo Finance API.</ol>
<ol>Calculates statistical properties: Mean returns and covariance matrix of the selected stocks.</ol>
<ol>Generates random weights: For the stocks in the portfolio.</ol>
<ol>Simulates future portfolio values: Using Monte Carlo simulation.</ol>
<ol>Plots the simulation results: To visualize the range of possible outcomes for the portfolio value.</ol>

## Prerequisites
Ensure you have the following libraries installed:
```sh
pip install pandas numpy matplotlib yfinance
```

## Running the MC simulation
<ol>Run the Monte Carlo.py script to execute the Monte Carlo simulation. The script fetches data for 5 preselected Australian stocks, computes their mean returns and covariance matrix, and then runs the simulation to predict future portfolio values.</ol>

**Fetch Data**:
<ol>It defines a get_data function to fetch historical stock data from Yahoo Finance, compute daily returns, mean returns, and the covariance matrix.</ol>

**Define Portfolio Weights**:
<ol>It generates random weights for the stocks in the portfolio and normalizes them to sum up to 1.</ol>

**Monte Carlo Simulation**:
<ol>The simulation runs multiple iterations, generating possible future values for the portfolio based on the assumption that daily returns follow a Multivariate Normal Distribution hence Cholesky Decomposition is used to determine the Lower Triangle Matrix.</ol>

**Plot Results**:
<ol>The script plots the results of the simulation, showing the range of possible outcomes for the portfolio value over time. Choice of time period for this simulation is 100 days.</ol>

**Example Output**
<ol>The script will output a plot similar to the following:</ol>
<ol><img src="Figure_1.png" /></ol>

## Potential Improvements
**Data Handling and Cleaning:**
<ol>Ensure that the data is clean and there are no missing values, outliers, or anomalies. You can include additional data cleaning steps to handle such issues.
The current code uses forward and backward filling for missing data. While this is a quick solution, more sophisticated methods (e.g., interpolation or regression techniques) might provide better results.</ol>

**Parameterization:**
<ol>Allow for user-defined parameters such as the number of simulations (mc_sims), the investment horizon (T), and the initial portfolio value (initialPortfolio).
Implement input validation to ensure the parameters are within reasonable ranges.</ol>

**Distribution Assumption:**
<ol>The assumption that returns follow a multivariate normal distribution might not hold in all cases. Consider exploring other distributions (e.g., t-distribution) or using empirical distributions derived from historical data.</ol>

**Performance Optimization:**
<ol>For large-scale simulations, consider performance optimization techniques such as parallel processing or vectorized operations to speed up computations.</ol>

**Scenario Analysis:**
<ol>Include features for stress testing and scenario analysis to evaluate how the portfolio performs under different economic conditions.</ol>

**Risk Metrics:**
<ol>Calculate and report additional risk metrics such as Value at Risk (VaR), Conditional Value at Risk (CVaR), Sharpe Ratio, and Maximum Drawdown.</ol>

**Visualization and Reporting:**
<ol>Enhance the visualization by adding more informative plots, such as histograms of final portfolio values, confidence intervals, and comparative plots for different scenarios.
Generate summary reports with key statistics and findings from the simulations.</ol>
