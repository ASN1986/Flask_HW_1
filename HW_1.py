from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shoes/')
def shoes():
    _shoes = [
        {
            "name": "Кроссовки Reebok Nano X",
            "price": '150 $',
            "description": 'Кроссовки для функциональных тренировок ',

        },
        {
            "name": "Кроссовки Nike Alpha Fly",
            "price": '270 $',
            "description": 'Кроссовки для бега',
        },
    ]
    return render_template('shoes.html', content=_shoes)


@app.route('/clothes/')
def clothes():
    _clothes = [
        {
            "name": "Лонгслив Puma",
            "price": '65 $',
            "description": 'Стильная кофта с капюшоном',
        },
        {
            "name": "Футболка Adidas",
            "price": '25 $',
            "description": 'Повседневная футболка',
        },
        {
            "name": "Шорты Nobull",
            "price": '50 $',
            "description": 'Шорты для спорта',
        },
    ]
    return render_template('clothes.html', content=_clothes)


if __name__ == '__main__':
    app.run(debug=True)