from sqlalchemy.exc import IntegrityError
from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Lead
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class LeadForm(FlaskForm):
    email = StringField('Email',)
    name = StringField('Name')
    company = StringField('Company')

@app.route('/')
def index():
    form = LeadForm()
    return render_template('index.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    form = LeadForm()
    if form.validate_on_submit():
        try:
            email = form.email.data
            name = form.name.data
            company = form.company.data

            # Create a new Lead instance and save it to the database
            new_lead = Lead(email=email, name=name, company=company)
            db.session.add(new_lead)
            db.session.commit()

            flash('Lead submitted successfully!', 'success')
            return redirect(url_for('index'))

        except IntegrityError:
            db.session.rollback()
            flash('Error: This email address is already registered.', 'error')

        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again later.', 'error')

    else:
        # Debugging: Print form data received when validation fails
        print("Form data received:", request.form)
        flash('Invalid form data. Please check your input.', 'error')

    return redirect(url_for('index'))
