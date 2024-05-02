from flask import render_template, request, redirect, url_for, flash 
from flask_login import login_required, current_user
from app import app, db
from app.models.staff_login import User

def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/change_password', methods=['GET', 'POST'])
# @login_required
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        
        # Retrieve the current user from the database
        user = User.query.get(current_user.id)
        
        if user is None:
            app.logger.error('User not found: {}'.format(current_user.id))
            flash('User not logged', 'danger')
            return redirect(url_for('job_log'))
        
        # Update the password for the current user
        user.set_password(new_password)
        db.session.commit()
        
        flash('Password changed successfully', 'success')
        return redirect(url_for('staff_login'))  # Redirect to staff login page after password change
       
    return render_template('root/change_password.html')
  
  
  
  
  
    # if request.method == 'POST':
    #     new_password = request.form['new_password']
        
    #     # Retrieve the current user from the database
    #     user = User.query.get(current_user.id)
        
    #     # Update the password for the current user
    #     user.set_password(new_password)
    #     db.session.commit()
        
    #     flash('Password changed successfully', 'success')
    #     return redirect(url_for('job_log'))  # Redirect to job log page after password change

    # return render_template('root/change_password.html')