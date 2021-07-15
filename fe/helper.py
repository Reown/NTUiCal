def splitall(val):
    valsplit = val.split("\t")
    return valsplit


def getsplits(valsplit):
    cc = []

    j = 0
    for j in range(0, len(valsplit), 14):
        temp = valsplit[j].replace("\r\n", " ").replace("\n", " ")
        cc.append(temp.split(" "))

    course = []
    weeks = []

    k = 0
    for k in range(len(cc)):
        if(k == 0):
            course.append(cc[k][0])

        else:
            if(len(cc[k]) > 3):
                course.append(cc[k][2])
                weeks.append(cc[k][1])

            else:
                course.append("")
                weeks.append(cc[k][1])
                
    course.pop()

    title = []
    ctype = []
    group = []
    day = []
    time = []
    venue = []

    k = 0
    for k in range(1, len(valsplit), 14):
        title.append(valsplit[k])
        ctype.append(valsplit[k+8])
        group.append(valsplit[k+9])
        day.append(valsplit[k+10])
        time.append(valsplit[k+11])
        venue.append(valsplit[k+12])

    return course, title, ctype, group, day, time, venue, weeks


def cleantime(time):
    timestart = []
    timeend = []

    k = 0
    for k in range(len(time)):
        starttemp1 = time[k][0] + time[k][1]
        starttemp2 = time[k][2] + time[k][3]
        timestart.append([starttemp1, starttemp2])
        
        endtemp1 = time[k][5] + time[k][6]
        endtemp2 = time[k][7] + time[k][8]
        timeend.append([endtemp1, endtemp2])

    return timestart, timeend


def cleanweeks(weeks):
    allweeks = []

    k = 0
    for k in range(len(weeks)):
        if "," in(weeks[k][2:]):
            temp = weeks[k][2:].split(",")
            allweeks.append(temp)
    
        elif "-" in(weeks[k][2:]):
            temp = weeks[k][2:].split("-")
            temp1 = int(temp[0])
            temp2 = int(temp[1])
            temp = list(range(temp1, temp2+1))
            allweeks.append(temp)

        else:
            temp = weeks[k][2:]
            allweeks.append([temp])

    return allweeks


def intday(day):
    return {
        "MON ": 0,
        "TUE ": 1,
        "WED ": 2,
        "THU ": 3,
        "FRI ": 4,
        "SAT ": 5
    }.get(day, "invalid")


def cleanday(day):
    utilday = []

    j = 0
    for j in range(len(day)):
        utilday.append(intday(day[j]))

    return utilday


def checkdel(weeks):
    exclude = ["", "course"]
    exc1, exc2 = exclude
    topop = []

    j = 0
    for j in range(len(weeks)):
        if (weeks[j] == exc1) or (weeks[j] == exc2):
            topop.append(j)

    topop.sort(reverse = True)
    
    return topop


def popall(course, title, ctype, group, day, time, venue, weeks, topop):
    i = 0
    for i in range(len(topop)):
        course.pop(topop[i])
        title.pop(topop[i])
        ctype.pop(topop[i])
        group.pop(topop[i])
        day.pop(topop[i])
        time.pop(topop[i])
        venue.pop(topop[i])
        weeks.pop(topop[i])

    return course, title, ctype, group, day, time, venue, weeks