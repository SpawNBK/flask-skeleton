from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from . import db

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return redirect(url_for('main.profile'))
    # return render_template('profile.html', name=current_user.login)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', events="hello")
