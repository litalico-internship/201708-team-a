import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/siritai')
def siritai():
    return render_template('siritai.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/oshietai')
def oshietai():
    return render_template('checkbox.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


if __name__ == '__main__':
    app.run(debug=True)
