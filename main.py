from flask import Flask, render_template, request
from mongoapi import MongoAPI

app = Flask(__name__)

data = {'database':'akifruits', 'collection':'test2'}

@app.errorhandler(404)
def not_found(error):
    return '<H1>Página no encontrada</H1>'


@app.route("/")
def index():
    db = MongoAPI(data)
    response = db.get_root()
    return render_template('index.html', nodo = response)
