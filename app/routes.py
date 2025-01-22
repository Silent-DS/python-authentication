from flask import render_template
from flask_login import login_required
from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')