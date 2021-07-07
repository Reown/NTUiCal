import numpy
import re
from ics import Calendar, Event

from helper import *

with open("sample.txt", "r") as myfile:
    val = myfile.read()

valsplit = splitall(val)
course, title, ctype, group, day, time, venue, weeks = getsplits(valsplit)
timestart, timeend = cleantime(time)
allweeks = cleanweeks(weeks)

print(course)
print(title)
print(ctype)
print(group)
print(day)
print(timestart)
print(timeend)
print(venue)
print(weeks)
print(allweeks)
