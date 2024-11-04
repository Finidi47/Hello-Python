# dates
from datetime import date

today = date.today()
print(today)

formatted_date = today.strftime("%d/%m/%Y")
print(formatted_date)