from flask import Blueprint, render_template

learning_path = Blueprint('learning_path', __name__)

@learning_path.route('/learning-path')
def path():
    return render_template('user/learning_path.html')