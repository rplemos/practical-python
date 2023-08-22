#import os
#os.getcwd()

with open('Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line, end='')
        #data = f.read()

#print(data)