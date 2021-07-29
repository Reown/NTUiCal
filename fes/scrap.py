import codecs
from bs4 import BeautifulSoup
from helper import *

def fh(path):

    raw_html = codecs.open(path, 'r').read()
    soup = BeautifulSoup(raw_html, features="html.parser")

    table = soup.find("table", attrs={"border": ""})
    table_data = table.tbody.find_all("tr")

    course = []
    title = []
    ctype = []
    group = []
    day = []
    time = []
    venue = []
    weeks = []

    for i in range(1, len(table_data)):

        temprow = []
        for td in table_data[i].find_all("td"):
            temprow.append(td.text.replace('\n', ' ').strip())

        course.append(temprow[0])
        title.append(temprow[1])
        ctype.append(temprow[9])
        group.append(temprow[10])
        day.append(temprow[11])
        time.append(temprow[12])
        venue.append(temprow[13])
        weeks.append(temprow[14].split(" ")[1])

    topop = checkdel(weeks)
    course, title, ctype, group, day, time, venue, weeks = popall(course, title, ctype, group, day, time, venue, weeks, topop)
    timestart, timeend = cleantime(time)
    allweeks = cleanweeks(weeks)
    utilday = cleanday(day)

    return course, title, ctype, group, utilday, timestart, timeend, venue, allweeks