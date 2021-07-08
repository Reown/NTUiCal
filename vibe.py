import numpy
import re
import datetime
from ics import Calendar, Event
from dateutil.relativedelta import *
from helper import *


def p2cal(c):
    i=0
    for i in range()):

        e = Event()

        e.name = "course"
        e.begin = '2021-07-0' + str(i) + '00:00:00'
        e.end = '2021-07-0' + str(i) + '01:00:00'
        e.location = 'venue'
        e.description = 'title\nctype group'

        c.events.add(e)
        c.events

    return c


with open("sample.txt", "r") as myfile:
    val = myfile.read()

valsplit = splitall(val)
course, title, ctype, group, day, time, venue, weeks = getsplits(valsplit)
timestart, timeend = cleantime(time)
allweeks = cleanweeks(weeks)

c = Calendar()
ical = p2cal(c)

with open('my.ics', 'w') as my_file:
    my_file.writelines(ical)




'''
print(course)
print(title)
print(ctype)
print(group)
print(day)
print(timestart)
print(timeend)
print(venue)
print(allweeks)
'''



#s = input("First day of class (DDMMYYYY): ")
#s = "09082021"
#startofclass = datetime.datetime.strptime(s, '%d%m%Y')

#print(startofclass.date())

