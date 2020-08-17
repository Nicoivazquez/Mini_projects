import math
import sys
import argparse as args

parser = args.ArgumentParser()
parser.add_argument("--type", help="...")
parser.add_argument("--principal", help="...", type=int)
parser.add_argument("--periods", help="...", type=int)
parser.add_argument("--interest", help="...", type=float)
parser.add_argument("--annuity", help="...")
parser.add_argument("--payment", help="...", type=int)
args = parser.parse_args()

count = 0
for key,value in args.__dict__.items():
    if value == None:
        count += 1
    if count >= 4:
        print('Incorrect parameters')
        sys.exit()
    if key != 'type':
            if value != None:
                if value < 0:
                    print('Incorrect parameters')
                    sys.exit()

choices=['diff','annuity']
if args.type not in choices:
    print('Incorrect parameters')
    sys.exit()
elif args.interest == None:
    print('Incorrect parameters')
    sys.exit()

if args.type == 'diff':
    monthly_payments = []
    principal = args.principal
    periods = args.periods
    interest = args.interest
    ajusted_intrest = interest / (12 * 100)
    m = 0
    while m < periods:
        m += 1
        diff_pay_month = math.ceil(
            principal / periods + ajusted_intrest * (principal - (principal * (m - 1) / periods)))
        monthly_payments.append(diff_pay_month)
    for idx, num in enumerate(monthly_payments):
        print(f'Month {idx + 1}: paid out {num}')
    overpayment = sum(monthly_payments) - principal
    print(f'Overpayment = {overpayment}')
    sys.exit()

if (args.type == 'annuity') and (args.payment is not None) and (args.principal is not None):
    credit_principal = args.principal
    monthly_payment = args.payment
    credit_interest = args.interest
    i = credit_interest / (12 * 100)
    num_of_payments = math.ceil(math.log((monthly_payment / (monthly_payment - i * credit_principal)), 1 + i))
    n = num_of_payments
    years = n // 12
    months = n % 12
    overpayment = monthly_payment * num_of_payments - credit_principal
    if years > 1 and months == 0:
        print(f'You need {years} years to repay this credit!')
        print(f'Overpayment = {overpayment}')
    elif years > 1 and months >= 1:
        print(f'You need {years} years and {months} months to repay this credit!')
        print(f'Overpayment = {overpayment}')
        sys.exit()
elif (args.type == 'annuity') and (args.periods is not None) and (args.principal is not None):
    credit_principal = args.principal
    count_periods = args.periods
    credit_interest = args.interest
    i = credit_interest / (12 * 100)
    annuity_payments = math.ceil(credit_principal * ((i * (1 + i) ** count_periods) / ((1 + i) ** count_periods - 1)))
    overpayment = annuity_payments * count_periods - credit_principal
    print(f'Your annuity payment = {annuity_payments}')
    print(f'Overpayment = {overpayment}')
    sys.exit()
elif (args.type == 'annuity') and (args.payment is not None) and (args.interest is not None):
    monthly_payment = args.payment
    count_periods = args.periods
    credit_interest = args.interest
    i = credit_interest / (12 * 100)
    credit_principal = monthly_payment / ((i * (1 + i) ** count_periods) / ((1 + i) ** count_periods - 1))
    overpayment = monthly_payment * count_periods - credit_principal
    print(f'Your credit principal = {credit_principal}!')
    print(f'Overpayment = {overpayment}')
    sys.exit()
