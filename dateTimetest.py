from datetime import datetime

# datetime(year, month, day, hour, minute, second)
a = datetime(2017, 6, 21, 18, 25, 30)
b = datetime(2017, 6, 21, 8, 25, 30)

# returns a timedelta object
c = a-b
print('Difference: ', c)

minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)

# returns the difference of the time of the day
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)
