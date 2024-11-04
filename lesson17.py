# dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

formatted_date = today.strftime("%d/%m/%Y")
print(formatted_date)

after_forty_days  = today + timedelta(days=40)
print(after_forty_days)

dob = '1990-03-27'
# convert to date object
date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
age = today.year - date_of_birth.year
print("I'm ", age, "years old")