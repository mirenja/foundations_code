from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
app.config.from_object('config')


@app.route('/city/<placeholder>')
def city(placeholder):
  cities = {
    'berlin': {'name': 'Berlin', 'address': '/images/berlin.jpg'},
    'konstanz': {'name': 'Konstanz', 'address': '/images/konstanz.jpg'},
    'heidelberg': {'name': 'Heidelberg', 'address': '/images/heidelberg.jpg'}}

  city_displayed = cities[placeholder]['name']
  city_link = cities[placeholder]['address']
  return render_template('city.html', city=city_displayed, new_add=city_link)

@app.route('/')
def index():
    cities = {
    'berlin': {'name': 'Berlin', 'address': '/images/berlin.jpg'},
    'konstanz': {'name': 'Konstanz', 'address': '/images/konstanz.jpg'},
    'heidelberg': {'name': 'Heidelberg', 'address': '/images/heidelberg.jpg'}}

    return render_template('index.html', cities=cities)


@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/signUp')
def signUp():
  return render_template('signUp.html')





if __name__ == '__main__':
  app.run()
