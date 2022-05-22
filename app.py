from http.client import FORBIDDEN
from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import bcrypt 


app = Flask(__name__)
app.secret_key = "membuatLOginFlask1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/palamtech'
db = SQLAlchemy(app)


# # Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Customer(db.Model,UserMixin):
    customer = "parents"
    id = db.Column(db.Integer, unique=True)
    custEmail = db.Column(db.String(255), primary_key=True)
    custName = db.Column(db.String(255),)
    custPhoneNo = db.Column(db.String(255)) 
    custAdd = db.Column(db.String(255)) 
    custPass = db.Column(db.String(255))
    childrens = db.relationship("child", backref = "parents"), 
    cascade ="all, delete"
   #customer = db.relationship('Customer', backref='feedback', lazy=True)
    
       
    def __init__(self,custEmail, custName, custPhoneNo,custAdd,custPass):
        self.custEmail = custEmail
        self.custName = custName
        self.custPhoneNo = custPhoneNo
        self.custAdd = custAdd
        self.custPass = custPass
        
       
@login_manager.user_loader
def load_user(user_id):
    return Customer.query.filter_by(id=user_id).first()
    
class Admin(db.Model):
    adminID = db.Column(db.Integer, primary_key=True)
    adminName = db.Column(db.String(255))
    adminEmail = db.Column(db.String(255), unique=True)
    adminPass = db.Column(db.String(255)) 

    def __init__(self,adminName, adminEmail, adminPass):
        self.adminName = adminName
        self.adminEmail = adminEmail
        self.adminPass = adminPass
        
class Feedbacks(db.Model):
    feedbacks = "children"
    fbID = db.Column(db.Integer, primary_key=True)
    custEmail = db.Column(db.String, db.ForeignKey('customer.custEmail'),
    nullable=False)
    fbDate = db.Column(db.DateTime)
    fbType = db.Column(db.String(255))
    fbDesc = db.Column(db.String(255))
    
    

    def __init__(self,custEmail, fbType,fbDate, fbDesc):
        
        self.custEmail = custEmail
        self.fbType = fbType
        self.fbDate = fbDate
        self.fbDesc = fbDesc

class Component(db.Model):
    component = "children"
    compID = db.Column(db.Integer, primary_key=True)
    catID = db.Column(db.Integer, db.ForeignKey('category.catID'),
        nullable=False)
    compName = db.Column(db.String(255))
    compBrand = db.Column(db.String(255))
    compPrice = db.Column(db.Float())
    

    def __init__(self,catID, compName, compBrand, compPrice):
        
        self.catID = catID
        self.compName = compName
        self.compBrand = compBrand
        self.compPrice = compPrice
   
        
class Category(db.Model):
    # category = 'parents'
    catID = db.Column(db.Integer, primary_key=True)
    catName = db.Column(db.String(255))
    component = db.relationship('Component', backref='category', lazy=True)

    def __init__(self,catName):
        self.catName = catName

class BuildPC(db.Model):
    buildPC = "children"
    pcID = db.Column(db.Integer, primary_key=True)
    casing = db.Column(db.Integer, db.ForeignKey("component.compID"),
    nullable=False)
    mb = db.Column(db.Integer, db.ForeignKey("component.compID"),
    nullable=False)
    gpu = db.Column(db.Integer, db.ForeignKey("component.compID"),
    nullable=False)
    ram = db.Column(db.Integer, db.ForeignKey("component.compID"),
    nullable=False)
    storage = db.Column(db.Integer, db.ForeignKey("component.compID"),
    nullable=False)
    psu = db.Column(db.Integer, db.ForeignKey("component.compID"),
    nullable=False)
    cpu = db.Column(db.Integer, db.ForeignKey("component.compID"),
    nullable=False)
    

    def __init__(self,casing, mb, gpu,ram,storage,psu,cpu):
        
        self.casing = casing
        self.mb = mb
        self.gpu = gpu
        self.ram = ram
        self.storage = storage       
        self.psu = psu
        self.cpu = cpu
        



        
@app.route('/')
def index() :    
    return render_template('index.html', message="WELCOME TO PALAMTECH PC BUILDER")


@app.route('/home')
def home() :           
        return render_template('home.html', message="WELCOME TO PALAMTECH PC BUILDER")
    
@app.route('/selfbuildin')
def selfbuildin():
    return render_template("product-self1.html")

@app.route('/question')
def question():
            return render_template('question.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login(): 
#     if request.method == 'GET':
#         return render_template('login.html',)
#     else:
#         c = request.form['custEmail']
#         p = request.form['custPass']
#         customer = Customer.query.filter_by(custEmail=c, custPass=p).first()
#         if customer is not None:
#             session['logged_in'] = True
#             return redirect(url_for('home'))
#         else:
#             return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        custEmail = request.form['custEmail']
        custPass = request.form['custPass']
        customer = Customer.query.filter_by(custEmail=custEmail).first()
        if customer:
            if customer.custPass == custPass:
                 login_user(customer)
                 return redirect(url_for('home'))
        else:

            return "invalid email or password"
    return render_template("login.html") 
     
     
        
@app.route('/loginAdmin', methods=['GET', 'POST'])
def loginAdmin(): 
    if request.method == 'GET':
        return render_template('loginAdmin.html')
    else:
        c = request.form['adminEmail']
        p = request.form['adminPass']
        data = Admin.query.filter_by(adminEmail=c, adminPass=p).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('allcust'))
        else:
            return redirect(url_for('loginAdmin'))




@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(Customer(custName=request.form['custName'],custEmail=request.form['custEmail'],custPhoneNo=request.form['custPhoneNo'],custAdd=request.form['custAdd'], custPass=request.form['custPass']))
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('home.html', message="User Already Exists")
    else:
        return render_template('register.html')

@app.route('/about')
def about():
            return render_template('about.html', message="WELCOME TO PALAMTECH PC BUILDER")

    
@app.route('/aboutbeforelogin')
def aboutbeforelogin():
    return render_template('aboutbeforelogin.html')
     
@app.route('/contact')
def contact():
            return render_template('contact.html', message="WELCOME TO PALAMTECH PC BUILDER")

    
@app.route('/writefeedback', methods=['POST', 'GET'])
def writefeedback():
    
    if request.method == 'POST':
            db.session.add(Feedbacks(custEmail=request.form['custEmail'],fbType=request.form['fbType'],fbDate=request.form['fbDate'],fbDesc=request.form['fbDesc']))
            db.session.commit()
            return redirect(url_for('myfeedback'))
    else:
        return render_template('writefeedback.html')
 
    
@app.route('/myfeedback')
def myfeedback():
         custEmail = current_user.custEmail
         result = db.engine.execute("SELECT * FROM feedbacks WHERE custEmail = %s",custEmail)
         return render_template("myfeedback.html", feedbacks = result)

    

@app.route('/contactbeforelogin')
def contactbeforelogin():
    return render_template("contactbeforelogin.html")


    
    
@app.route('/insert')
def insert():
    if request.method =='POST':
        
        custName = request.form['custName']
        custEmail = request.form['custEmail']
        custPhoneNo = request.form['custPhoneNo']
        custAdd = request.form['custAdd']
        custPass = request.form['custPass']
        
        my_data = Customer(custName,custEmail,custPhoneNo,custAdd,custPass)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('home'))
    
@app.route('/productself1')
def productself1():
            return render_template('productself1.html')

    


@app.route('/allcust')
def allcust():
         all_data = Customer.query.all()
         return render_template("allcust.html", customer = all_data)

    
@app.route('/feedbacks')
def feedbacks():
         result = db.engine.execute("SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail)")
        #all_data = text('SELECT feedbacks.fbID,customer.custID,customer.custName,feedbacks.fbType,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.fbID = customer.custID)')
         #all_data = Feedbacks.query.all()
         return render_template("feedbacks.html", feedbacks = result)

    
@app.route('/complaints')
def complaints():
         result = db.engine.execute("SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail) WHERE fbType = 'Complain'")
         return render_template("complaints.html", complaints = result)

    
@app.route('/suggestions')
def suggestions():
         result = db.engine.execute("SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail) WHERE fbType = 'Suggestions'")
         return render_template("suggestions.html", suggestions = result)
    
@app.route('/reviews')
def reviews():
         result = db.engine.execute("SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail) WHERE fbType = 'Review'")
         return render_template("reviews.html", reviews = result)

    

    
@app.route('/component')
def component():
         result = db.engine.execute("SELECT component.compID,category.catName,component.compName,component.compBrand,component.compPrice FROM component INNER JOIN category ON (component.catID = category.catID) ORDER BY 1 ")
         return render_template("component.html", component = result)


@app.route('/allpackage')
def allpackage():
         result = db.engine.execute("SELECT component.compID,category.catName,component.compName,component.compBrand,component.compPrice FROM component INNER JOIN category ON (component.catID = category.catID) ORDER BY 1 ")
         return render_template("component.html", component = result)

    
    
@app.route('/addcomponent', methods=['POST', 'GET'])
def addcomponent():
    
    if request.method == 'POST':
        
            
            db.session.add(Component(catID=request.form['catID'],compName=request.form['compName'],compBrand=request.form['compBrand'],compPrice=request.form['compPrice']))
            db.session.commit()
            return redirect('/component')
            
        
    else:
        return render_template('addcomponent.html')
    
@app.route('/addpackage', methods=['POST', 'GET'])
def addpackage():
    rcasing = db.engine.execute("SELECT compID, compName FROM component WHERE catID =1")
    rmobo = db.engine.execute("SELECT compID, compName FROM component WHERE catID =2")
    rgpu = db.engine.execute("SELECT compID, compName FROM component WHERE catID =3")
    rram = db.engine.execute("SELECT compID, compName FROM component WHERE catID =4")
    rstorage = db.engine.execute("SELECT compID, compName FROM component WHERE catID =5")
    rpsu = db.engine.execute("SELECT compID, compName FROM component WHERE catID =6")
    rcpu = db.engine.execute("SELECT compID, compName FROM component WHERE catID =7")
    if request.method == 'POST':
            
            
            db.session.add(BuildPC(casing=request.form['casing'],mb=request.form['mb'],gpu=request.form['gpu'],ram=request.form['ram'],storage=request.form['storage'],psu=request.form['psu'],cpu=request.form['cpu']))
            db.session.commit()
            return redirect('/allcust')

            
        
    else:
        return render_template('addpackage.html',casing=rcasing,mobo=rmobo,gpu=rgpu,ram=rram,storage=rstorage,psu=rpsu,cpu=rcpu)




@app.route('/updatecomponent/<int:compID>',methods = ['GET','POST'])
def updatecomponent(compID):
    #category = Category.query.filter_by(catID=catID).first()
    all_data = Category.query.all()
    component_to_update = Component.query.filter_by(compID=compID).first()
    if request.method == 'POST':
        # print(request.form['catID'])
        # print(request.form['compName'])
        
        
        # if component_to_update:
            
           
        component_to_update.catID = request.form['catID']
        component_to_update.compName = request.form['compName']
        component_to_update.compBrand = request.form['compBrand']
        component_to_update.compPrice = request.form['compPrice']
        component_to_update.component = Component(catID =component_to_update.catID ,compName=component_to_update.compName, compBrand=component_to_update.compBrand, compPrice = component_to_update.compPrice)
            
        
        db.session.commit()
        return redirect('/component')
            # return f"Component with id = {compID} Does not exist"
 
    return render_template('updatecomponent.html',component_to_update=component_to_update, category=all_data)  


@app.route('/updatefeedback/<int:fbID>',methods = ['GET','POST'])
def updatefeedback(fbID):
    
    all_data = Feedbacks.query.all()
    feedback_to_update = Feedbacks.query.filter_by(fbID=fbID).first()
    if request.method == 'POST':
   
        feedback_to_update.custEmail = request.form['custEmail']
        feedback_to_update.fbType = request.form['fbType']
        feedback_to_update.fbDate = request.form['fbDate']
        feedback_to_update.fbDesc = request.form['fbDesc']
        feedback_to_update.feedback = Feedbacks(custEmail=feedback_to_update.custEmail, fbType=feedback_to_update.fbType, fbDate = feedback_to_update.fbDate, fbDesc = feedback_to_update.fbDesc)
            
        
        db.session.commit()
        return redirect('/myfeedback')
 
    return render_template('updatefeedback.html',feedback_to_update=feedback_to_update, feedback=all_data)          


@app.route('/deletecomponent/<int:compID>')
def deletecomponent(compID):
    component_to_delete = Component.query.get_or_404(compID)
    
    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/component')
    except:
        return "There was a problem deleting the component"
    
@app.route('/deletefeedback/<int:fbID>')
def deletefeedback(fbID):
    feedback_to_delete = Feedbacks.query.get_or_404(fbID)
    
    try:
        db.session.delete(feedback_to_delete)
        db.session.commit()
        return redirect('/myfeedback')
    except:
        return "There was a problem deleting the component"

    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index')) 

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)