# Задание
# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/electronics")
def electronics():
    products = {
        '1': {
            'name': 'Ноутбук Acer Aspire',
            'price': 45000,
            'description': 'Ноутбук с диагональю 15.6", 8GB RAM, 256GB SSD.',
            'category': 'Ноутбуки',
            'in_stock': 5
        },
        '2': {
            'name': 'Apple iPhone 13',
            'price': 80000,
            'description': 'Смартфон с диагональю 6.1", камера 12MP, 128GB памяти.',
            'category': 'Смартфоны',
            'in_stock': 3
        },
        '3': {
            'name': 'Sony WH-1000XM4',
            'price': 20000,
            'description': 'Беспроводные наушники с активным шумоподавлением.',
            'category': 'Аудиотехника',
            'in_stock': 10
        },
        '4': {
            'name': 'Samsung QLED TV 55"',
            'price': 55000,
            'description': 'Телевизор с диагональю 55", разрешение 4K.',
            'category': 'Телевизоры',
            'in_stock': 2
        }
    }
    return render_template("electronics.html", products=products)


@app.route("/tv")
def tv():
    product = {
        
        'name': 'Samsung QLED TV 55"',
        'price': 55000,
        'description': 'Телевизор с диагональю 55", разрешение 4K.',
        'category': 'Телевизоры',
        'in_stock': 2

    }
    return render_template("tv.html", product=product)


if __name__ == '__main__':
    app.run(debug=True)
