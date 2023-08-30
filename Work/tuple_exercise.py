import csv

f = open('Data/portfolio.csv')

rows = csv.reader(f)
headers = next(f).split(',')
row = next(rows)
t = (row[0], int(row[1]), float(row[2]))

print(t)
print(type(t))
print(t[1]*t[2])

