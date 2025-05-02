from flask import Flask
from infrastructure.init_db import db_uri
from extensions import db
from routes.notes import note_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db.init_app(app)

app.register_blueprint(note_bp, url_prefix="/api")

@app.route("/")
def hello():
    return "Hello, world"