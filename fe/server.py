from flask import Flask, render_template, request
app = Flask(__name__)

data="sdnaosd"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/parse/")
def parse():
    print("clickme")
    return render_template('index.html', data=data)



if __name__ == '__main__':
  app.run(debug=True)