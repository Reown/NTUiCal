def splitall(val):
    valsplit = val.split("\t")
    return valsplit


def getsplits(valsplit):
    cc = []

    j = 0
    for j in range(0, len(valsplit), 14):
        temp = valsplit[j].replace("\n", " ")
        cc.append(temp.split(" "))

    course = []
    weeks = []

    k = 0
    for k in range(0, len(cc), 1):
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
    for k in range(0, len(time), 1):
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
    for k in range(0, len(weeks), 1):
        if "," in(weeks[k][2:]):
            temp = weeks[k][2:].split(",")
            allweeks.append(temp)
    
        elif "-" in(weeks[k][2:]):
            temp = weeks[k][2:].split("-")
            allweeks.append(temp)

        else:
            allweeks.append(temp)

    return allweeks