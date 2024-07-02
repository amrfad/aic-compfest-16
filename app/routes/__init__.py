from flask import Blueprint
from .main import main
from .auth import auth
# from .dashboard import dashboard
# from .chat import chat
# from .learning_path import learning_path

def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(auth)
    # app.register_blueprint(dashboard)
    # app.register_blueprint(chat)
    # app.register_blueprint(learning_path)