from datetime import datetime
from flask import Flask, render_template, request, send_file, send_from_directory
from vibe import *

app = Flask(__name__)

path = "my.ics"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cal')
def calview():
    return render_template('calview.html')

@app.route('/cal', methods = ['POST'])
def parse():
    testdata = request.form['sourcetxt']
    getdate = request.form['getdate2']

    ss = datetime.datetime.strptime(getdate, '%d/%m/%Y')
    weekbef = minusweek(ss)

    valsplit = splitraw(testdata)
    course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = splitfunc(valsplit)
    ical = p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks)
    
    if((len(valsplit) - 1) % 14 != 0 or len(valsplit) == 1):
        return "exception", 500

    with open(path, 'w') as my_file:
        my_file.writelines(ical)

    return render_template('calview.html', filename=path)
    #return send_file(path, as_attachment=True)

@app.route('/cal/download', methods = ['POST'])
def download():
    return send_file(path, as_attachment=True)

@app.route('/data')
def return_data():
    with open("fe/static/events.json", "r") as input_data:
        return input_data.read()

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

if __name__ == '__main__':
  app.run(debug=True)