from flask import Flask,render_template,request,redirect,url_for,flash
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap

import os
import numpy as np
import pandas as pd
import json
import plotly

from data_generator import cwt

UPLOAD_FOLDER = "./uploads/"
SECRET_KEY = "secret key"
ALLOWED_EXTENSIONS = set(['csv'])

#自信の名称をappという名前でインスタンス化する
app = Flask(__name__)
boot_strap = Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_csv(file):
    df = pd.read_csv(file)
    time = np.array(df.iloc[:,0])
    time_val = np.array(df.iloc[:,1])
    return time,time_val

def gen_graph(time,time_val,freqs,wav_val):
    """グラフオブジェクトの生成"""
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
    # [os.remove(os.path.join(app.config['UPLOAD_FOLDER'],file_)) for file_ in os.listdir(app.config['UPLOAD_FOLDER'] )]
    title = "wavelet transformer"
    # index.htmlのレンダリング
    return render_template(
        "index.html",
        title=title,
        body_message=True
    )

@app.route("/post",methods=["GET","POST"])
def post():
    title="PostTest"
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part","add-file")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == "":
            flash("No selected file","add-file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # save file
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            # load saved file
            time,time_val = load_csv(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            # cwt
            freqs,wav_val = cwt(time,time_val)
            # gen graphJSON
            graphs = gen_graph(time,time_val,freqs,wav_val)
            graphJSON = json.dumps(graphs,cls=plotly.utils.PlotlyJSONEncoder)
            return render_template(
                "index.html",
                title="wct",
                filename=filename,
                graphJSON=graphJSON
            )
        else:
            flash("only csv file is allowed","add-file")
            return redirect(request.url)
    else:
        return redirect(url_for("index"))

@app.route("/params",methods=["GET","POST"])
def params():
    if request.method == "POST":
        import pdb; pdb.set_trace()
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
