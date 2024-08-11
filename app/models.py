from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import JSON

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(128))
    password_hash = db.Column(db.String(255))
    
    # Kolom baru untuk menyimpan data JSON
    skills = db.Column(JSON)
    learning_path = db.Column(JSON)
    job_recommendations = db.Column(JSON)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def update_skills(self, skills_data):
    #     self.skills = skills_data

    # def update_learning_path(self, path_data):
    #     self.learning_path = path_data

    # def update_job_recommendations(self, job_data):
    #     self.job_recommendations = job_data