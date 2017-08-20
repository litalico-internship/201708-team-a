from flask import Flask, render_template, request, redirect, url_for
import db
from firebase import firebase
firebase = firebase.FirebaseApplication("https://itayatest.firebaseio.com", None)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    counselor_flag = request.args.get('counselor_flag')
    if counselor_flag == 'true':
        user_type = 'counselor'
        firebase.put('', 'rooms/room1/caller', 'in')
    else:
        user_type = 'listener'

    return render_template('chat.html',user=user_type)

@app.route('/oshietai', methods=['GET','POST'])
def oshietai():
    if request.method == 'POST':
        item_ids = request.form.getlist('teach_cat')
        item_ids = list(map(int, item_ids))
        print(item_ids)

        # 教えたい側のdbから対応するユーザーidをとってくる
        uid = db.register(item_ids)
        # 別のページに移動
        return render_template('thanks.html', user_id=uid)

    return render_template("checkbox.html", items=db.get_items())

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/siritai', methods=['GET','POST'])
def siritai():
    if request.method == 'POST':
        item_id = request.form['learn_cat']
        print(item_id)

        # 教えたい側のdbから対応するユーザーidをとってくる
        user_ids = db.get_uids(item_id)
        # 別のページに移動＋ユーザーidを渡す

        print(user_ids)

        item_name = db.get_item_name(item_id)

        for user_id in user_ids:
            print(user_id)
            firebase.put('', 'counselors/' + str(user_id), {'tag': item_name})

        firebase.put('', 'rooms/room1/', {'tag': item_name, 'caller': None, 'listener': 'in', 'chats': None})

        return render_template('chat.html')

    return render_template("siritai.html", items=db.get_items())


@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
