from app import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))