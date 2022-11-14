from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL, MySQLdb

mysql = MySQL()


transportadora_blueprint = Blueprint ('transportadoras', __name__, template_folder='templates')


# CADASTRO DE TRANSPORTADORA
@transportadora_blueprint.route('/transportadora', methods=['GET', 'POST'])
def transportadora():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('''SELECT * FROM transportadoras''')
    if request.method == "POST":
        transportadora = request.form['transportadora']
        cidade = request.form['cidade']
        estado = request.form['estado']
        telefone = request.form['telefone']
        cur = mysql.connection.cursor()
        cur.execute( ''' INSERT INTO transportadoras(transportadora, cidade, estado, telefone) 
                         VALUES (%s, %s, %s, %s) ''',
                   (transportadora, cidade, estado, telefone))
        mysql.connection.commit()
        cur.close()
        flash("Dados inseridos com sucesso!")
        return redirect(url_for('transportadoras.transportadora'))
    rv = cur.fetchall()
    return render_template('transportadora.html', listatransportadoras=rv)


# ATUALIZAÇÃO DO CADASTRO DA TRANSPORTADORA
@transportadora_blueprint.route('/updatetransp', methods=['POST', 'GET'])
def updatetransp():
    if request.method == "POST":
        idtransportadora = request.form['idtransportadora']
        transportadora = request.form['transportadora']
        cidade = request.form['cidade']
        estado = request.form['estado']
        telefone = request.form['telefone']
        cur = mysql.connect.cursor()
        cur.execute( """ UPDATE transportadoras 
                         SET transportadora=%s, cidade=%s, estado=%s, telefone=%s 
                         WHERE idtransportadora=%s """,
                   (transportadora, cidade, estado, telefone, idtransportadora))
        mysql.connect.commit()
        flash("Dados alterados com sucesso!")
        return redirect(url_for('transportadoras.transportadora'))


# DELETAR A TRANSPORTADORA
@transportadora_blueprint.route('/deletetransp/<string:idtransportadora>', methods=['GET'])
def deletetransp(idtransportadora):

    cur = mysql.connection.cursor()
    cur.execute(""" DELETE from transportadoras WHERE idtransportadora=%s """ %(idtransportadora))
    mysql.connection.commit()
    flash("Item deletado com sucesso!")
    return redirect(url_for('transportadoras.transportadora'))