from flask import Flask, redirect, url_for, render_template
from random import randint

app = Flask(__name__)
app.config.from_object('config')
blogs_data = {
  'chocolate-chip' : {'name': 'Chocolate Chip', 'price': '$1.50'},
  'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': '$1.00'},
  'sugar' : {'name': 'Sugar', 'price': '$0.75'},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': '$0.50'},
  'oatmeal' : {'name': 'Oatmeal', 'price': '$0.25'},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': '$1.00'},
}

@app.route('/')
def index():
    return render_template('index.html', blogs=blogs_data)
    


@app.route('/about-me')
def about_me():
  return redirect(url_for('/about'))
# Dynamic routes
@app.route('/blogs/<slug>')
def blog(slug):
  return '<h1>' + blogs_data[slug]['name'] + '</h1><p>' + blogs_data[slug]['price'] + '</p>'


if __name__ == '__main__':
 app.run(host="0.0.0.0", port=8080)
 