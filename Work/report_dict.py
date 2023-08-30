# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            entry = {
                'name':row[0],
                'shares':int(row[1]),
                'price':float(row[2])
            }
            portfolio.append(entry)
    return portfolio

def calculate(portfolio):
    total = 0
    for name, shares, price in portfolio:
        total += shares*price
    return total

portfolio = read_portfolio('Data/portfolio.csv')
#total = calculate(portfolio)

#print("Portfolio: ", portfolio)
print(portfolio[0])
