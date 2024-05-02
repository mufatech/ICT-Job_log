# Import necessary modules
from flask import render_template, request, redirect, url_for
from app import app
from app.models.joblog import Terminal, Unit, JobLogForm
from app.models.user import User
from flask_login import login_required
from app.models.staff_login import User

@app.route('/view_terminals', methods=['GET'])
@login_required
def view_terminals():
    terminals = Terminal.query.all()
    return render_template('admin/view_terminals.html', terminals=terminals)


@app.route('/view_units', methods=['GET'])
@login_required
def view_units():
    units = Unit.query.all()
    return render_template('admin/view_units.html', units=units)


@app.route('/view_users', methods=['GET'])
@login_required
def view_users():
    users = User.query.all()
    return render_template('admin/view_users.html', users=users)

@app.route('/view_created_users', methods=['GET'])
@login_required
def view_created_users():
    staffs = User.query.all()
    return render_template('admin/view_created_users.html', staffs=staffs)

@app.route('/unit_jobs', methods=['GET'])
def unit_jobs():
    # Query units from the database
    units = Unit.query.all()
    return render_template('admin/unit_jobs.html', units=units)

@app.route('/view_unit_jobs', methods=['GET', 'POST'])
def view_unit_jobs():
    if request.method == 'POST':
        unit_id = request.form.get('unit_id')
        if unit_id:
            return redirect(url_for('view_unit_jobs', unit_id=unit_id))
    
    unit_id = request.args.get('unit_id')
    if unit_id:
        unit = Unit.query.get_or_404(unit_id)
        unit_jobs = JobLogForm.query.filter_by(unit_id=unit_id).all()
        return render_template('admin/view_unit_jobs.html', unit=unit, unit_jobs=unit_jobs)
    
    
@app.route('/terminal_jobs', methods=['GET'])
def terminal_jobs():
    # Query terminals from the database
    terminals = Terminal.query.all()
    return render_template('admin/terminal_jobs.html', terminals=terminals)


@app.route('/view_terminal_jobs', methods=['GET', 'POST'])
def view_terminal_jobs():
    if request.method == 'POST':
        terminal_id = request.form.get('terminal_id')
        if terminal_id:
            return redirect(url_for('view_terminal_jobs', terminal_id=terminal_id))
    
    terminal_id = request.args.get('terminal_id')
    if terminal_id:
        terminal = Terminal.query.get_or_404(terminal_id)
        terminal_jobs = JobLogForm.query.filter_by(terminal_id=terminal_id).all()
        return render_template('admin/view_terminal_jobs.html', terminal=terminal, terminal_jobs=terminal_jobs)


    # return redirect(url_for('unit_jobs'))

# @app.route('/view_unit_jobs/<int:unit_id>', methods=['GET'])
# def view_unit_jobs(unit_id):
    
#     # Get the selected unit ID from the request
#     unit_id = request.args.get('unit_id')

#     # Query the unit object based on the selected unit ID
#     unit = Unit.query.get(unit_id)

#     # If unit_id is not provided or invalid, handle it appropriately
#     if not unit:
#         return "Invalid unit selected or no unit selected."

#     # Query jobs filtered by the selected unit ID
#     jobs = JobLogForm.query.filter_by(unit_id=unit_id).all()

#     return render_template('admin/view_unit_jobs.html', unit=unit, jobs=jobs)
    
    # unit = Unit.query.get_or_404(unit_id)  # Retrieve the unit based on the ID
    # unit_jobs = JobLogForm.query.filter_by(unit_id=unit_id).all()  # Retrieve job logs for the unit
    # return render_template('admin/view_unit_jobs.html', unit=unit, unit_jobs=unit_jobs)