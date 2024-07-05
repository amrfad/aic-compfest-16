# import os
# from dotenv import load_dotenv

# # Load environment variables from a .env file
# load_dotenv()
import os

username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASS')
database = os.environ.get('DB_NAME')

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@127.0.0.1:5432/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
