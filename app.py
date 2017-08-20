import flask
from flask import render_template, request, redirect, url_for
import db

app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html',user='listener')

@app.route('/oshietai', methods=['GET','POST'])
def oshietai():
    print(request.method)
    if request.method == 'POST':
        itemIds = request.form.getlist('fav')
        itemIds = list(map(int, itemIds))
        print(itemIds)

        # 教えたい側のdbから対応するユーザーidをとってくる
        db.register(itemIds)
        # 別のページに移動
        return redirect(url_for('thanks'))

    return render_template("checkbox.html", items=db.get_name())

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/siritai', methods=['GET','POST'])
def siritai():
    print(request.method)
    if request.method == 'POST':
        itemId = request.form['category']
        print(itemId)

        # 教えたい側のdbから対応するユーザーidをとってくる
        uids = db.get_uids(itemId)
        # 別のページに移動＋ユーザーidを渡す
        return render_template('result.html', uids=uids)

    return render_template("siritai.html", items=db.get_name())


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
