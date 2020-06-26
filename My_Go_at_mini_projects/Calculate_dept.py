import math

user_principal = int(input())
what_to_cal = input(print('what do you want to calculate? \n'
                          ' type "m" for count of months ', '\n'
                         ' Type "p" for monthly payment:'))
if what_to_cal == 'p':
    total_months = int(input('Enter count of months:'))
    payment = user_principal / total_months
    last_month = user_principal - (total_months - 1 * math.ceil(payment))
    if payment != last_month:
        print("Your monthly payment =", math.ceil(payment), "with last month payment =", math.ceil(last_month) )
    else:
        print('Your monthly payment = ', math.ceil(payment))
elif what_to_cal == 'm':
    monthly_payment = int(input('Enter monthly payment:'))
    total_months = user_principal / monthly_payment
    payment = (int(user_principal) / int(total_months))
    last_month = int(user_principal - (total_months - 1) * payment)
    if payment != last_month:
        print("Your monthly payment =", math.ceil(payment), "with last month payment =", math.ceil(total_months))
    else:
        print("It takes", total_months, "months to repay the credit")

