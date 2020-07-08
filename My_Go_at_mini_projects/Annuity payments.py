import math

what_to_cal = input(print('what do you want to calculate? \n'
                          ' type "n" - for count of months,', '\n'
                          ' type "a" - for annuity monthly payment', '\n'
                          ' type "p" - for credit principal:'))
if what_to_cal == 'n':
    credit_principal = float(input('Enter credit principal:'))
    monthly_payment = float(input('Enter monthly payment:'))
    credit_interest = float(input('Enter credit interest:'))
    i = credit_interest / (12*100)
    num_of_payments = math.ceil(math.log((monthly_payment/(monthly_payment-i*credit_principal)),1+i))
    n = num_of_payments
    years = n // 12
    months = n % 12
    if years > 1 and months == 0:
        print(f'You need {years} to repay this credit!')
    elif years > 1 and months >= 1:
        print(f'You need {years} and {months} to repay this credit!')
elif what_to_cal == 'a':
    credit_principal = float(input('Enter credit principal:'))
    count_periods = int(input('Enter count of periods:'))
    credit_interest = float(input('Enter credit interest:'))
    i = credit_interest / (12*100)
    annuity_payments = credit_principal *((i*(1+i)**count_periods)/((1+i)**count_periods-1))
    print(f'Your annuity payment = {annuity_payments}')
elif what_to_cal == 'p':
    monthly_payment = float(input('Enter monthly payment:'))
    count_periods = int(input('Enter count of periods:'))
    credit_interest = float(input('Enter credit interest:'))
    i = credit_interest / (12*100)
    credit_principal = monthly_payment /((i*(1+i)**count_periods)/((1+i)**count_periods-1))
    print(f'Your credit principal = {credit_principal}!')



