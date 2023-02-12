import sqlalchemy.exc
from flask import Blueprint, jsonify, render_template, request, Response
from data import db_session
from data.model import Model
from flask import Flask, abort, send_from_directory
from sqlalchemy.sql import text
import random

Server = 'localhost'
Port = 8080



db_session.global_init("db/data.db")

users_blueprint = Blueprint(
    'hahaprof_app_api',
    __name__
)

@users_blueprint.route('/api/get_all_models', methods=['GET'])
def get_all_models():
    session = db_session.create_session()
    models = session.query(Model).values(Model.name, Model.id)
    d = {}
    for name, id in models:
        d[name] = id
    return jsonify(d)


@users_blueprint.route('/api/get_model/<int:id>', methods=['GET'])
def get_model(id):
    session = db_session.create_session()
    try:
        filename = session.query(Model).filter(Model.id == id).one().file
    except sqlalchemy.exc.NoResultFound:
        return 'Model not found', 400

    print(filename)

    try:
        return send_from_directory(app.config['models_dir'], filename)
    except FileNotFoundError:
        abort(401)



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['models_dir'] = '/Users/egorurov/PycharmProjects/backend/models'

if __name__ == '__main__':
    app.register_blueprint(users_blueprint)
    app.run(Server, Port)