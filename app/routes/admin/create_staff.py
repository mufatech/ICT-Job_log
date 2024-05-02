from flask import render_template, request, redirect, url_for, flash 
from flask_login import login_required, current_user
from app import app, db
from app.models.user import User
from app.models.staff_login import User
from werkzeug.security import generate_password_hash

@app.route('/admin/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'user')  # Default role is 'user'

        if role not in ['admin', 'user']:
            flash('Invalid role', 'danger')
            return redirect(url_for('create_user'))
        
        # Check if the email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('create_user'))
        
        # Create a new user object
        new_user = User(email=email)

        # Set the password for the new user
        new_user.set_password(password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('User created successfully', 'success')
        return redirect(url_for('view_created_users'))

    return render_template('admin/create_user.html')



# @app.route('/change_password', methods=['GET', 'POST'])
# # @login_required
# def change_password():
#     if request.method == 'POST':
#         new_password = request.form['new_password']
        
#         # Retrieve the current user from the database
#         user = User.query.get(current_user.id)
        
#         # Update the password for the current user
#         user.set_password(new_password)
#         db.session.commit()
        
#         flash('Password changed successfully', 'success')
#         return redirect(url_for('job_log'))  # Redirect to job log page after password change

#     return render_template('change_password.html')



# def change_password():
#     if request.method == 'POST':
#         # Check if the user is authenticated
#         if current_user.is_authenticated:
#             new_password = request.form['new_password']
#             confirm_password = request.form['confirm_password']
#             current_user.set_password(new_password)
#             db.session.commit()
#             flash('Password changed successfully', 'success')
#             return redirect(url_for('staff_login'))
#         # else:
#         #     # If user is not logged in, redirect to the login page
#         #     flash('Please log in to change your password', 'danger')
#         #     return redirect(url_for('staff_login'))
#     return render_template('root/change_password.html')

            
            
            
        # current_password = request.form['current_password']
        

        # # Check if the current password matches the user's password
        # # Check if the user is authenticated
        # if current_user.is_authenticated:
        #     # Proceed with changing the password
        #     # (Code for changing password goes here)
        #     new_password = request.form['new_password']
        #     current_user.set_password(new_password)
        #     db.session.commit()
        # # if not current_user.check_password(current_password):
        #     flash('Incorrect current password', 'danger')
        #     return redirect(url_for('change_password'))

        # # Check if the new password and confirm password match
        # if new_password != confirm_password:
        #     flash('New password and confirm password do not match', 'danger')
        #     return redirect(url_for('change_password'))

        # # Update the user's password
        # current_user.set_password(new_password)
        # db.session.commit()

        # flash('Password changed successfully', 'success')
        # return redirect(url_for('staff_login'))

    