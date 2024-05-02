from flask import render_template, request, redirect, url_for, flash
from app import app, db
from flask_login import login_required
from app.models.joblog import Terminal, Unit
from app.models.staff_login import User


# Route to edit terminal
@app.route('/edit_terminal/<int:terminal_id>', methods=['GET', 'POST'])
@login_required
def edit_terminal(terminal_id):
    terminal = Terminal.query.get_or_404(terminal_id)

    if request.method == 'POST':
        # Update terminal details
        terminal.terminal= request.form.get('terminal')
        db.session.commit()
        flash('Terminal updated successfully!', 'success')
        return redirect(url_for('view_terminals'))

    return render_template('admin/edit_terminal.html', terminal=terminal)


@app.route('/edit_terminals', methods=['GET'])
@login_required
def edit_terminals():
    terminals = Terminal.query.all()
    return render_template('admin/edit-delete_terminals.html', terminals=terminals)



# Route to edit unit 
@app.route('/edit_unit/<int:unit_id>', methods=['GET', 'POST'])
@login_required
def edit_unit(unit_id):
    unit = Unit.query.get_or_404(unit_id)

    if request.method == 'POST':
        # Update unit details
        unit.unit = request.form.get('unit')
        db.session.commit()
        flash('Unit updated successfully!', 'success')
        return redirect(url_for('view_units'))

    return render_template('admin/edit_unit.html', unit=unit)


@app.route('/edit_units', methods=['GET'])
@login_required
def edit_units():
    units = Unit.query.all()
    return render_template('admin/edit-delete_units.html', units=units)




@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if user is None:
        return "User not found", 404

    if request.method == 'POST':
        # Update user details
        user.email = request.form['email']
        user.password = request.form['password']
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('view_users'))

    return render_template('admin/edit_user.html', email=user.email, password=user.password)


@app.route('/edit_users', methods=['GET'])
@login_required
def edit_users():
    users = User.query.all()
    return render_template('admin/edit-delete_users.html', users=users)