import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
