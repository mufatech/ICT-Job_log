from flask import redirect, url_for, flash
from app import app, db
from flask_login import login_required
from app.models.joblog import Terminal, Unit

# Route to delete terminal
@app.route('/delete_terminal/<int:terminal_id>', methods=['GET'])
@login_required
def delete_terminal(terminal_id):
    terminal = Terminal.query.get_or_404(terminal_id)
    db.session.delete(terminal)
    db.session.commit()
    flash('Terminal deleted successfully!', 'success')
    return redirect(url_for('view_terminals'))



# Route to delete unit


@app.route('/delete_unit/<int:unit_id>', methods=['GET'])
@login_required
def delete_unit(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    db.session.delete(unit)
    db.session.commit()
    flash('Unit deleted successfully!', 'success')
    return redirect(url_for('view_units'))
