# dates
from datetime import date, timedelta

today = date.today()
print(today)

formatted_date = today.strftime("%d/%m/%Y")
print(formatted_date)

after_forty_days  = today + timedelta(days=40)
print(after_forty_days)