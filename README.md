# Monte-Carlo-Simulation-of-a-Stock-Portfolio-in-Python

Monte Carlo Simulation of a Stock Portfolio
This project implements a Monte Carlo simulation to model the future value of a stock portfolio over a given timeframe. The simulation is based on historical stock data and generates multiple potential outcomes to assess the risk and return of the portfolio.

Project Overview
Monte Carlo simulation is a powerful statistical technique used to understand the impact of risk and uncertainty in prediction and forecasting models. In the context of financial portfolios, it helps in modeling the behavior of asset returns and portfolio value under different scenarios.

This Python script performs the following tasks:

Fetches historical stock data: Using the Yahoo Finance API.
Calculates statistical properties: Mean returns and covariance matrix of the selected stocks.
Generates random weights: For the stocks in the portfolio.
Simulates future portfolio values: Using Monte Carlo simulation.
Plots the simulation results: To visualize the range of possible outcomes for the portfolio value.
Prerequisites
Ensure you have the following libraries installed:

pandas
numpy
matplotlib
yfinance
You can install these libraries using pip:

bash
Copy code
pip install pandas numpy matplotlib yfinance
Getting Started
Clone this repository to your local machine and navigate to the project directory.

bash
Copy code
git clone https://github.com/yourusername/monte-carlo-stock-portfolio.git
cd monte-carlo-stock-portfolio
Usage
Run the Monte Carlo.py script to execute the Monte Carlo simulation. The script fetches data for a selection of Australian stocks, computes their mean returns and covariance matrix, and then runs the simulation to predict future portfolio values.

bash
Copy code
python "Monte Carlo.py"
Script Details
Import Libraries:
The script imports necessary libraries such as pandas, numpy, matplotlib, datetime, and yfinance.

Fetch Data:
It defines a get_data function to fetch historical stock data from Yahoo Finance, compute daily returns, mean returns, and the covariance matrix.

Define Portfolio Weights:
It generates random weights for the stocks in the portfolio and normalizes them to sum up to 1.

Monte Carlo Simulation:
The simulation runs multiple iterations, generating possible future values for the portfolio based on the assumption that daily returns follow a Multivariate Normal Distribution.

Plot Results:
The script plots the results of the simulation, showing the range of possible outcomes for the portfolio value over time.

Example Output
The script will output a plot similar to the following:
