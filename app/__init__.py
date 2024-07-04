from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.secret_key = 'super_secret_key'
    app.config.from_object(Config)
    
    db.init_app(app)
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_view = 'auth.login'

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))
    
    from .routes import init_app as init_routes
    init_routes(app)
    
    return app