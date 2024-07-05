import os

class Config:
    ### Untuk Lokal
    from dotenv import load_dotenv

    # Load environment variables from a .env file
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}"

    ### Untuk Deployment
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@127.0.0.1:5432/{os.environ.get('DB_NAME')}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
