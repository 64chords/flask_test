from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap

import numpy as np
import pandas as pd
import json
import plotly


#自信の名称をappという名前でインスタンス化する
app = Flask(__name__)
boot_strap = Bootstrap(app)

def pickup():
    messages = [
        "hello",
        "good",
        "excelent"
    ]
    return np.random.choice(messages)

def gen_graph():
    rng = pd.date_range('1/1/2011', periods=7500, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    graphs = [
        dict(
            data=[
                dict(
                    x=[1,2,3],
                    y=[10,20,30],
                    type="scatter"
                ),
            ],
            layout=dict(
                title="first graph"
            )
        ),

        dict(
            data=[
                dict(
                    x=[1,3,5],
                    y=[10,50,30],
                    type="bar"
                ),
            ],
            layout=dict(
                title="second graph"
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,
                    y=ts
                )
            ]
        )
    ]
    return graphs

@app.route("/")
def index():
    title = "ようこそ"
    # 表示するメッセージの取得
    message = pickup()
    # 描画データ
    graphs = gen_graph()
    # idsの追加
    ids = ["graph-{}".format(i) for i,_ in enumerate(graphs)]
    # figureをJsonへ変換 pandas,datetime,etc objectsを変換できる
    graphJSON = json.dumps(graphs,cls=plotly.utils.PlotlyJSONEncoder)

    # index.htmlのレンダリング
    return render_template(
        "index.html",
        message=message,
        title=title,
        ids=ids,
        graphJSON=graphJSON
    )

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
