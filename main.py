#main.py

from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from view_form import UserForm

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:admin123456@hw-db.cnst1jrtc4pc.us-east-1.rds.amazonaws.com:3306/sample"
app.config['SECRET_KEY'] = "hard to guess string"
bootstrap = Bootstrap(app)

db.init_app(app)

class Account(db.Model):
    __tablename__ = 'account'
    memid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30), nullable = False)
    telephone = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    address = db.Column(db.String(50))
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, name, password, telephone, email, address):
        self.name = name
        self.password = password
        self.telephone = telephone
        self.email = email
        self.address = address

@app.route('/')
def index():
    return "hello, world"

@app.route('/user', methods=['GET', 'POST'])
def user():
    form = UserForm()
    formData = {
            'username' : None,
            'password' : None, 
            'telephone' : None, 
            'email' : None,
            'address' : None
    }
    if form.validate_on_submit():
        formData = {
                'username':form.username.data, 
                'password':form.password.data,
                'telephone':form.telephone.data, 
                'email':form.email.data, 
                'address':form.address.data
        }
        session["formData"] = formData
        return redirect(url_for("register"))
    elif form.errors and 'formData' in session:
        del session['formData']
    return render_template('user.html', form=form, formData = session.get("formData"))

@app.route('/register')
def register():
    tmp = session.get('formData')
    account_tmp = Account(tmp['username'], tmp['password'], tmp['telephone'], tmp['email'], tmp['address'])
    db.session.add(account_tmp)
    db.session.commit()
    return redirect(url_for("query"))

@app.route('/query')
def query():
    query = Account.query.all()
    #for i in query:
        #print(i.name)
    return render_template('data.html', table=query)

@app.route('/config-db')
def configdb():
    db.create_all()
    return 'ok'

@app.route('/test')
def test():
    return '<p> test </p> <br>'
