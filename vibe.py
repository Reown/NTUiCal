import numpy
import re
import datetime
from ics import Calendar, Event
from dateutil.relativedelta import *
from helper import *


def splitfunc(val):
    valsplit = splitall(val)
    course, title, ctype, group, day, time, venue, weeks = getsplits(valsplit)
    topop = checkdel(weeks)
    course, title, ctype, group, day, time, venue, weeks = popall(course, title, ctype, group, day, time, venue, weeks, topop)
    timestart, timeend = cleantime(time)
    allweeks = cleanweeks(weeks)
    utilday = cleanday(day)

    return course, title, ctype, group, utilday, timestart, timeend, venue, allweeks


def p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks):
    c = Calendar()

    i = 0
    for i in range(len(allweeks)):

        t = i
        while(course[t] == ""):
            t = t - 1

        n = 0
        for n in range(len(allweeks[i])):
            if(int(allweeks[i][n]) > 7):
                weekstoadd = int(allweeks[i][n]) + 1
            else:
                weekstoadd = int(allweeks[i][n])

            e = Event()

            e.begin = str((weekbef+relativedelta(weeks =+ weekstoadd, weekday = utilday[i])).date()) + " " + str(format(int(timestart[i][0]) - 8, '02d')) + ":" + timestart[i][1] + ":00"
            e.end = str((weekbef+relativedelta(weeks =+ weekstoadd, weekday = utilday[i])).date()) + " " + str(format(int(timeend[i][0]) - 8, '02d')) + ":" + timeend[i][1] + ":00"
            #e.begin = '2021-07-01 00:00:00'
            #e.end = '2021-07-01 01:00:00'
            e.name = course[t]
            e.location = venue[i]
            e.description = title[t] + "\n" + ctype[i] + "\t" + group[i]

            c.events.add(e)
            c.events

    return c


if __name__ == "__main__":
    #s = input("First day of class (DDMMYYYY): ")
    s = "09082021"
    startofclass = datetime.datetime.strptime(s, '%d%m%Y')
    weekbef = startofclass+relativedelta(weeks=-1)

    with open("sample.txt", "r") as myfile:
        val = myfile.read()

    course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = splitfunc(val)

    ical = p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks)

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