from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap

import numpy as np
import pandas as pd
import json
import plotly

from data_generator import generate_data


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
    """グラフオブジェクトの生成"""
    time,time_val,freqs,wav_val = generate_data()

    graphs = dict(
        data=[
            dict(
                x=time,
                y=time_val,
                yaxis="y2",
                type="line"
            ),
            dict(
                x=time,
                y=freqs,
                z=wav_val,
                colorscale='Electric',
                type="heatmap"
            )
        ],
        layout=dict(
            height=800,
            xaxis=dict(
                title="time[s]",
                range=np.array([0,30]),
                rangeslider=dict()
            ),
            yaxis2=dict(
                domain=[0.8,1.0],
                title="value"
            ),
            yaxis=dict(
                domain=[0,0.8],
                title="frequency[Hz]"
            )
        )
    )
    return graphs

@app.route("/")
def index():
    title = "ようこそ"
    # 表示するメッセージの取得
    message = pickup()
    # 描画データ
    # graphs = gen_graph()
    # idsの追加
    # ids = ["graph-{}".format(i) for i,_ in enumerate(graphs)]
    # figureをJsonへ変換 pandas,datetime,etc objectsを変換できる
    # graphJSON = json.dumps(graphs,cls=plotly.utils.PlotlyJSONEncoder)

    # index.htmlのレンダリング
    return render_template(
        "index.html",
        message=message,
        title=title
        # ids=ids,
        # graphJSON=graphJSON
    )

@app.route("/post",methods=["GET","POST"])
def post():
    title="PostTest"
    if request.method == "POST":
        #リクエストフォームから名前を取得
        # name = request.form["name"]
        return render_template("index.html",title=title)
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
