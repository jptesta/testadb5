from app import app, mysql
from flask_mysqldb import MySQLdb
from flask import render_template, request, redirect, url_for, flash, jsonify


@app.route('/', methods=['GET','POST'])
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(''' SELECT * FROM clientes''')
    clientes = cur.fetchall()
    return render_template('index.html', clientes=clientes)

@app.route('/index2')
def index2():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == ' ':
            query = "SELECT * FROM clientes ORDER BY id"
            cur.execute(query)
            clientes = cur.fetchall()
        else:
            query = "SELECT * FROM clientes WHERE razao_social like '%{}%%"
            cur.execute(query)
            numrows = int(cur.rowcount)
            clientes = cur.fetchall()
            print(numrows)
    return jsonify({'htmlresponse': render_template('index.html', clientes=clientes, numrows=numrows)})
    # cur.close()
    # return render_template('index.html', clientes=clientes)


# cadastro de clientes#
@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(''' SELECT * FROM clientes ''')
    if request.method == "POST":
        details = request.form
        razao_social = details['razao_social']
        nome_fantasia = details['nome_fantasia']
        cnpj = details['cnpj']
        inscricao_estadual = details['inscricao_estadual']
        telefone = details['telefone']
        celular = details['celular']
        email = details['email']
        danfe = details['danfe']
        site = details['site']
        vendedor = details['vendedor']
        visita = details['visita']
        observacoes = details['observacoes']
        caixa_postal = details['caixa_postal']
        status = details['status']
        pagamentos = details['pagamentos']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO clientes(razao_social, nome_fantasia, cnpj, inscricao_estadual, telefone, celular, 
                                    email, danfe, site, vendedor, visita, observacoes, caixa_postal, status, pagamentos) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ''',
                                    (razao_social, nome_fantasia, cnpj, inscricao_estadual, telefone, celular, email,
                                    danfe, site, vendedor, visita, observacoes, caixa_postal, status, pagamentos))
        mysql.connection.commit()
        cur.close()
        flash("Cliente cadastrado com sucessso!")
        return redirect(url_for('clientes'))
    listaclientes = cur.fetchall()
    cur.close()
    return render_template('clientes.html', clientes=listaclientes)


# EDITAR CLIENTE
@app.route('/editcliente', methods=['GET', 'POST'])
def editcliente():
    if request.method == 'POST':
        idcliente = request.form['idcliente']
        razao_social = request.form['razao_social']
        nome_fantasia = request.form['nome_fantasia']
        cnpj = request.form['cnpj']
        inscricao_estadual = request.form['inscricao_estadual']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        danfe = request.form['danfe']
        site = request.form['site']
        vendedor = request.form['vendedor']
        visita = request.form['visita']
        observacoes = request.form['observacoes']
        caixa_postal = request.form['caixa_postal']
        status = request.form['status']
        pagamentos = request.form['pagamentos']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE clientes SET razao_social=%s, nome_fantasia=%s, cnpj=%s, inscricao_estadual=%s, 
                        telefone=%s, celular=%s, email=%s, danfe=%s, site=%s, vendedor=%s, visita=%s, observacoes=%s, 
                        caixa_postal=%s, status=%s, pagamentos=%s WHERE idcliente=%s""",
                   (razao_social, nome_fantasia, cnpj, inscricao_estadual, telefone, celular, email, danfe, site,
                    vendedor, visita, observacoes, caixa_postal, status, pagamentos, idcliente))
        mysql.connection.commit()
        flash("Cliente alterado com sucesso!!")
        cur.close()
        return redirect(url_for('clientes'))


# DELETAR CLIENTE
@app.route('/deletecliente/<string:idcliente>', methods=['GET'])
def deletecliente(idcliente):
    flash("Item deletado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE from clientes WHERE idcliente=%s """ % (idcliente))
    mysql.connection.commit()
    return redirect(url_for('clientes'))


@app.route('/tree')
def tree():
    return render_template('tree.html')


@app.route('/mdb')
def mdb():
    return render_template('mdb.html')


@app.route('/tabletree')
def tabletree():
    return render_template('tabletree.html')


# CADASTRO DE ENDEREÇOS DE CLIENTES
@app.route('/clientesenderecos', methods=['GET', 'POST'])
def clientesenderecos():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(""" SELECT * FROM clientesenderecos  """)
    if request.method == "POST":
        finalidade = request.form['finalidade']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO clientesenderecos(finalidade, endereco, bairro, estado, cidade, cep) 
                        VALUES (%s, %s, %s, %s, %s, %s) ''',
                    (finalidade, endereco, bairro, estado, cidade, cep))
        mysql.connection.commit()
        cur.close()
        flash('endereço cadastrado ')
        return redirect(url_for('clientesenderecos'))
    listaenderecos = cur.fetchall()
    return render_template('clientesenderecos.html', listaenderecos=listaenderecos)


# EDIÇÃO DO ENDEREÇO DE CLIENTES
@app.route('/editclientesenderecos', methods=['GET', 'POST'])
def editclientesenderecos():
    if request.method == "POST":
        finalidade = request.form['finalidade']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO clientesenderecos(finalidade, endereco, bairro, estado, cidade, cep)
                        VALUES (%s, %s, %s, %s, %s, %s) ''',
                    (finalidade, endereco, bairro, estado, cidade, cep))
        mysql.connection.commit()
        cur.close()
        flash('Endereço alterado com sucesso!')
        return redirect(url_for('clientesenderecos'))
    return render_template('clientesenderecos.html')


# CADASTRO DE CONTATOS DE CLIENTES
@app.route('/clientescontatos', methods=['GET', 'POST'])
def clientescontatos():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("""SELECT * FROM clientescontatos """)
    if request.method == 'POST':
        idcliente = request.form['idcliente']
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        ramal = request.form['ramal']
        celular = request.form['celular']
        email = request.form['email']
        cur.execute(''' INSERT INTO clientescontatos(idcliente, nome, cargo, telefone, ramal, celular, email)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                    (idcliente, nome, cargo, telefone, ramal, celular, email))
        mysql.connection.commit()
        cur.close()
        flash('Contato cadastrado com sucesso')
        return redirect(url_for('clientescontatos'))
    lc = cur.fetchall()
    return render_template('clientescontatos.html', listacontatos=lc)


# EDIÇÃO DE CONTATOS
@app.route('/editclientescontatos', methods=['GET', 'POST'])
def editclientescontatos():
    if request.method == 'POST':
        idclientecontato = request.form['idclientecontato']
        idcliente = request.form['idcliente']
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        ramal = request.form['ramal']
        celular = request.form['celular']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute(''' UPDATE clientescontatos 
                        SET idcliente=%s, nome=%s, cargo=%s, telefone=%s, ramal=%s, celular=%s, email=%s 
                        WHERE idclientecontato=%s''',
                        (idcliente, nome, cargo, telefone, ramal, celular, email, idclientecontato))
        mysql.connection.commit()
        flash("contato alterado com sucesso")
        cur.close()
        return redirect(url_for('clientescontatos'))
    return render_template('clientescontatos.html')


# DELETAR CONTATO DE CLIENTE
@app.route('/deleteclientescontatos/<string:idclientecontato>', methods=['GET'])
def deleteclientecontato(idclientecontato):
    flash("Item deletado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE from clientescontatos WHERE idclientecontato=%s """ % (idclientecontato))
    mysql.connection.commit()
    return redirect(url_for('clientescontatos'))




@app.route('/listatransportadoras')
def listatransportadoras():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(''' SELECT clientesbp.*, clientescontatos.*, clientesenderecos.*
                    FROM ((clientesbp 
                        INNER JOIN clientesenderecos 
                        ON clientesbp.idcliente = clientesenderecos.idcliente)
                        INNER JOIN clientescontatos ON clientesbp.idcliente = clientescontatos.idclientecontato) 
                        ''')
    rv = cur.fetchall()
    return render_template('listatransportadoras.html', rv=rv)


# CADASTRAR REPRESENTADA
@app.route('/representadas', methods=['GET', 'POST'])
def representadas():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(''' SELECT * FROM representadas ''')
    if request.method == 'POST':
        flash("Dados inseridos com sucesso!")
        razaosocial = request.form['razaosocial']
        cnpj = request.form['cnpj']
        inscricaoestadual = request.form['inscricaoestadual']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        comissao = request.form['comissao']
        cur.execute(''' INSERT INTO representadas(razaosocial, cnpj, inscricaoestadual,telefone, endereco, bairro, 
                        cidade, estado, cep, comissao )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ''',
                    (razaosocial, cnpj, inscricaoestadual, telefone, endereco, bairro, cidade, estado, cep, comissao))
        mysql.connection.commit()
        cur.close()
        # flash("Representada cadastrada")
        return redirect(url_for('representadas'))
    representadas = cur.fetchall()
    return render_template('representadas.html', repre=representadas)


# editar cadastro representadas
@app.route('/editrepresentadas', methods=['GET', 'POST'])
def editrepresentadas():
    if request.method == "POST":
        idrepresentada = request.form['idrepresentada']
        razaosocial = request.form['razaosocial']
        cnpj = request.form['cnpj']
        inscricaoestadual = request.form['inscricaoestadual']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        comissao = request.form['comissao']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(""" UPDATE representadas SET razaosocial=%s, 
                                                    cnpj=%s, 
                                                    inscricaoestadual=%s, 
                                                    telefone=%s, 
                                                    endereco=%s, 
                                                    bairro=%s, 
                                                    cidade=%s, 
                                                    estado=%s, 
                                                    cep=%s, 
                                                    comissao=%s 
                                                    WHERE idrepresentada=%s """,
                    (razaosocial, cnpj, inscricaoestadual, telefone, endereco, bairro, cidade, estado, cep, comissao,
                     idrepresentada))
        mysql.connection.commit()
        cur.close()
        flash('Representada atualizada com sucesso!')
        return redirect(url_for('representadas'))
    return render_template('representadas.html')


# DELETAR A REPRESENTADA
@app.route('/deleterepres/<string:idrepresentada>', methods=['GET'])
def deleterepres(idrepresentada):
    flash("Item deletado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE from representadas WHERE idrepresentada=%s """ % (idrepresentada))
    mysql.connection.commit()
    return redirect(url_for('representadas'))


# cadastrar contatos das representadas
@app.route('/representadacontatos', methods=['GET', 'POST'])
def representadacontatos():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('''SELECT representadascontatos.*, representadas.idrepresentada, representadas.razaosocial
                    FROM representadascontatos, representadas
                    WHERE representadas.idrepresentada = representadascontatos.idrepresentada ''')
    if request.method == 'POST':
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        cur.execute(""" INSERT INTO representadascontatos (nome, cargo, telefone,celular, email) 
                    VALUES (%s, %s, %s, %s, %s) """,
                    (nome, cargo, telefone, celular, email))
        mysql.connection.commit()
        cur.close()
        flash("cadastro realizado com sucesso")
        return redirect(url_for(representadacontatos))
    contrepre = cur.fetchall()
    return render_template('representadacontatos.html', cr=contrepre)


# editar cadastro contatos das representadas
@app.route('/editrepresentadacontatos', methods=['GET', 'POST'])
def editrepresentadacontatos():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('''SELECT representadascontatos.*, representadas.idrepresentada, representadas.razaosocial
                    FROM representadascontatos, representadas
                    WHERE representadas.idrepresentada = representadascontatos.idrepresentada
                    GROUP BY representadas.razaosocial''')
    if request.method == 'POST':
        idrepresentadacontatos = request.form['idrepresentadacontato']
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        cur.execute(""" UPDATE representadascontatos (nome=%s, cargo=%s, telefone=%s,celular=%s, email=%s 
                        WHERE idrepresentadascontatos=%s) 
                     """,
                    (nome, cargo, telefone, celular, email, idrepresentadacontatos))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for(representadacontatos))
    flash("cadastro realizado com sucesso")
    contrepre = cur.fetchall()
    return render_template('representadacontatos.html', cr=contrepre)


# DELETAR A CONTATO REPRESENTADA
@app.route('/deletereprescontato/<string:idrepresentada>', methods=['GET'])
def deletereprescontato(idcontatorepresentada):
    flash("Item deletado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE from representadascontatos WHERE idcontatorepresentada=%s """ % (idcontatorepresentada))
    mysql.connection.commit()
    return redirect(url_for('representadacontatos'))


@app.route('/orcamentos', methods=['GET', 'POST'])
def orcamentos():
    return render_template('orcamentos.html')


@app.route('/solicitacoes', methods=['GET', 'POST'])
def solicitacoes():
    return render_template('solicitacoes.html')


@app.route('/pedido', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'POST':
        details = request.form
        idpedido = details['idpedido']
        idcliente = details['idcliente']
        razaosocial = details['razaosocial']
        idnumeroorcamento = details['numeroorcamento']
        ordemdecompra = details['ordemdecompra']
        idrepresentada = details['idrepresentanda']
        representada = details['representada']
        datapedido = details['datapedido']
        dataprevista = details['dataprevista']
        descricao = details['descricao']
        ipi = details['ipi']
        valor = details['valor']
        idvendedor = details['idvendedor']
        vendedor = details['vendedor']
        idtransportadora = details['idtransportadora']
        transportadora = details['transportadora']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO pedidos(idpedido,
                                            idcliente,
                                            razaosocial,
                                            idnumeroorcamento,
                                            ordemdecompra,
                                            idrepresentada,
                                            representada,
                                            datapedido,
                                            dataprevista,
                                            descricao,
                                            ipi,
                                            valor,
                                            idvendedor,
                                            vendedor,
                                            idtransportadora,
                                            transportadora)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ''',
                    (idpedido,
                     idcliente,
                     razaosocial,
                     idnumeroorcamento,
                     ordemdecompra,
                     idrepresentada,
                     representada,
                     datapedido,
                     dataprevista,
                     descricao,
                     ipi,
                     valor,
                     idvendedor,
                     vendedor,
                     idtransportadora,
                     transportadora))
        mysql.connection.commit()
        cur.close()
        return render_template('/')
    return render_template('pedido.html')


@app.route('/vendedores', methods=['GET', 'POST'])
def vendedores():
    if request.method == 'POST':
        details = request.form
        nome = details['name']
        telefone = details['telefone']
        celular = details['celular']
        email = details['email']
        endereco = details['endereco']
        bairro = details['bairro']
        cidade = details['cidade']
        estado = details['estado']
        cep = details['cep']
        cpf = details['cpf']
        cnpj = details['cnpj']
        areadeatuacao = details['areadeatuacao']
        comissao = details['comissao']
        banco = details['banco']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO vendedores(nome, telefone, celular, email, endereco, bairro, cidade, estado, 
                        cep, cpf, cnpj, areadeatuacao, comissao, banco) 
                        VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s) ''',
            (nome, telefone, celular, email, endereco, bairro, cidade, estado, cep, cpf, cnpj, areadeatuacao, comissao,
             banco))
        mysql.connection.commit()
        cur.close()
        return 'sucessso'
    return render_template('vendedores.html')


@app.route('/contasbancarias', methods=['GET', 'POST'])
def contasbancarias():
    if request.method == "POST":
        details = request.form
        banco = details['banco']
        agencia = details['agencia']
        contabancaria = details['contabancaria']
        codigoauxiliar = details['codigoauxiliar']
        cur = mysql.connection.cursor()
        cur.execute(
            ''' INSERT INTO contas_bancarias(banco, agencia, contabancaria, codigoauxiliar) VALUES (%s, %s, %s, %s) ''',
            (banco, agencia, contabancaria, codigoauxiliar))
        mysql.connection.commit()
        cur.close()
        flash('conta cadastrada')
        return redirect(url_for('contasbancarias'))
    return render_template('contasbancarias.html')
