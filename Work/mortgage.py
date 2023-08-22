# mortgage.py
#
# Exercise 1.7


principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.00
total_paid = 0.0
month = 0
start_month = 61
end_month = 108

while principal > 0:
    month += 1
    if (month >= start_month) and (month <= end_month):
        montly_payment = payment + extra_payment
    else:
        montly_payment = payment
    principal = principal * (1+rate/12) - montly_payment
    total_paid = total_paid + montly_payment
    print(month, round(principal, ndigits=2))

print('Total paid', total_paid)
print('Months', month)
print('test')