# pcost.py
#
# Exercise 1.27

total = 0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        arr = line.split(',')
        total = total + (int(arr[1]) * float(arr[2]))
print(total)        