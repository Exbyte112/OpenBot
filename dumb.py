# importing datetime module
from datetime import datetime
import pytz

# assigned regular string date
tyme = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
Year = datetime.now().strftime("%Y")
Year = int(Year)
Month = datetime.now().strftime("%m")
Month = int(Month)
Day = datetime.now().strftime("%d")
Day = int(Day)
h = datetime.now().strftime("%H")
h = int(h)
m = datetime.now().strftime("%M")
m = int(m)
s = datetime.now().strftime("%S")
s = int(s)

#print(Month)
#print(tyme)
# displaying unix timestamp after conversion

timezones = pytz.all_timezones
#print(timezones)