from http.client import FORBIDDEN
from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


app = Flask(__name__)
app.secret_key = "membuatLOginFlask1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/palamtech'
db = SQLAlchemy(app)


# # Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Users(db.Model):
   # customer = "parents"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(255))

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role


class Customer(db.Model, UserMixin):
    customer = "parents"
    id = db.Column(db.Integer, primary_key=True)
    custEmail = db.Column(db.String(255), unique=True)
    custName = db.Column(db.String(255))
    custPhoneNo = db.Column(db.String(255))
    custAdd = db.Column(db.String(255))
    custPass = db.Column(db.String(255))
    childrens = db.relationship("child", backref="parents"),
    cascade = "all, delete"
   #customer = db.relationship('Customer', backref='feedback', lazy=True)

    def __init__(self, custEmail, custName, custPhoneNo, custAdd, custPass):
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

    def __init__(self, adminName, adminEmail, adminPass):
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

    def __init__(self, custEmail, fbType, fbDate, fbDesc):

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

    def __init__(self, catID, compName, compBrand, compPrice):

        self.catID = catID
        self.compName = compName
        self.compBrand = compBrand
        self.compPrice = compPrice


class Casing(db.Model):
    casing = "children"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float())

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Mb(db.Model):
    mb = "children"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float())

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Gpu(db.Model):
    gpu = "children"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float())

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Ram(db.Model):
    ram = "children"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float())

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Ssd(db.Model):
    ssd = "children"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float())

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Psu(db.Model):
    psu = "children"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float())

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Cpu(db.Model):
    cpu = "children"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float())

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

# class Category(db.Model):
#     # category = 'parents'
#     catID = db.Column(db.Integer, primary_key=True)
#     catName = db.Column(db.String(255))
#     component = db.relationship('Component', backref='category', lazy=True)

#     def __init__(self,catName):
#         self.catName = catName


class Pcpackage(db.Model):
    pcpackage = "children"
    id = db.Column(db.Integer, primary_key=True)
    casing = db.Column(db.Integer, db.ForeignKey("casing.id"),
                       nullable=False)
    mb = db.Column(db.Integer, db.ForeignKey("mb.id"),
                   nullable=False)
    gpu = db.Column(db.Integer, db.ForeignKey("gpu.id"),
                    nullable=False)
    ram = db.Column(db.Integer, db.ForeignKey("ram.id"),
                    nullable=False)
    ssd = db.Column(db.Integer, db.ForeignKey("ssd.id"),
                    nullable=False)
    psu = db.Column(db.Integer, db.ForeignKey("psu.id"),
                    nullable=False)
    cpu = db.Column(db.Integer, db.ForeignKey("gpu.id"),
                    nullable=False)

    def __init__(self, casing, mb, gpu, ram, ssd, psu, cpu):

        self.casing = casing
        self.mb = mb
        self.gpu = gpu
        self.ram = ram
        self.ssd = ssd
        self.psu = psu
        self.cpu = cpu


# end of models


@app.route('/')
def index():
    return render_template('index.html', message="WELCOME TO PALAMTECH PC BUILDER")


@app.route('/home')
def home():
    return render_template('home.html', message="WELCOME TO PALAMTECH PC BUILDER")


@app.route('/selfbuildin')
def selfbuildin():
    return render_template("product-self1.html")


@app.route('/question')
def question():
    return render_template('question.html')


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
            db.session.add(Users(
                email=request.form['custEmail'], password=request.form['custPass'], role="customer"))
            db.session.add(Customer(custName=request.form['custName'], custEmail=request.form['custEmail'],
                           custPhoneNo=request.form['custPhoneNo'], custAdd=request.form['custAdd'], custPass=request.form['custPass']))

            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
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
        db.session.add(Feedbacks(custEmail=request.form['custEmail'], fbType=request.form['fbType'],
                       fbDate=request.form['fbDate'], fbDesc=request.form['fbDesc']))
        db.session.commit()
        return redirect(url_for('myfeedback'))
    else:
        return render_template('writefeedback.html')


@app.route('/myfeedback')
def myfeedback():
    custEmail = current_user.custEmail
    result = db.engine.execute(
        "SELECT * FROM feedbacks WHERE custEmail = %s", custEmail)
    return render_template("myfeedback.html", feedbacks=result)


@app.route('/contactbeforelogin')
def contactbeforelogin():
    return render_template("contactbeforelogin.html")


@app.route('/insert')
def insert():
    if request.method == 'POST':

        custName = request.form['custName']
        custEmail = request.form['custEmail']
        custPhoneNo = request.form['custPhoneNo']
        custAdd = request.form['custAdd']
        custPass = request.form['custPass']

        my_data = Customer(custName, custEmail, custPhoneNo, custAdd, custPass)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/productself1')
def productself1():
    return render_template('productself1.html')


@app.route('/allcust')
def allcust():
    all_data = Customer.query.all()
    return render_template("allcust.html", customer=all_data)


# @app.route('/allpackage')
# def allpackage():
#     result = db.engine.execute("SELECT pcpackage.id, casing.name "Casing", mb.name "Motherboard",gpu.name"GPU",ram.name"RAM",ssd.name"Storage",psu.name"PSU",cpu.name"CPU",casing.price+mb.price+gpu.price+ram.price+ssd.price+psu.price+cpu.price AS "Price" FROM pcpackage JOIN casing ON (pcpackage.casing=casing.id) JOIN mb ON (pcpackage.mb=mb.id) JOIN gpu ON (pcpackage.gpu = gpu.id) JOIN ram ON (pcpackage.ram=ram.id) JOIN ssd ON (pcpackage.ssd=ssd.id) JOIN psu ON (pcpackage.psu=psu.id) JOIN cpu ON (pcpackage.cpu=cpu.id)")
#     return render_template("allpackage.html", package=result)


@app.route('/feedbacks')
def feedbacks():
    result = db.engine.execute(
        "SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail)")

    return render_template("feedbacks.html", feedbacks=result)


@app.route('/complaints')
def complaints():
    result = db.engine.execute(
        "SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail) WHERE fbType = 'Complain'")
    return render_template("complaints.html", complaints=result)


@app.route('/suggestions')
def suggestions():
    result = db.engine.execute(
        "SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail) WHERE fbType = 'Suggestions'")
    return render_template("suggestions.html", suggestions=result)


@app.route('/reviews')
def reviews():
    result = db.engine.execute(
        "SELECT feedbacks.fbID,customer.custEmail,customer.custName,feedbacks.fbType,feedbacks.fbDate,feedbacks.fbDesc FROM feedbacks INNER JOIN customer ON (feedbacks.custEmail = customer.custEmail) WHERE fbType = 'Review'")
    return render_template("reviews.html", reviews=result)


@app.route('/component')
def component():
    result = db.engine.execute(
        "SELECT component.compID,category.catName,component.compName,component.compBrand,component.compPrice FROM component INNER JOIN category ON (component.catID = category.catID) ORDER BY 1 ")
    return render_template("component.html", component=result)


@app.route('/addcomponent', methods=['POST', 'GET'])
def addcomponent():

    if request.method == 'POST':

        db.session.add(Component(catID=request.form['catID'], compName=request.form['compName'],
                       compBrand=request.form['compBrand'], compPrice=request.form['compPrice']))
        db.session.commit()
        return redirect('/component')

    else:
        return render_template('addcomponent.html')


@app.route('/addcasing', methods=['POST', 'GET'])
def addcasing():
    all_data = Casing.query.all()
    if request.method == 'POST':

        db.session.add(Casing(
            name=request.form['name'], brand=request.form['brand'], price=request.form['price']))
        db.session.commit()

        return redirect('/addcasing')

    else:
        return render_template('addcasing.html', casing=all_data)


@app.route('/addmb', methods=['POST', 'GET'])
def addmb():
    all_data = Mb.query.all()
    if request.method == 'POST':

        db.session.add(
            Mb(name=request.form['name'], brand=request.form['brand'], price=request.form['price']))
        db.session.commit()

        return redirect('/addmb')

    else:
        return render_template('addmb.html', mb=all_data)


@app.route('/addgpu', methods=['POST', 'GET'])
def addgpu():
    all_data = Gpu.query.all()
    if request.method == 'POST':

        db.session.add(Gpu(
            name=request.form['name'], brand=request.form['brand'], price=request.form['price']))
        db.session.commit()

        return redirect('/addgpu')

    else:
        return render_template('addgpu.html', gpu=all_data)


@app.route('/addram', methods=['POST', 'GET'])
def addram():
    all_data = Ram.query.all()
    if request.method == 'POST':

        db.session.add(Ram(
            name=request.form['name'], brand=request.form['brand'], price=request.form['price']))
        db.session.commit()

        return redirect('/addram')

    else:
        return render_template('addram.html', ram=all_data)


@app.route('/addssd', methods=['POST', 'GET'])
def addssd():
    all_data = Ssd.query.all()
    if request.method == 'POST':

        db.session.add(Ssd(
            name=request.form['name'], brand=request.form['brand'], price=request.form['price']))
        db.session.commit()

        return redirect('/addssd')

    else:
        return render_template('addssd.html', ssd=all_data)


@app.route('/addpsu', methods=['POST', 'GET'])
def addpsu():
    all_data = Psu.query.all()
    if request.method == 'POST':

        db.session.add(Psu(
            name=request.form['name'], brand=request.form['brand'], price=request.form['price']))
        db.session.commit()

        return redirect('/addpsu')

    else:
        return render_template('addpsu.html', psu=all_data)


@app.route('/addcpu', methods=['POST', 'GET'])
def addcpu():
    all_data = Cpu.query.all()
    if request.method == 'POST':

        db.session.add(Cpu(
            name=request.form['name'], brand=request.form['brand'], price=request.form['price']))
        db.session.commit()

        return redirect('/addcpu')

    else:
        return render_template('addcpu.html', cpu=all_data)

# @app.route('/addpackage', methods=['POST', 'GET'])
# def addpackage():
#     rcasing = db.engine.execute("SELECT compID, compName FROM component WHERE catID =1")
#     rmobo = db.engine.execute("SELECT compID, compName FROM component WHERE catID =2")
#     rgpu = db.engine.execute("SELECT compID, compName FROM component WHERE catID =3")
#     rram = db.engine.execute("SELECT compID, compName FROM component WHERE catID =4")
#     rstorage = db.engine.execute("SELECT compID, compName FROM component WHERE catID =5")
#     rpsu = db.engine.execute("SELECT compID, compName FROM component WHERE catID =6")
#     rcpu = db.engine.execute("SELECT compID, compName FROM component WHERE catID =7")
#     if request.method == 'POST':


#             db.session.add(BuildPC(casing=request.form['casing'],mb=request.form['mb'],gpu=request.form['gpu'],ram=request.form['ram'],storage=request.form['storage'],psu=request.form['psu'],cpu=request.form['cpu']))
#             db.session.commit()
#             return redirect('/allcust')

@app.route('/addpackage', methods=['POST', 'GET'])
def addpackage():
    rcasing = db.engine.execute("SELECT id, name FROM casing")
    rmobo = db.engine.execute("SELECT id, name FROM mb")
    rgpu = db.engine.execute("SELECT id, name FROM gpu")
    rram = db.engine.execute("SELECT id, name FROM ram")
    rstorage = db.engine.execute("SELECT id, name FROM ssd")
    rpsu = db.engine.execute("SELECT id, name FROM psu")
    rcpu = db.engine.execute("SELECT id, name FROM cpu")
    if request.method == 'POST':

        db.session.add(Pcpackage(casing=request.form['casing'], mb=request.form['mb'], gpu=request.form['gpu'],
                       ram=request.form['ram'], ssd=request.form['ssd'], psu=request.form['psu'], cpu=request.form['cpu']))
        db.session.commit()
        return redirect('/allcust')

    else:
        return render_template('addpackage.html', casing=rcasing, mobo=rmobo, gpu=rgpu, ram=rram, storage=rstorage, psu=rpsu, cpu=rcpu)


@app.route('/updatecasing/<int:id>', methods=['GET', 'POST'])
def updatecasing(id):
    component_to_update = Casing.query.filter_by(id=id).first()
    if request.method == 'POST':
        component_to_update.name = request.form['name']
        component_to_update.brand = request.form['brand']
        component_to_update.price = request.form['price']
        component_to_update.component = Casing(
            name=component_to_update.name, brand=component_to_update.brand, price=component_to_update.price)
        db.session.commit()
        return redirect('/addcasing')
    return render_template('updatecasing.html', component_to_update=component_to_update)


@app.route('/updatemb/<int:id>', methods=['GET', 'POST'])
def updatemb(id):
    component_to_update = Mb.query.filter_by(id=id).first()
    if request.method == 'POST':
        component_to_update.name = request.form['name']
        component_to_update.brand = request.form['brand']
        component_to_update.price = request.form['price']
        component_to_update.component = Mb(
            name=component_to_update.name, brand=component_to_update.brand, price=component_to_update.price)
        db.session.commit()
        return redirect('/addmb')
    return render_template('updatemb.html', component_to_update=component_to_update)


@app.route('/updategpu/<int:id>', methods=['GET', 'POST'])
def updategpu(id):
    component_to_update = Gpu.query.filter_by(id=id).first()
    if request.method == 'POST':
        component_to_update.name = request.form['name']
        component_to_update.brand = request.form['brand']
        component_to_update.price = request.form['price']
        component_to_update.component = Gpu(
            name=component_to_update.name, brand=component_to_update.brand, price=component_to_update.price)
        db.session.commit()
        return redirect('/addgpu')
    return render_template('updategpu.html', component_to_update=component_to_update)


@app.route('/updateram/<int:id>', methods=['GET', 'POST'])
def updateram(id):
    component_to_update = Ram.query.filter_by(id=id).first()
    if request.method == 'POST':
        component_to_update.name = request.form['name']
        component_to_update.brand = request.form['brand']
        component_to_update.price = request.form['price']
        component_to_update.component = Ram(
            name=component_to_update.name, brand=component_to_update.brand, price=component_to_update.price)
        db.session.commit()
        return redirect('/addram')
    return render_template('updateram.html', component_to_update=component_to_update)


@app.route('/updatessd/<int:id>', methods=['GET', 'POST'])
def updatessd(id):
    component_to_update = Ssd.query.filter_by(id=id).first()
    if request.method == 'POST':
        component_to_update.name = request.form['name']
        component_to_update.brand = request.form['brand']
        component_to_update.price = request.form['price']
        component_to_update.component = Ssd(
            name=component_to_update.name, brand=component_to_update.brand, price=component_to_update.price)
        db.session.commit()
        return redirect('/addssd')
    return render_template('updatessd.html', component_to_update=component_to_update)


@app.route('/updatepsu/<int:id>', methods=['GET', 'POST'])
def updatepsu(id):
    component_to_update = Psu.query.filter_by(id=id).first()
    if request.method == 'POST':
        component_to_update.name = request.form['name']
        component_to_update.brand = request.form['brand']
        component_to_update.price = request.form['price']
        component_to_update.component = Psu(
            name=component_to_update.name, brand=component_to_update.brand, price=component_to_update.price)
        db.session.commit()
        return redirect('/addpsu')
    return render_template('updatepsu.html', component_to_update=component_to_update)


@app.route('/updatecpu/<int:id>', methods=['GET', 'POST'])
def updatecpu(id):
    component_to_update = Cpu.query.filter_by(id=id).first()
    if request.method == 'POST':
        component_to_update.name = request.form['name']
        component_to_update.brand = request.form['brand']
        component_to_update.price = request.form['price']
        component_to_update.component = Cpu(
            name=component_to_update.name, brand=component_to_update.brand, price=component_to_update.price)
        db.session.commit()
        return redirect('/addcpu')
    return render_template('updatecpu.html', component_to_update=component_to_update)
# @app.route('/updatecomponent/<int:compID>',methods = ['GET','POST'])
# def updatecomponent(compID):
#     #category = Category.query.filter_by(catID=catID).first()
#     all_data = Category.query.all()
#     component_to_update = Component.query.filter_by(compID=compID).first()
#     if request.method == 'POST':
#         # print(request.form['catID'])
#         # print(request.form['compName'])


#         # if component_to_update:


#         component_to_update.catID = request.form['catID']
#         component_to_update.compName = request.form['compName']
#         component_to_update.compBrand = request.form['compBrand']
#         component_to_update.compPrice = request.form['compPrice']
#         component_to_update.component = Component(catID =component_to_update.catID ,compName=component_to_update.compName, compBrand=component_to_update.compBrand, compPrice = component_to_update.compPrice)


#         db.session.commit()
#         return redirect('/component')
#             # return f"Component with id = {compID} Does not exist"

#     return render_template('updatecomponent.html',component_to_update=component_to_update, category=all_data)


@app.route('/updatefeedback/<int:fbID>', methods=['GET', 'POST'])
def updatefeedback(fbID):

    all_data = Feedbacks.query.all()
    feedback_to_update = Feedbacks.query.filter_by(fbID=fbID).first()
    if request.method == 'POST':

        feedback_to_update.custEmail = request.form['custEmail']
        feedback_to_update.fbType = request.form['fbType']
        feedback_to_update.fbDate = request.form['fbDate']
        feedback_to_update.fbDesc = request.form['fbDesc']
        feedback_to_update.feedback = Feedbacks(
            custEmail=feedback_to_update.custEmail, fbType=feedback_to_update.fbType, fbDate=feedback_to_update.fbDate, fbDesc=feedback_to_update.fbDesc)

        db.session.commit()
        return redirect('/myfeedback')

    return render_template('updatefeedback.html', feedback_to_update=feedback_to_update, feedback=all_data)


# @app.route('/deletecomponent/<int:compID>')
# def deletecomponent(compID):
#     component_to_delete = Component.query.get_or_404(compID)

#     try:
#         db.session.delete(component_to_delete)
#         db.session.commit()
#         return redirect('/component')
#     except:
#         return "There was a problem deleting the component"

@app.route('/deletecasing/<int:id>')
def deletecasing(id):
    component_to_delete = Casing.query.get_or_404(id)

    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/addcasing')
    except:
        return "There was a problem deleting the component"


@app.route('/deletemb/<int:id>')
def deletemb(id):
    component_to_delete = Mb.query.get_or_404(id)

    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/addmb')
    except:
        return "There was a problem deleting the component"


@app.route('/deletegpu/<int:id>')
def deletegpu(id):
    component_to_delete = Gpu.query.get_or_404(id)

    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/addgpu')
    except:
        return "There was a problem deleting the component"


@app.route('/deleteram/<int:id>')
def deleteram(id):
    component_to_delete = Ram.query.get_or_404(id)

    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/addram')
    except:
        return "There was a problem deleting the component"


@app.route('/deletessd/<int:id>')
def deletessd(id):
    component_to_delete = Ssd.query.get_or_404(id)

    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/addssd')
    except:
        return "There was a problem deleting the component"


@app.route('/deletepsu/<int:id>')
def deletepsu(id):
    component_to_delete = Psu.query.get_or_404(id)

    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/addpsu')
    except:
        return "There was a problem deleting the component"


@app.route('/deletecpu/<int:id>')
def deletecpu(id):
    component_to_delete = Cpu.query.get_or_404(id)

    try:
        db.session.delete(component_to_delete)
        db.session.commit()
        return redirect('/addcpu')
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
