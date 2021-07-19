from datetime import datetime
from flask import Flask, render_template, request, send_file, send_from_directory
from vibe import *
from genjson import *

app = Flask(__name__)

icspath = "my.ics"
jsonpath = "my.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cal')
def calview():
    return render_template('calview.html')

@app.route('/cal', methods = ['POST'])
def parse():
    getdate = request.form['getdate2']
    getsource = request.form['sourcetxt']
    
    ss = datetime.datetime.strptime(getdate, '%d/%m/%Y')
    weekbef = minusweek(ss)

    valsplit = splitraw(getsource)
    course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = splitfunc(valsplit)
    ical = p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks)
    
    if((len(valsplit) - 1) % 14 != 0 or len(valsplit) == 1):
        return "exception", 500

    with open(icspath, 'w') as my_file:
        my_file.writelines(ical)

    output_file = valid_check(icspath)
    calendar_data = read_file(icspath)
    vevents = get_events(calendar_data)
    save_json(vevents, output_file)

    return render_template('calview.html')

@app.route('/cal/download', methods = ['POST'])
def download():
    return send_file(icspath, as_attachment=True)
    #return send_from_directory("static", "events.json")

@app.route('/data')
def return_data():
    with open(jsonpath, "r") as input_data:
        return input_data.read()

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

if __name__ == '__main__':
  app.run(debug=True)