from flask import Flask, render_template,  request, url_for, flash, redirect
from app.models.joblog import JobLogForm, Terminal, Unit
from app import app, db


@app.route('/joblog', methods=['GET', 'POST'])
def job_log():
    form = JobLogForm()

    if request.method == 'POST':
        fault_date = request.form['fault_date']
        username = request.form['username']
        number = request.form['number']
        terminal_id = int(request.form['terminal'])
        unit_id = int(request.form['unit'])
        location = request.form['location']
        equipment_type = request.form['equipment_type']
        fault = request.form['fault']
        rectification = request.form['rectification']
        remarks = request.form['remarks']


        #Create a new job
        new_job = JobLogForm(
            fault_date=fault_date, 
            username=username, 
            number=number, 
            terminal_id=terminal_id,
            unit_id=unit_id,
            location=location,
            equipment_type=equipment_type,
            fault=fault,
            rectification=rectification,
            remarks=remarks
        )
           

        db.session.add(new_job)
        db.session.commit()

        flash('Job log submitted successfully!', 'success')
        return redirect(url_for('success_page'))
    
    # Fetching terminals and units for rendering the form
    terminals = Terminal.query.all()
    units = Unit.query.all()

    return render_template('root/joblog.html', terminals=terminals, units=units)


@app.route('/success')
def success_page():
    return render_template('root/success.html')


    
