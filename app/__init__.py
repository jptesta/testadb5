from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{root}:{}@{localhost}/testadb".format(username, password, server)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@server/db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/testadb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['secret_key'] = 'secret@@@##$)(*&¨%$#@'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'testadb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from app.controllers import default
