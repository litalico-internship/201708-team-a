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

#登録
def register(itemIds):
    with connection.cursor() as cursor:
        sql = "INSERT INTO user (id, tag) VALUES (%s, %s)"
        for i in itemIds:
            r = cursor.execute(sql, (id_num, itemIds))
        # autocommitではないので、明示的にコミットする
        connection.commit()

#教えたい側のid引っ張る
def get_uids(itemId):
    with connection.cursor() as cursor:
        sql = "SELECT id FROM user_teaching_item WHERE tag == %s"
        cursor.execute(sql, itemId)

        # Select結果を取り出す
        results = cursor.fetchall()
        return results

'''
@app.route('/oshietai')
def oshietai():
    return render_template('checkbox.html')
'''

@app.route('/oshietai', methods=['GET','POST'])
def oshietai():
    print(request.method)
    if request.method == 'POST':
        itemIds = request.form['fav']
        print(itemIds)

        # 教えたい側のdbから対応するユーザーidをとってくる
        register(itemIds)
        # 別のページに移動
        return page

    return render_template("checkbox.html")

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

'''
@app.route('/siritai')
def siritai():
    return render_template('siritai.html')
'''

@app.route('/siritai', methods=['GET','POST'])
def siritai():
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
