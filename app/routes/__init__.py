from flask import Blueprint

def init_app(app):
    from .main import main
    from .auth import auth
    from .dashboard import dashboard
    from .llm import llm
    from .learning_path import learning_path

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(llm)
    app.register_blueprint(learning_path)