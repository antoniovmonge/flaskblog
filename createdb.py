from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Config
from run import app

db = SQLAlchemy(app)

db.create_all()