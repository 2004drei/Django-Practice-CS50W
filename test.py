from datetime import datetime, date, timedelta

now = datetime.now()

if now.month == 12 and now.day == 25:
  print(True)
else:
  print(False)