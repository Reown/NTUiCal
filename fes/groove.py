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


def get_events(calendar_data):
    vevents = []

    for component in calendar_data.walk():
        if component.name == "VEVENT":
            temp = {
                "title": component.get('summary'),
                "start": component.decoded('dtstart').isoformat(),
                "end": component.decoded('dtend').isoformat(),
                "location": component.get('location'),
                "description": component.get('description')
            }
            vevents.append(temp)

    return vevents


def save_json(vevents, output_file):
    print("Saving json at '" + output_file + "'")
    with open(output_file, "w") as o_f:
        json.dump(vevents, o_f, indent = 4)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Invalid Arguments")
        exit(1)
    
    output_file = valid_check(sys.argv[1])
    calendar_data = read_file(sys.argv[1])
    vevents = get_events(calendar_data)
    save_json(vevents, output_file)