# bounce.py
#
# Exercise 1.5

start_height = 100 
num_bounce = 0

while num_bounce <= 10:
    print(round(start_height, ndigits=4))
    start_height = start_height * 0.6
    num_bounce += 1
