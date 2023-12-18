from datetime import datetime, timedelta, date
from pprint import pprint

# Автоматическая дата сегодня
today = date.today()
timetoday = today.strftime('%Y-%m-%d')

amount = input("Введите сумму кредита: ")
while not amount.isdigit():
    print("Некорректный ввод! Введите число.")
    amount = input("Введите сумму кредита: ")
amount = float(amount)

percent = input("Введите процентную ставку: ")
while not percent.isdigit():
    print("Некорректный ввод! Введите число.")
    percent = input("Введите процентную ставку: ")
percent = float(percent)

period = input("Введите период кредитования (в месяцах): ")
while not period.isdigit():
    print("Некорректный ввод! Введите число.")
    period = input("Введите период кредитования (в месяцах): ")
period = int(period)

#дата вручную
# timetoday = str(input("Введите дату начала (ГГГГ-ММ-ДД): "))


def calculate_next_month(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    next_month = date_obj + timedelta(days=31)

    return next_month.strftime("%Y-%m-%d")

def calculate_monthly_payment(amount, percent, period, i):
    monthly_payment = (amount / period) + ((amount - (amount / period) * (i - 1)) / 100) * (percent / 12)
    
    return monthly_payment

payment_schedule = {}
total_payment = 0

for i in range(1, period+1):
    monthly_payment = calculate_monthly_payment(amount, percent, period, i)
    payment_schedule[calculate_next_month(timetoday)] = monthly_payment
    total_payment += monthly_payment
    timetoday = calculate_next_month(timetoday)

overpayment = total_payment - amount
K = 1
res = {key : round(payment_schedule[key], K) for key in payment_schedule}
print("\nГрафик платы по кредиту: \n")
pprint(str(res), width = 30)
print("\nПереплата по кредиту составит:", round(overpayment))
