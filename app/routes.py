from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required
from flask_login import logout_user
from app.models import Admin, Employee
from flask import request
from werkzeug.urls import url_parse
from app import db, app
from app.forms import LoginForm, RegistrationForm, EmpForm, UpdateEmpForm


@app.route('/')
@app.route('/index')
def index():
    employees = Employee.query.all()
    return render_template('index.html', title='Home', employees=employees)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        admin = Admin(email=form.email.data)
        admin.set_password(form.password.data)
        db.session.add(admin)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/add_emp', methods=['GET', 'POST'])
@login_required
def add_emp():
    form = EmpForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            name=form.name.data,
                            phone=form.phone.data,
                            location=form.location.data,
                            salary=form.salary.data)
        db.session.add(employee)
        db.session.commit()
        flash('Employee added', 'success')
        return redirect(url_for('index'))
    return render_template('add_emp.html', title='Add Employee', form=form)


@app.route("/employee/<int:id>")
def employee(id):
    employee = Employee.query.get_or_404(id)
    return render_template('employee.html',
                           title=employee.name,
                           employee=employee)


@app.route("/employee/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update_emp(id):
    employee = Employee.query.get_or_404(id)

    form = UpdateEmpForm()

    if form.validate_on_submit():

        email = form.email.data
        phone = form.phone.data
        location = form.location.data
        name = form.name.data
        salary = form.salary.data

        data_updated = False
        data_valid = True

        if email != employee.email:
            if Employee.query.filter_by(email=email).first() is not None:
                form.email.errors.append("Email already exist.")
                data_valid = False
            else:
                employee.email = email
                data_updated = True

        if phone != employee.phone:
            if Employee.query.filter_by(phone=phone).first() is not None:
                form.phone.errors.append("Phone No already exist.")
                data_valid = False
            else:
                employee.phone = phone
                data_updated = True

        if location != employee.location or salary != employee.salary \
                or employee.name != name:
            data_updated = True

        if data_updated and data_valid:
            employee.location = location
            employee.salary = salary
            employee.name = name
            db.session.commit()
            flash('Employee details updated', 'success')
            return redirect(url_for('employee', id=id))

    elif request.method == 'GET':
        form.name.data = employee.name
        form.email.data = employee.email
        form.phone.data = employee.phone
        form.location.data = employee.location
        form.salary.data = employee.salary
    return render_template('add_emp.html', title='Update Post',
                           form=form,)


@app.route("/employee/<int:id>/delete", methods=['GET', 'POST'])
@login_required
def delete_emp(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    message = str(employee.name) + ' has been deleted!'
    flash(message, 'success')
    return redirect(url_for('index'))
