from flask import Flask
from flask_mysqldb import MySQL
from app.clientesbp.clientesbp import clientes_blueprint

app = Flask(__name__)

app.register_blueprint(clientes_blueprint)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{root}:{}@{localhost}/testadb".format(username, password, server)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@server/db"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/testadb'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret@@@##$)(*&¨%$#@'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'testadb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from app.controllers import default
