import datetime
from dumb import h, m, s, Year, Month, Day
import time

t_epoch = time.time()
print(f"The epoch time is now: {t_epoch}")
ts = datetime.datetime(Year, Month, Day,h, m, s).timestamp()
#print(ts)
#print(type(ts))
print("ready")