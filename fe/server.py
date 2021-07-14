import os
from datetime import datetime
from flask import Flask, render_template, request
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
    course, title, ctype, group, utilday, timestart, timeend, venue, allweeks = splitfunc(testdata)
    ical = p2cal(weekbef, course, title, ctype, group, utilday, timestart, timeend, venue, allweeks)

    with open('my.ics', 'w') as my_file:
        my_file.writelines(ical)
        
    return render_template('index.html', data=testdata, data2=getdate)

@app.route('/cal')
def calview():
    return render_template('calview.html')

if __name__ == '__main__':
  app.run(debug=True)