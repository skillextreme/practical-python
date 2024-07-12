# mortgage.py
#
# Exercise 1.7

print("Exercise 1.7")

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment


print('Total paid', total_paid)

print("Exercise 1.8")

principal = 500000.0
rate = 0.05
payment = 2684.11
extra = 1000
total_paid = 0.0
months=0

while principal > 0:
    if (months<12):
        principal = principal * (1+rate/12) - (payment + extra)
        total_paid = total_paid + payment + extra
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment  
    months=months+1   
    
print('Total paid = ', total_paid , 'Months = ' , months)

print(" Exercise 1.9 , 1.10 , 1.11")

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month =int(input(" Give the start month"))
extra_payment_end_month =int(input(" Give the end month"))
extra_payment =int(input(" Give the extra amount"))
months=0
final_payment=0

while principal > 0:
    months=months+1
    if (months>=extra_payment_start_month and months<=extra_payment_end_month):
        final_payment= extra_payment + payment
    else:
        final_payment= payment
    principal = principal * (1+rate/12) - final_payment
    total_paid = total_paid + final_payment
    if (principal<=0):
        total_paid=total_paid + principal
        principal=0
        print(months,total_paid,principal)
    else:
        print(months,total_paid,principal)

result=f'total paid amount is {total_paid:0.2f} and the numeber of months it took are {months}'

print(result)

