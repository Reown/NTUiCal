import os
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def parse():
    testdata = request.form['sourcetxt']
    getdate = datetime.strptime(request.form['getdate'], '%Y-%m-%d')
    return render_template('index.html', data=testdata, data2=getdate.date())

@app.route('/cal')
def calview():
    return render_template('calview.html')
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, port=port)