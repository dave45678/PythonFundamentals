"""
Examples of:
writing to a file
creating HTML calendar
opening web browser with local file
formatting dates
adding days to dates
"""
import os
import calendar
import webbrowser
import datetime


myCal = calendar.HTMLCalendar(calendar.SUNDAY)
myStr = myCal.formatmonth(2015, 10)

#write to a file and open in browser
filename = "myCalendar.html"
f = open(os.path.realpath(filename),'w')
f.write(myStr)
f.close()

#webbrowser.open('file://' + os.path.realpath(filename))

import datetime
print(str(datetime.datetime(2008, 11, 22, 19, 53, 42)))
print( datetime.date.today())
today = datetime.date.today()
#format reference: http://strftime.org/
print(today.strftime('Today is a %A'))
print(today.strftime('%A %B %d %Y'))
print(today.strftime('Today is %A, %B %d %Y'))

from datetime import timedelta
d = datetime.datetime.strptime('2011-03-05','%Y-%m-%d')
print(d)
datetime.datetime(2011, 3, 5, 0, 0)
d.strftime('%Y-%m-%d')
tomorrow = d+timedelta(days=1)
print(tomorrow)
datetime.datetime(2011, 3, 6, 0, 0)
tomorrow.strftime('%Y-%m-%d')
