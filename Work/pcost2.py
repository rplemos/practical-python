def cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            arr = line.split(',')
            try:
                total = total + (int(arr[1]) * float(arr[2]))
            except ValueError:
                print("Couldn't parse", line)
    return(total)        

portfolio = cost('Data/missing.csv')
print(portfolio)