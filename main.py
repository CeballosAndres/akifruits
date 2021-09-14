from flask import Flask


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
