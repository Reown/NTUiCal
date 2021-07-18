import os
import sys
import json
import vobject

def valid_check(param):
    base, ext = os.path.splitext(param)
    if ext.lower() != (".ics"):
        print("This script only works for '.ics' format")
        exit(1)
    else:
        print("Reading source from '" + sys.argv[1] + "'")
        return base

def get_events(vevent):
    print()

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Invalid Arguments")
        exit(1)
    
    base = valid_check(sys.argv[1])
    output_file = base + ".json"
    
    calendar_data = open(sys.argv[1]).read()
    vevents = vobject.readComponents(calendar_data)
    #print(vevents.vevent.summary.valueRepr())
    gg = []
    for cal in vevents:
        for component in cal.components():
            if component.name == "VEVENT":
                #gg.append([component.summary.valueRepr(),component.dtstart.valueRepr(),component.dtend.valueRepr(),component.description.valueRepr()])
                gg.append(component)

    print(gg[0])
    print(len(gg))