import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
from models import db

load_dotenv()
PATH = os.path.abspath('instance')

app = Flask(__name__, instance_path=PATH)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)
Migrate(app, db)
jwt = JWTManager(app)
CORS(app)


@app.route('/')
def main():
    return jsonify({"message": "Server running successfully!"}), 200

if __name__=='__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port = 5000
    )