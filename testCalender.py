import time
start_time = time.time();
from calendar import TextCalendar

year = int(input("Enter the year: "))
cal = TextCalendar()
print(cal.formatyear(year , 2,1,8,3));

print("--- %s seconds ---" % (time.time() - start_time));