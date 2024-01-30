# from app import db

# class Terminal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     terminal = db.Column(db.String(50), nullable=False)

# class Unit(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     unit = db.Column(db.String(50), nullable=False)


# # Define relationships
#     terminal = db.relationship('Terminal', backref=db.backref('job_log', lazy=True))
#     unit = db.relationship('Unit', backref=db.backref('job_log', lazy=True))