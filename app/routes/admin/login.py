from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models.login import Admin
from flask_login import login_user, logout_user, login_required


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if there are any admins in the admin DB
        admin_count = Admin.query.count()

        if admin_count == 0:
            # No admins in the DB, so the first user becomes the admin
            admin = Admin(email=email)
            admin.set_password(password)  # Set the password securely
            db.session.add(admin)
            db.session.commit()

            # Log in the admin user
            login_user(admin)
            
            flash('You are now the admin. Welcome!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            # Admins exist, so check the entered credentials
            admin = Admin.query.filter_by(email=email).first()
            if admin and admin.check_password(password):
                # Log in the admin user
                login_user(admin)
                flash('Login successful!', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid login details.', 'danger')

    return render_template("admin/login.html")




@app.route('/admin/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('admin_login'))
    
