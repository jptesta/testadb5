


Base = automap_base()
Base.prepare(db.engine, reflect=True)


class Clientes(db.Model):
    __tablename__ = "clientes"
    Idcliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Razao_social = db.Column(db.String(255))
    Nome_fantasia = db.Column(db.String(255))
    Cnpj = db.Column(db.String(255), unique=True, nullable=False)
    Inscricao_estadual = db.Column(db.String(255))
    Telefone = db.Column(db.String(255))
    Celular = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Danfe = db.Column(db.String(255))
    Site = db.Column(db.String(255))
    Vendedor = db.Column(db.String(255))
    Visita = db.Column(db.String(255))
    Observacoes = db.Column(db.String(255))
    Caixa_postal = db.Column(db.String(255))
    Status = db.Column(db.String(255))
    Pagamentos = db.Column(db.String(255))
    Enderecos = db.relationship('Clientesenderecos', backref="cliend")
    Contatos = db.relationship('Clientescontatos', backref="clicon")
    Contatosrealizados = db.relationship('Contatos_realizados', backref="crealizado")


class Clientesenderecos(db.Model):
    __tablename__ = "clientesenderecos"
    Idclientesenderecos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Finalidade = db.Column("finalidade", db.String(255))
    Endereco = db.Column('endereco', db.String(255))
    Bairro = db.Column("bairro", db.String(255))
    Cidade = db.Column('cidade', db.String(255))
    Estado = db.Column('estado', db.String(255))
    Cep = db.Column('cep', db.String(255))
    idcliente = db.Column(db.Integer, db.ForeignKey('clientes.Idcliente'))


class Clientescontatos(db.Model):
    __tablename__ = "clientescontatos"
    Idclientecontato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nome = db.Column(db.String)
    Cargo = db.Column(db.String)
    Telefone = db.Column(db.String)
    Ramal = db.Column(db.String)
    Celular = db.Column(db.String)
    Email = db.Column(db.String)
    idcliente = db.Column(db.Integer, db.ForeignKey("clientes.Idcliente"))
