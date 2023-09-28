import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, send_file, send_from_directory, session
from vibe import *
from groove import *
from scrap import fh

app = Flask(__name__)
#app.secret_key = "onprod" #local
app.secret_key = os.getenv('SECRET_KEY', 'onprod') #heroku

@app.route('/')
def index():
    if session.get('uid') is None:
        session['uid']=uuid.uuid4()
    return render_template('index.html')

@app.route('/cal')
def calview():
    return render_template('calview.html')

@app.route('/cal', methods = ['POST'])
def parse():
    ufile = request.files['file']
    if ufile and ufile.filename.endswith('.html'):
        course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = fh(ufile)
        
    else:
        getsource = request.form['sourcetxt']
        valsplit = splitraw(getsource)
        if((len(valsplit) - 1) % 14 != 0 or len(valsplit) == 1):
            return "exception", 500

        course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = splitfunc(valsplit)

    getdate = request.form['getdate2']
    ss = datetime.datetime.strptime(getdate, '%d/%m/%Y')
    weekbef = minusweek(ss)

    ical = p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks)
    
    #icspath = (str(session['uid']).split("-"))[0] + ".ics" #local
    icspath = "/tmp/" + (str(session['uid']).split("-"))[0] + ".ics" #heroku

    with open(icspath, 'w') as my_file:
        my_file.writelines(ical)

    output_file = valid_check(icspath)
    calendar_data = read_file(icspath)
    course_list = get_course(course)
    vevents = get_events(course_list, calendar_data)
    save_json(vevents, output_file)

    return render_template('calview.html')

@app.route('/cal/download', methods = ['POST'])
def download():
    #icspath = (str(session['uid']).split("-"))[0] + ".ics" #local
    icspath = "/tmp/" + (str(session['uid']).split("-"))[0] + ".ics" #heroku
    return send_file(icspath, as_attachment=True)
    #return send_from_directory("static", "events.json")

@app.route('/data')
def return_data():
    #jsonpath = (str(session['uid']).split("-"))[0] + ".json" #local
    jsonpath = "/tmp/" + (str(session['uid']).split("-"))[0] + ".json" #heroku
    with open(jsonpath, "r") as input_data:
        return input_data.read()

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

if __name__ == '__main__':
  app.run(debug=True)