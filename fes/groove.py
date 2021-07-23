import os
import sys
import json
from icalendar import Calendar


def valid_check(param):
    base, ext = os.path.splitext(param)
    if ext.lower() != (".ics"):
        print("This script only works for '.ics' format")
        exit(1)

    else:
        output_file = base + ".json"
        return output_file


def read_file(path):
    print("Reading source from '" + path + "'")
    with open(path, "r") as i_f:
        calendar_data = Calendar.from_ical(i_f.read())

    return calendar_data


def get_colour(course_list, summary):
    colour_list = ["maroon", "olive", "green", "teal", "navy", "purple", "#5C3317", "#838996", "#413839"]

    k = 0
    for k in range(len(course_list)):
        if summary == course_list[k]:
            return colour_list[k]

    return ""
    

def get_events(course_list, calendar_data):
    vevents = []

    for component in calendar_data.walk():
        if component.name == "VEVENT":
            temp = {
                "title": component.get('summary'),
                "start": component.decoded('dtstart').isoformat(),
                "end": component.decoded('dtend').isoformat(),
                "location": component.get('location'),
                "description": component.get('description'),
                "color": get_colour(course_list, component.get('summary'))
            }
            vevents.append(temp)

    return vevents


def save_json(vevents, output_file):
    print("Saving json at '" + output_file + "'")
    with open(output_file, "w") as o_f:
        json.dump(vevents, o_f, indent = 4)


def get_course(course_list):
    course_list = list(filter(None, course_list))
    return course_list


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Invalid Arguments")
        exit(1)
    
    output_file = valid_check(sys.argv[1])
    calendar_data = read_file(sys.argv[1])
    course_list = ["placeholder"]
    vevents = get_events(course_list, calendar_data)
    save_json(vevents, output_file)