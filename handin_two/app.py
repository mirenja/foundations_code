from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
app.config.from_object('config')

cities = {
    'berlin': {'name': 'Berlin', 'address': '/images/berlin.jpg'},
    'konstanz': {'name': 'Konstanz', 'address': '/images/konstance.jpg'},
    'heidelberg': {'name': 'Heidelberg', 'address': '/images/heidelberg.jpg'}
  }
@app.route('/')
def index():
    
    return render_template('index.html', cities=cities)
@app.route('/city/<placeholder>')
def city(placeholder):
#move the city dict outside fxn

  if placeholder in cities:
    city_displayed = cities[placeholder]['name']
    city_link = cities[placeholder]['address']
  else:
    return "City not found"

  return render_template('city.html', city=city_displayed, added_url=city_link)




@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/signUp')
def signUp():
  return render_template('signUp.html')





if __name__ == '__main__':
  app.run()
