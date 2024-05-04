# Lead Capture App

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-v3.9-blue)](https://www.python.org/downloads/release/python-390/)
[![Flask](https://img.shields.io/badge/flask-v2.0-blue)](https://flask.palletsprojects.com/en/2.0.x/)
[![MySQL](https://img.shields.io/badge/mysql-v8.0-blue)](https://dev.mysql.com/downloads/mysql/)


<!-- Description of the Application -->
Lead Capture App is a simple web application built with Flask, MySQL, and SQLAlchemy. It serves as a landing page with a lead capture form to collect email addresses and additional information from users. Submitted data is securely stored in a MySQL database.

## Basic Setup

### Step 1: Environment Setup

#### Open Visual Studio Code (VSCode):

- Launch VSCode on your Windows 11 system.

#### Create a New Project Directory:

1. Open the terminal in VSCode.
2. Navigate to the directory where you want to create your project.
3. Create a new directory for your project, for example:

   ```bash
   mkdir lead_capture_app
   cd lead_capture_app
   ```

#### Set Up Virtual Environment:

- Install the virtual environment package:

  ```bash
  pip install virtualenv
  ```

- Create a new virtual environment:

  ```bash
  virtualenv venv
  ```

- Activate the virtual environment:

  ```bash
  venv\Scripts\activate
  ```

  You should see `(venv)` in your terminal prompt, indicating that the virtual environment is active.

### Step 2: Dependency Installation

#### Create requirements.txt:

- Create a file named `requirements.txt` in your project directory if it doesn't exist already.

#### Add Dependencies:

- Open `requirements.txt` in your text editor.
- Add the following dependencies required for the project:

  ```plaintext
  Flask==2.0.2
  SQLAlchemy==1.4.31
  mysql-connector-python==8.0.28
  Flask-WTF
  ```

- Save the `requirements.txt` file.

#### Install Dependencies:

- In the terminal, while the virtual environment is activated, install the dependencies using pip:

  ```bash
  pip install -r requirements.txt
  ```

### Install MySQL Server

- If you haven't already installed MySQL Server, you can download it from the [official website](https://dev.mysql.com/downloads/mysql/).

#### Start MySQL Server:

- Once MySQL Server is installed, start the MySQL service.
- You can typically start the service from the Services application on Windows or by using the command line.

#### Create a New Database:

1. Open a terminal or command prompt.
2. Log in to MySQL as the root user (you may need to provide your MySQL root password):

   ```bash
   mysql -u root -p
   ```

3. Once logged in, create a new database for your Flask application. For example, let's create a database named `lead_capture_db`:

   ```sql
   CREATE DATABASE lead_capture_db;
   ```

   You can replace `lead_capture_db` with your preferred database name.

#### Create a Database User (Optional, but recommended):

- It's a good practice to create a separate database user for your Flask application with restricted permissions.
- You can create a new user and grant permissions to access the `lead_capture_db` database:

  ```sql
  CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
  GRANT ALL PRIVILEGES ON lead_capture_db.* TO 'root'@'localhost';
  FLUSH PRIVILEGES;
  ```

  Replace `'app_user'` with your desired username and `'your_password'` with a secure password.

#### Exit MySQL:

- Once you've created the database and user, you can exit MySQL by typing:

  ```bash
  exit;
  ```
