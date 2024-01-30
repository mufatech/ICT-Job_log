# Modify joblog.py
from app import db

class JobLogForm(db.Model):
    __tablename__ = 'joblogs' 
    id = db.Column(db.Integer, primary_key=True)
    fault_date = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(15), nullable=False)
    terminal_id = db.Column(db.Integer, db.ForeignKey('terminals.id'), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    equipment_type = db.Column(db.String(50), nullable=False)
    fault= db.Column(db.Text, nullable=False)
    rectification = db.Column(db.Text, nullable=True)
    remarks = db.Column(db.String(100), nullable=False)

    #Define relationships
    terminal = db.relationship('Terminal', back_populates='joblogs', primaryjoin='JobLogForm.terminal_id == Terminal.id')
    unit = db.relationship('Unit', back_populates='joblogs', primaryjoin='JobLogForm.unit_id == Unit.id')

class Terminal(db.Model):
    __tablename__ = 'terminals'
    id = db.Column(db.Integer, primary_key=True)
    terminal = db.Column(db.String(50), nullable=False)

    #Define relationships
    joblogs = db.relationship('JobLogForm', back_populates='terminal')

class Unit(db.Model):
    __tablename__ = 'units'
    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(50), nullable=False)
    
    joblogs = db.relationship('JobLogForm', back_populates='unit')
