# Import necessary modules
from flask import render_template
from app import app
from app.models.joblog import Terminal, Unit
from flask_login import login_required

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
