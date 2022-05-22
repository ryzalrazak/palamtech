from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
import bcrypt 


app = Flask(__name__)
app.secret_key = "membuatLOginFlask1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3307/fypdb'
db = SQLAlchemy(app)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_PORT'] = '3307'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'fypDB'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#mysql = MySQL(app) 

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,name, email, password):
        self.name = name
        self.email = email
        self.password = password

@app.route('/')
def home() :
    if session.get('logged_in'):
        return render_template('index.html', message="WELCOME TO SYSTEM")
    else:
        return render_template('index.html', message="Hello!")

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['email']
        p = request.form['password']
        data = Users.query.filter_by(email=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('home'))
        return render_template('home.html', message="Incorrect Details")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(Users(name=request.form['name'],email=request.form['email'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('home.html', message="User Already Exists")
    else:
        return render_template('register.html')

@app.route('/about')
def about():
    if 'email' in session:
        return render_template("about.html")
    else:
        return redirect(url_for('home'))

    
@app.route('/portfolio')
def portfolio():

    if session.get('logged_in'):
        return render_template('portfolio.html')
    else:
        return redirect(url_for('home')) 
@app.route('/contact')
def contact():
    if 'email' in session:
        return render_template("contact.html")
    else:
        return redirect(url_for('home')) 
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home')) 

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)