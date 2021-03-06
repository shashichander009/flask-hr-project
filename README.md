# Flask Web App - MindFree HR System

MindFree HR System is a CRUD web app built with Flask.

## Language and Libraries

This project is built with

Backend : Python 3.7.4

Web Framework : Flask with SQLAlchemy and Alembic for Data Migration

Database : PostgresSQL

Frontend : HTML, CSS

## Installation

clone this repo

create a virtual env

activate the virtual env

install all dependencies

```bash
pip install -r requirements.txt
```

## Usage

### DATABASE SETTING UP

Create a postgres Database and replace the link of SQLALCHEMY_DATABASE_URI in config.py folder. It should be of the format

postgresql://username:password@localhost:5432/db-name

Once you are done, run the following command

```bash
flask db upgrade
```

This will create Admin and Employee DB in your database

### PROJECT USAGE

Finally, after all the steps run the following command

```bash
flask run
```

Go to the URL : http://127.0.0.1:5000/ to view the project

### First Steps at the Website

Click Sign Up button and create an Admin.

Now go to add Employee and create an employee. Important points

- Phone Number should be 10 digits
- Salary can't be zero

On the home page, you can find employee list.

Click on any Employee to view Details of Employee

If you are logged in you can edit and delete employees.

## Screenshots

### Home Page

![Home Screen](screenshots/home_screen.png?raw=true "Home Page")

### Sign In Page

![SignIn Page](screenshots/sign_in_page.png?raw=true "Sign In Page")

### Employee Detail

![Employee Detail](screenshots/employee_detail.png?raw=true "Emp Detail Page")

### Add Employee Page

![Add Employee](screenshots/add_employee.png?raw=true "Add Emp Page")
