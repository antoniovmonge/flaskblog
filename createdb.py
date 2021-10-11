from flask_sqlalchemy import SQLAlchemy
from flaskblog import create_app

app = create_app()

db = SQLAlchemy(app)

db.create_all()