from flask import Blueprint, render_template

llm = Blueprint('llm', __name__)

@llm.route('/chat')
def chat():
    return render_template('user/chat.html')