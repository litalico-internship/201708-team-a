from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/oshietai', methods=['POST'])
def oshietai():
    if request.method == 'POST':
        item_ids = request.form.getlist('teach_cat')
        item_ids = list(map(int, item_ids))
        print(item_ids)

        # 教えたい側のdbから対応するユーザーidをとってくる
        db.register(item_ids)
        # 別のページに移動
        return redirect(url_for('thanks'))

    return render_template("checkbox.html", items=db.get_items())

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/siritai', methods=['POST'])
def siritai():
    if request.method == 'POST':
        item_ids = request.form['learn_cat']
        print(item_ids)

        # 教えたい側のdbから対応するユーザーidをとってくる
        user_ids = db.get_uids(item_ids)
        # 別のページに移動＋ユーザーidを渡す
        return render_template('result.html', user_ids=user_ids)

    return render_template("siritai.html", items=db.get_items())

@app.route('/result')
def result():
    return render_template('result.html')

<<<<<<< HEAD
@app.route('/oshietai')
def oshietai():
    return render_template('checkbox.html')

@app.route('/thanks')
def thanks():
    return render_template('thx.html')

=======
>>>>>>> origin/master

if __name__ == '__main__':
    app.run(debug=True)
