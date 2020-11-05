#main.py

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from view_form import UserForm

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URO'] = "mysql+pymysql://admin:admin123456@hw-db.cnst1jrtc4pc.us-east-1.rds.amazonaws.com:3306/sample"
app.config['SECRET_KEY'] = "hard to guess string"
bootstrap = Bootstrap(app)

db.init_app(app)

class Product(db.Model):
    __tablname__ = 'account'
    memid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30), nullable = False)
    telephone = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    address = db.Column(db.String(50))
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, name, password, telephone, email):
        self.name = name
        self.password = password
        self.telephone = telephone
        self.email = user@mail.com

@app.route('/')
def index():
    return "hello, world"

@app.route('/user', methods=['GET', 'POST'])
def user():
    form = UserForm()
    if form.validate_on_submit():
        return 'Sucess Submit'
    return render_template('user.html', form=form)


@app.route('/config-db')
def configdb():
    db.create_all()
    return 'ok'

@app.route('/test')
def test():
    return '<p> test </p> <br>'
