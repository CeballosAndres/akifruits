from threading import current_thread
from flask import Flask, json, render_template, request, jsonify, redirect
from mongoapi import MongoAPI

app = Flask(__name__)

data = {'database': 'akifruits', 'collection': 'tree'}


@app.errorhandler(404)
def not_found(error):
    return '<H1>Página no encontrada</H1>'


@app.route('/')
def index():
    return render_template('welcome.html')


@app.route("/game", methods=['GET', 'POST'])
def game():
    db = MongoAPI(data)
    if request.method == 'GET':
        # Display root node when request is by get
        response = db.get_root()
        return render_template('game.html', current_node=response)


@app.route("/end", methods=['GET'])
def end():
    return render_template('end.html')


@app.route("/fail/<id>", methods=['GET', 'POST'])
def fail(id):
    db = MongoAPI(data)
    response = db.get_node(id)
    if request.method == 'POST':
        if request.form['new-fruit'] and request.form['new-fruit-characteristic']:
            dataRight = {'document': response}
            dataLeft = {
                'document':
                {'text': request.form['new-fruit'].lower(),
                 'img': request.form['image-fruit']}
            }

            nLeft = db.write(dataLeft)
            nRight = db.write(dataRight)

            dataFather = {
                'text': request.form['new-fruit-characteristic'].lower(),
                'nLeft': nLeft['Document_ID'],
                'nRight': nRight['Document_ID']
            }

            db.update(id, dataFather)

            return redirect('/end')

    return render_template('fail.html', current_node=response)


@app.route("/next-node", methods=['POST'])
def next_node():
    db = MongoAPI(data)
    current_node = request.form['current_node']
    answer = request.form['answer']

    response = db.get_node(current_node)
    if "nLeft" in response and 'nRight' in response:
        if answer == 'yes':
            son = response['nLeft']
        else:
            son = response['nRight']
        return jsonify({'node': son, 'body': db.get_node(son)})
    else:
        return jsonify({'error': 'Do not have more children'})
