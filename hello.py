from flask import Flask
# Mac
# export FLASK_APP=hello.py FLASK_ENV=development flask run
# Windows
# $env: FLASK_APP='hello.py' ; flask run
# uvicorn/gunicorn - production env.

app = Flask(__name__)

@app.route("/") #root is "/"
def hello():
    return "Hello Folx"

@app.route("/tamil")
def hello_in_tamil():
    return "vannakkam!"

@app.route("/name/<name>")
def hello_name(name):
    return f"vannakkam {name}!"


