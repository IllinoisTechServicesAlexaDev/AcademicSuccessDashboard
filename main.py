from flask import Flask, render_template, url_for, request
from app import app
from db_setup import init_db
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, and_, or_

from models import Student, db

#app = Flask(__name__)

init_db()
        
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/advisor", methods=['GET', 'POST'])
def advisor():

    results = Student.query.all()
    if request.method == 'POST':
        #name = request.form['name']
        degree_level = request.form.get('degree_level')
        department = request.form.get('department')

        query = Student.query
        #if name:
            #query = query.filter(Student.name == name)
        if degree_level:
            query = query.filter(Student.degree_level == degree_level)
        if department:
            query = query.filter(Student.department == department)

        results = query.all()
        
    return render_template('advisor.html', advisees=results)


if __name__ == '__main__':
    app.run(debug=True)