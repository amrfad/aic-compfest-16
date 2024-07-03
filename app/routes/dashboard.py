from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def dash():
    return render_template('user/dashboard.html')