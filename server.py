from flask import Flask, render_template
import random
# import time
import datetime as dt

app = Flask(__name__)


def query_api(url, name):
    import requests
    query = {'name': name}
    response = requests.get(url=url, params=query)
    response.raise_for_status()
    return response.json()


@app.route('/')
def home():
    random_int = random.randint(0, 100)
    name = 'John Patmore'
    from_year = '2021'
    # current_year = time.localtime().tm_year
    current_year = dt.datetime.now().year
    return render_template('index.html', name=name, num=random_int, from_year=from_year, current_year=current_year)


@app.route('/guess/<name>')
def guess(name: str):
    name = name.title()
    age = query_api(url='https://api.agify.io', name=name)["age"]
    gender = query_api(url='https://api.genderize.io', name=name)["gender"]
    return render_template('guess.html', name=name, gender=gender, age=age)


@app.route('/blog')
def blog():


    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)

