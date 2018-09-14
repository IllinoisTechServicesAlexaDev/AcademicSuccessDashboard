from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Student, db
 
engine = create_engine('sqlite:///academystatus.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


advisees = [
    {
        'netid' : 'msmith5',
        'name': 'Mary Smith',
        'department': 'Computer Science',
        'degree_level': 'Undergraduate',
        'email': 'msmith5@illinois.edu',
        'wireless_status':'danger',
        'compass_status':'warning',
        'moodle_status':'success'
    },
    {
        'netid' : 'jdoe2',
        'name': 'John Doe',
        'department': 'Information Science',
        'degree_level': 'PhD',
        'email': 'jdoe2@illinois',
        'wireless_status':'success',
        'compass_status':'warning',
        'moodle_status':'success'
    },
    {
        'netid' : 'jwhite3',
        'name': 'Jane White',
        'department': 'Electrical and Computer Engineering',
        'degree_level': 'Master',
        'email': 'jwhite3@illinois.edu',
        'wireless_status':'danger',
        'compass_status':'warning',
        'moodle_status':'danger'
    },
    {
        'netid' : 'mjones6',
        'name': 'Mark Jones',
        'department': 'Electrical and Computer Engineering',
        'degree_level': 'Master',
        'email': 'mjones6@illinois.edu',
        'wireless_status':'success',
        'compass_status':'warning',
        'moodle_status':'danger'
    }

]
 
def init_db():
    Base.metadata.create_all(bind=engine)
    db.drop_all()
    db.create_all()
    for advisee in advisees:
    	ad = Student(netid=advisee['netid'],
    				 name=advisee['name'],
    				 department=advisee['department'], 
    				 degree_level=advisee['degree_level'], 
    				 email=advisee['email'],
    				 wireless_status=advisee['wireless_status'],
    				 compass_status=advisee['compass_status'],
    				 moodle_status=advisee['moodle_status'])
    	db.session.add(ad)
    db.session.commit()

