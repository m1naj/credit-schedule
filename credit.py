from datetime import datetime, timedelta, date
from pprint import pprint
from tabulate import tabulate

def calculate_next_month(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    next_month = date_obj + timedelta(days=31)
    return next_month.strftime("%Y-%m-%d")

def calculate_monthly_payment(amount, percent, period, i):
    monthly_payment = (amount / period) + ((amount - (amount / period) * (i - 1)) / 100) * (percent / 12)
    return monthly_payment

def calculate_loan(amount, percent, period):
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    if not isinstance(percent, (int, float)):
        raise ValueError("Percent must be a number")
    if not isinstance(period, int):
        raise ValueError("Period must be an integer")
    
    if amount <= 0:
        raise ValueError("Amount must be a positive number")
    if percent <= 0:
        raise ValueError("Percent must be a positive number")
    if period <= 0:
        raise ValueError("Period must be a positive number")

    today = date.today()
    timetoday = today.strftime('%Y-%m-%d')

    payment_schedule = []
    total_payment = 0

    for i in range(1, period+1):
        monthly_payment = calculate_monthly_payment(amount, percent, period, i)
        payment_schedule.append([calculate_next_month(timetoday), round(monthly_payment, 2)])
        total_payment += monthly_payment
        timetoday = calculate_next_month(timetoday)

    overpayment = total_payment - amount
    return payment_schedule, round(overpayment, 2)

amount = 100000
percent = 12
period = 12

payment_schedule, overpayment = calculate_loan(amount, percent, period)
print("Таблица выплат \n")
print(tabulate(payment_schedule, headers=["Дата", "Месячный платеж"], tablefmt="grid"))
print("Переплата по кредиту: ", overpayment)