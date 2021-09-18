from flask import Flask, render_template, request, jsonify, redirect
from mongoapi import MongoAPI

app = Flask(__name__)

data = {'database':'akifruits', 'collection':'tree'}

@app.errorhandler(404)
def not_found(error):
    return '<H1>Página no encontrada</H1>'

@app.route('/')
def index():
    return "<h1>Bienvenido</h1>"

@app.route("/game", methods=['GET','POST'])
def game():
    db = MongoAPI(data)
    if request.method == 'GET':
        # Display root node when request is by get
        response = db.get_root()
        return render_template('game.html', current_node = response)

@app.route("/end", methods=['GET'])
def end():
    return render_template('end.html')

@app.route("/fail/<id>", methods=['GET'])
def fail(id):
    print(id)
    return render_template('fail.html')

@app.route("/next-node", methods=['POST'])
def next_node():
    db = MongoAPI(data)
    current_node = request.form['current_node']
    answer = request.form['answer']

    response = db.get_node(current_node)
    if answer == 'yes':
        son = response['nLeft']
    else: 
        son = response['nRight']
    
    return jsonify({'node': son, 'body': db.get_node(son)})
    


