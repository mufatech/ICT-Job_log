from flask import render_template, request
from app import app, db
from flask_login import login_required
from app.models.joblog import JobLogForm
from sqlalchemy import func

@app.route('/admin/dashboard', methods=['GET'])
@login_required
def admin_dashboard():
    # Calculate total jobs_logged
    total_logged_jobs = db.session.query(func.count(JobLogForm.id)).scalar()

    return render_template('admin/dashboard.html', total_logged_jobs=total_logged_jobs)




#      return render_template('admin/dashboard.html')
# @app.route("/admin/search", methods=["GET", "POST"])
# def search():
#     if request.method == "POST":
#         search_term = request.form["searchTerm"]
#         results = execute_query(search_term='', filter_columns=['terminal', 'unit'])
#     else:
#         results = execute_query()

#     return render_template("index.html", results=results)
  