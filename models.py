from app import db
  
class Student(db.Model):

    netid = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)
    degree_level = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    wireless_status = db.Column(db.String(20), nullable=False)
    compass_status = db.Column(db.String(20), nullable=False)
    moodle_status = db.Column(db.String(20), nullable=False)

