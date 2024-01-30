# Import necessary modules
from flask import render_template, request
from app import app
from sqlalchemy.orm import joinedload
from app.models.joblog import JobLogForm
from flask_login import login_required

# Define a route for viewing logged jobs
@app.route('/view_logged_jobs', methods=['GET'])
@login_required  # Use login_required to ensure only logged-in admins can access this page
def view_logged_jobs():
    # Retrieve the page number from the request, default to 1 if not provided
    page = request.args.get('page', default=1, type=int)

    # Set the number of results per page
    per_page = 20  # You can adjust this to your desired number of results per page

    # Query logged job with pagination
    logged_jobs = JobLogForm.query.options(
        joinedload(JobLogForm.terminal),
        joinedload(JobLogForm.unit)
    ).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('admin/view_logged_jobs.html', logged_jobs=logged_jobs)

