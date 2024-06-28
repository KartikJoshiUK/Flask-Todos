from flask import Blueprint, request, url_for, redirect
from flask_login import login_user, login_required, logout_user
from models.user import User

authRouter = Blueprint("auth", __name__)


@authRouter.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('auth.protected'))
    return 'Invalid username or password'

@authRouter.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully'

@authRouter.route('/protected')
@login_required
def protected():
    return 'Protected area'