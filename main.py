from flask import Flask, render_template


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return '<H1>Página no encontrada</H1>'


@app.route("/")
def index():
    return render_template('index.html')
