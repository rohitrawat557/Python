import datetime

date = datetime.date(2024, 6, 1)
today = datetime.date.today()

time = datetime.time(14, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%y")

target_date = datetime.datetime(2020,1,2,12,30,1)
current_date = datetime.datetime.now()

if target_date < current_date:
    print("The target date has already passed")