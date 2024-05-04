### Step 4: Flask Application Configuration

1. **Create Configuration File**:
   - Create a file named `config.py` in your project directory.

2. **Database Configuration**:
   - In `config.py`, add the configuration for connecting to the MySQL database. You'll need to specify the database URL, which includes the username, password, host, port, and database name.

     ```python
     import os

     class Config:
         SECRET_KEY = 'your_secret_key'  # Replace with a random secret key

         # MySQL database configuration
         SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://app_user:your_password@localhost/lead_capture_db'
         SQLALCHEMY_TRACK_MODIFICATIONS = False
     ```
   - Replace `'your_secret_key'`, `'app_user'`, `'your_password'`, and `'lead_capture_db'` with appropriate values.

### Step 5: Database Model Definition

1. **Create Models File**:
   - Inside the `app` directory, create a file named `models.py`.

2. **Define SQLAlchemy Model**:
   - In `models.py`, define the SQLAlchemy model for storing lead information.
 
     ```python
     from app import db

     class Lead(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         email = db.Column(db.String(120), unique=True, nullable=False)
         name = db.Column(db.String(100))
         company = db.Column(db.String(100))

         def __repr__(self):
             return f'<Lead {self.email}>'
     ```
   - This model represents a lead with an email address, name, and company.
  
   - Your Flask application is configured to connect to the MySQL database, and you have defined the database model for storing lead information.

### Step 6: Flask Routes and Views
- Define Flask routes and views to handle requests, serve the landing page, and process form submissions.

1. **Create Routes File**:
   - Inside the `app` directory, create a file named `routes.py`.

2. **Define Routes**:
   - In `routes.py`, define the routes for serving the landing page and handling form submissions.  

3. **Implement Error Handling**:
   - In your Flask routes (`routes.py`), implement basic error handling to catch any validation errors or database-related issues.
 
4. **Flash Messages**:
Integrate Flask's `flash()` function into the `routes.py` file to display informative messages to the user.

Validating form data, especially email format, is crucial for data integrity and security. While Flask-WTF is a popular choice for form validation in Flask applications, you can also implement validation manually using built-in Python libraries or regular expressions.

```python
from sqlalchemy.exc import IntegrityError
from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Lead
from wtforms import Form, StringField, validators

class LeadForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    name = StringField('Name')
    company = StringField('Company')

@app.route('/')
def index():
    form = LeadForm()
    return render_template('index.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    form = LeadForm(request.form)
    if form.validate():
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
        flash('Invalid form data. Please check your input.', 'error')

    return redirect(url_for('index'))
```

- We've defined a `LeadForm` class using Flask-WTF's `Form` class. We've added validators for the email field to ensure it's not empty and that it's a valid email address.

- When a form submission is received, the data is validated using `form.validate()`. If the form data is valid, the lead is submitted and a success flash message is displayed. If the form data is invalid, an error flash message is displayed.

- Whenever a lead is successfully submitted, a success flash message will be displayed. If there's an IntegrityError (e.g., duplicate email), an error flash message will be displayed. Additionally, if any other unexpected error occurs, an error flash message will be displayed as well.

### Step 7: Basic HTML

- We use a mechanism in the HTML templates to display these flash messages to the user. Typically, we would place something like `{% with messages = get_flashed_messages(with_categories=true) %}` in the template to iterate over the messages and display them accordingly.

- The form in the `index.html` file submits data to the appropriate Flask route for processing, and let's design the HTML form to collect lead information.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lead Capture</title>
    <style>
        /* Basic CSS styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        form {
            margin-top: 20px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            font-weight: bold;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .form-group input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
        }
        .flash-message {
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        .success {
            background-color: #d4edda;
            border-color: #c3e6cb;
            color: #155724;
        }
        .error {
            background-color: #f8d7da;
            border-color: #f5c6cb;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Lead Capture Form</h1>
        <form action="{{ url_for('submit') }}" method="post">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name">
            </div>
            <div class="form-group">
                <label for="company">Company</label>
                <input type="text" id="company" name="company">
            </div>
            <div class="form-group">
                <input type="submit" value="Submit">
            </div>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash-message {{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

The `<form>` tag's `action` attribute is set to `{{ url_for('submit') }}`, which dynamically generates the URL for the `/submit` route in Flask. This ensures that when the form is submitted, the data will be sent to the appropriate route for processing.


