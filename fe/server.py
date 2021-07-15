from datetime import datetime
from flask import Flask, render_template, request, send_file
from vibe import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
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

    path = "/tmp/my.ics"

    with open(path, 'w') as my_file:
        my_file.writelines(ical)

    return send_file(path, as_attachment=True)

@app.route('/cal')
def calview():
    return render_template('calview.html')

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

if __name__ == '__main__':
  app.run(debug=True)