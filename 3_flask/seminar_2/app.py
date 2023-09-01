from pathlib import PurePath, Path

from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from werkzeug.utils import secure_filename

import re

app = Flask(__name__)
app.secret_key = b'db7fce575ca9ea66f0726d555abb58dc95fd493bc00e5e1c1247ff4e9c6eb71e'


@app.context_processor
def menu_items():
    menu_items = [
        {'name': 'Home', 'url': url_for("index")},
        {'name': 'Task 1', 'url': url_for("task1")},
        {'name': 'Task 2', 'url': url_for("task2")},
        {'name': 'Task 3', 'url': url_for("task3")},
        {'name': 'Task 4', 'url': url_for("task4")},
        {'name': 'Task 9', 'url': url_for("task9")},
    ]
    return dict(menu_items=menu_items)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1', methods=['GET', 'POST'])
def task1():
    if request.method == 'POST':
        return redirect(url_for('hello', name='User'))
    return render_template('task1.html')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет {name}'


@app.route('/task2')
def task2():
    return render_template('task2.html')


@app.route('/task2_upload', methods=['GET', 'POST'])
def task2_upload():
    if request.method == 'POST':
        image = request.files.get('image')
        file_name = secure_filename(image.filename)
        Path(Path.cwd(), 'static', 'uploads').mkdir(exist_ok=True)
        image.save(PurePath.joinpath(Path.cwd(), 'static', 'uploads', file_name))
        return f"""Файл {file_name} загружен на сервер<br>
            <a href='{url_for('task2_upload')}'>Назад</a>"""
    return render_template('form_task2.html')


@app.route('/task3', methods=['GET', 'POST'])
def task3():
    login = 'login'
    password = 'password'
    if request.method == 'POST':
        l = request.form.get('login')
        p = request.form.get('password')
        if l == login and p == password:
            return redirect(url_for('hello', name=login))
        else:
            flash('Ошибка!, неверный логин или пароль', 'danger')
            return redirect(url_for('task3'))
    return render_template('task3.html')


@app.route('/task4', methods=['GET', 'POST'])
def task4():
    if request.method == 'POST':
        text = request.form.get('text').strip()
        words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', text)
        print(words)
        return f'Слов в тексте: {len(words)}'
    return render_template('task4.html')


@app.route('/task9', methods=['GET', 'POST'])
def task9():
    username = request.cookies.get('username')
    email = request.cookies.get('email')
    if request.method == 'POST':
        name_form = request.form.get('name')
        email_form = request.form.get('email')
        response = make_response(redirect('/task9'))
        response.set_cookie('username', name_form)
        response.set_cookie('email', email_form)
        return response
    return render_template('task9.html', username=username, email=email)


@app.post('/logout')
def logout():
    response = make_response(redirect('/task9'))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
