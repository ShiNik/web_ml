from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

# create an application:
def create_app():
    global app
    app = Flask(__name__)
    UPLOAD_FOLDER = './flask_package/static/upload_db/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    ALLOWED_EXTENSIONS = {'csv'}
    app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/upload_db/filestorage.db'

    global db
    db = SQLAlchemy(app)
    db.init_app(app)
    from flask_package.database import FileContents
    db.create_all()

    from flask_package import routes

    return app
