from flask import Flask, render_template, request, session, redirect, url_for, session
import pymongo
#import bcrypt



# Conexión
myClient = pymongo.MongoClient("mongodb://localhost:27017")
myDb = myClient["talesapp"] #database
myCollection = myDb["tales"] #collection
myCavanas = myDb["cavanas"] #collection

app = Flask(__name__)




@app.route('/login', methods=["POST", "GET"])  # decorador)
def login():
  if request.method == "POST":
    users = myCollection
    
    existing_user = users.find_one({'name' : request.form['username']})
    if existing_user:
      if request.form['password'] == existing_user['password']:
        return redirect(url_for('index'))
    return 'Invalid username/password combination'
    
  return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])  # decorador)
def register():
    if request.method == "POST":
      users =myCollection
      existing_user = users.find_one({'name' : request.form['username']})
      
      if existing_user is None:
        name = request.form['username']
        EMail = request.form['EMail']
        Country = request.form['Country']
        city = request.form['city']
        password = request.form['password']
        rol_name = request.form['rol_name']
        users.insert({'name' : name, 'EMail' : EMail, 'Country' : Country, 'city' : city, 'password' : password,'rol_name' : rol_name})
        return redirect(url_for('index'))
        
      return 'That username already exists!'

    return render_template('register.html')



@app.route('/index')
def home():
  return render_template('index.html')

  

@app.route('/')
def index():
  return render_template('index.html')

# @app.route('/news')
# def news():
#   return  render_template("news.html")

  
# @app.route('/register')
# def register():
#   return render_template("register.html")

# @app.route('/login')
# def login():
#   return  render_template("login.html")


# @app.route('/register', methods=["POST", "GET"])  # decorador 
# def register():
#   mytales = {"name": "Estudiar python con flask", "date":"24/04/2021" }
#     result = myCollection.insert_one(mytales)
# inserData()
 


if __name__ == '__main__':
     app.run(debug=True)