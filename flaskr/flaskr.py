from flask import Flask,render_template,request,redirect,url_for
import numpy as np

#自信の名称をappという名前でインスタンス化する
app = Flask(__name__)

def pickup():
    messages = [
        "hello",
        "good",
        "excelent"
    ]
    return np.random.choice(messages)

@app.route("/")
def index():
    title = "ようこそ"
    message = pickup()
    # index.htmlのレンダリング
    return render_template("index.html",message=message,title=title)

@app.route("/post",methods=["GET","POST"])
def post():
    title="こんにちは"
    if request.method == "POST":
        #リクエストフォームから名前を取得
        name = request.form["name"]
        return render_template("index.html",name=name,title=title)
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
