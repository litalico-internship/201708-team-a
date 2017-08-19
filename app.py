import flask
from flask import render_template, request, redirect, url_for
import mysql.connector

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/oshietai')
def oshietai():
    return render_template('checkbox.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

'''
@app.route('/siritai')
def siritai():
    return render_template('siritai.html')
'''

@app.route('/siritai', methods=['GET','POST'])
def get_data():
    print(request.method)
    if request.method == 'POST':
        itemId = request.form['category']
        print(itemId)

        # 教えたい側のdbから対応するユーザーidをとってくる
        uids = get_uids(itemId)
        # 別のページに移動＋ユーザーidを渡す
        return uids

    return render_template("siritai.html")


if __name__ == '__main__':
    app.run(debug=True)
