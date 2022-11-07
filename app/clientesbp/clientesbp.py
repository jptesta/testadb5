from flask import Blueprint, render_template
from flask_mysqldb import MySQLdb
from app import mysql

clientes_blueprint = Blueprint('clientes', __name__, template_folder='templates')


@clientes_blueprint.route('/clientesbp')
def clitentebp():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(''' SELECT * FROM clientes''')
    clientes = cur.fetchall()
    return render_template('clientesbp.html', clientes=clientes)
