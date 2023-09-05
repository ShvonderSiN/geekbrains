from flask import Flask, render_template, url_for, request, redirect, flash
from models import db, Student, Faculty, Author, Book, Mark, Users, User
from forms import RegistrationForm, HomeWorkRegistrationForm
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar3.db'
app.config['SECRET_KEY'] = b'db7fce575ca9ea66f0726d555abb58dc95fd493bc00e5e1c1247ff4e9c6eb71e'
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)


@app.context_processor
def menu_items():
    menu_items = [
        {'name': 'Home', 'url': url_for("index")},
        {'name': 'Homework', 'url': url_for("homework")},
        {'name': 'Task 1', 'url': url_for("task1")},
        {'name': 'Task 2', 'url': url_for("task2")},
        {'name': 'Task 3', 'url': url_for("task3")},
        {'name': 'Task 4', 'url': url_for("task4")},
        # {'name': 'Task 9', 'url': url_for("task9")},
    ]
    return dict(menu_items=menu_items)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1')
def task1():
    all_students = Student.query.order_by(-Student.id).all()
    return render_template('task1.html', students=all_students)


@app.route('/task2')
def task2():
    all_books = Book.query.all()
    return render_template('task2.html', all_books=all_books)


@app.route('/task3')
def task3():
    students = Student.query.all()  # Получаем всех студентов
    student_data = []

    for student in students:
        marks = Mark.query.filter_by(student_id=student.id).all()  # Получаем оценки для каждого студента
        mark_data = [{'subject_name': mark.subject_name, 'mark': mark.mark} for mark in marks]
        student_info = {
            'id': student.id,
            'name': student.name,
            'surname': student.surname,
            'age': student.age,
            'gender': student.gender,
            'group': student.group,
            'email': student.email,
            'marks': mark_data
        }
        student_data.append(student_info)

    return render_template('task3.html', students=student_data)


@app.route('/task4', methods=['POST', 'GET'])
def task4():
    form = RegistrationForm()
    username = form.username.data
    email = form.email.data
    password = form.password.data
    if request.method == 'POST' and form.validate():
        if Users.query.filter(Users.username == username).all() or Users.query.filter(
                Users.email == email).all():
            context = {'alert_message': "Пользователь уже существует!"}
            return render_template('task4.html', form=form, **context)
        else:
            print(Users.query.filter(Users.username == username).all())
            new_user = Users(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
    return render_template('task4.html', form=form)


@app.route('/homework', methods=['GET', 'POST'])
def homework():
    form = HomeWorkRegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name, surname, email, password = form.name.data, form.surname.data, form.email.data, form.password.data
        hashed_password = generate_password_hash(password, method='sha256')
        del password
        db.session.add(User(name=name, surname=surname, email=email, password=hashed_password))
        db.session.commit()
        flash('Спасибо за регистрацию!', 'success')
        return redirect(url_for('index'))
    return render_template('homework.html', form=form)


@app.cli.command('init_db')
def initdb_command():
    db.create_all()
    print('New DB just created.')
