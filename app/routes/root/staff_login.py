from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models.user import User
from app.models.staff_login import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash


# @login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/root/staff_login', methods=['GET', 'POST'])
def staff_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        # return render_template('root/joblog.html')
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            session['email'] = email
            return redirect(url_for('job_log'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('root/staff_login.html')

# @app.route('/job_log')
# @login_required
# def job_log():
#     # Only authenticated users can access this route
#     # You can implement further authorization logic here
#     return render_template('root/joblog.html')

# @app.route('/root/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out.', 'success')
#     return redirect(url_for('user_login'))

