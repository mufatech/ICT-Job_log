from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.joblog import Terminal, Unit


# Add New terminal Route
@app.route('/admin/add_terminal', methods=['GET', 'POST'])
@login_required
def add_terminal():
    if request.method == 'POST':
        terminal = request.form.get('terminal')
        
        if not terminal:
            flash('Terminal name is requires', 'error')
            return redirect(url_for('add_terminal'))
        try:
        # Create a new terminal instance and add it to the database
            new_terminal = Terminal(terminal=terminal)
            db.session.add(new_terminal)
            db.session.commit()
        
            flash('Terminal added successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            flash(f'Error adding terminal: {str(e)}', 'error')
            db.session.rollback() # Rollback the transaction in case of an error
          
    return render_template('admin/add_terminal.html')


# Add New unit Route
@app.route('/admin/add_unit', methods=['GET', 'POST'])
@login_required
def add_unit():
    if request.method == 'POST':
        unit = request.form.get('unit')       
        
        if not unit:
            flash('Unit name is requires', 'error')
            return redirect(url_for('add_unit'))
        try:
        # Create a new unit instance and add it to the database
            new_unit = Unit(unit=unit)
            db.session.add(new_unit)
            db.session.commit()
        
            flash('Unit added successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            flash(f'Error adding unit: {str(e)}', 'error')
            db.session.rollback() # Rollback the transaction in case of an error
    
    return render_template('admin/add_unit.html')


