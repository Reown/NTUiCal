import datetime
import os
import sys
from ics import Calendar, Event
from dateutil.relativedelta import *
from helper import *
from scrap import fh

def minusweek(startofclass):
    weekbef = startofclass+relativedelta(weeks=-1)
    return weekbef


def splitraw(val):
    valsplit = splitall(val)
    return valsplit


def splitfunc(valsplit):
    course, title, ctype, group, day, time, venue, weeks = getsplits(valsplit)
    topop = checkdel(weeks)
    course, title, ctype, group, day, time, venue, weeks = popall(course, title, ctype, group, day, time, venue, weeks, topop)
    timestart, timeend = cleantime(time)
    allweeks = cleanweeks(weeks)
    title, ctype, group, day, venue = white(title, ctype, group, day, venue)
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


def save_ics(ical, out_file):
    with open(out_file, 'w') as my_file:
        my_file.writelines(ical)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Invalid Arguments")
        exit(1)

    base, ext = os.path.splitext(sys.argv[1])
    if (ext.lower() != (".txt") and ext.lower() != (".html")):
        print(ext.lower())
        print("Path to .txt or .html")
        exit(1)
    
    else:
        out_file = base + ".ics"

    try:
        s = sys.argv[2]
        startofclass = datetime.datetime.strptime(s, '%d%m%Y')
        weekbef = minusweek(startofclass)

    except:
        print("Follow the 'DDMMYYYY' format")
        exit(1)

    if ext.lower() == (".txt"):
        with open(sys.argv[1], "r") as myfile:
             val = myfile.read()

        valsplit = splitraw(val)
        course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = splitfunc(valsplit)
        ical = p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks)

    elif ext.lower() == (".html"):
        course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = fh(sys.argv[1])
        ical = p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks)
        
    save_ics(ical, out_file)

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

