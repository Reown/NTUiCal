import numpy
import re
import datetime
from ics import Calendar, Event
from dateutil.relativedelta import *
from helper import *


def p2cal(c, weekbef):
    i = 0
    for i in range(len(allweeks)):

        n = 0
        for n in range(len(allweeks[i])):
            
            e = Event()
            e.name = course[i]
            e.begin = str((weekbef+relativedelta(weeks =+ int(allweeks[i][n]), weekday = utilday[i])).date()) + " " + str(format(int(timestart[i][0]) - 8, '02d')) + ":" + timestart[i][1] + ":00"
            e.end = str((weekbef+relativedelta(weeks =+ int(allweeks[i][n]), weekday = utilday[i])).date()) + " " + str(format(int(timeend[i][0]) - 8, '02d')) + ":" + timeend[i][1] + ":00"
            #e.begin = '2021-07-01 00:00:00'
            #e.end = '2021-07-01 01:00:00'
            e.location = venue[i]
            e.description = title[i] + "\n" + ctype[i] + "\t" + group[i]

            c.events.add(e)
            c.events

    return c


#s = input("First day of class (DDMMYYYY): ")
s = "09082021"
startofclass = datetime.datetime.strptime(s, '%d%m%Y')
weekbef = startofclass+relativedelta(weeks=-1)

with open("sample.txt", "r") as myfile:
    val = myfile.read()

valsplit = splitall(val)
course, title, ctype, group, day, time, venue, weeks = getsplits(valsplit)
topop = checkdel(weeks)
course, title, ctype, group, day, time, venue, weeks = popall(course, title, ctype, group, day, time, venue, weeks, topop)
timestart, timeend = cleantime(time)
allweeks = cleanweeks(weeks)

utilday = []

j = 0
for j in range(len(day)):
    utilday.append(cleanday(day[j]))

c = Calendar()
ical = p2cal(c, weekbef)

with open('my.ics', 'w') as my_file:
    my_file.writelines(ical)


'''
print(course)
print(title)
print(ctype)
print(group)
print(utilday)
print(timestart)
print(timeend)
print(venue)
print(allweeks)
'''

