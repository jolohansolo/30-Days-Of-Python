from datetime import datetime , date
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
s= 'Today is 5 December, 2019'
times = s[8:]
date_object = datetime.strptime(times, "%d %B, %Y")
print(date_object)
new_year = date(year=2026, month=1, day=1)
time_diff = now - new_year
old_date = date(year=1970,month=1,day=1)
date_diff = now - old_date
