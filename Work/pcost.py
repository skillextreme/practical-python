# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    sum=0
    totalcost=0
    with open(filename, 'rt')as file:
        headers = next(file).split(',')
        for line in file:
            row = line.split(',')
            totalcost= float(row[1])*float(row[2].strip())
            sum=totalcost+sum
        return sum
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)