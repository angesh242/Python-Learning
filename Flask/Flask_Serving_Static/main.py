#use--https://flask.palletsprojects.com/en/stable/quickstart/
#use--https://getbootstrap.com/docs/5.3/
#Access the files directly

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
app.run(port=8000, debug=True)