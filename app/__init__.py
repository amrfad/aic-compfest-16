from flask import Flask
from .routes import init_app as init_routes

def create_app():
    app = Flask(__name__, template_folder='../templates')
    
    # # Konfigurasi aplikasi
    # app.config['SECRET_KEY'] = 'your_secret_key_here'
    
    # Inisialisasi routes
    init_routes(app)
    
    return app