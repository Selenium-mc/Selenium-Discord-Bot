from flask import Flask, send_from_directory, render_template
from threading import Thread
import json
import os


app = Flask("SeleniumBot", template_folder="flask/templates")
app.config['UPLOAD_FOLDER'] = "files/videos/"


@app.route("/")
def index():
    return render_template("index.html", videos=os.listdir("files/videos/"))


@app.route("/backup/<id>")
@app.route("/backup/<id>.json")
def getrules(id):
    try:
        with open(f"data/backups/{id}.json") as f:
            return "<pre>"+f.read()+"</pre>"
    except FileNotFoundError:
        return "<pre>User has no backups</pre>"
    else:
        return "<pre>Unknown error</pre>"


@app.route('/video/<file>')
def returnfile(file):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], file)
    except:
        return f"<pre>File '{file}' not found</pre>"


def run():
    app.run(host="0.0.0.0", port=8080)

def start():
    server = Thread(target=run)
    server.start()
