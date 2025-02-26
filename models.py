from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'uni1500'}  # Especifica o schema
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

class InseminacaoEstruturaDados(db.Model):
    __tablename__ = 'inseminacaoestruturadados'
    __table_args__ = {'schema': 'uni1500'}  # Especifica o schema

    fazenda = db.Column(db.String, primary_key=True)
    estado = db.Column(db.String)
    municipio = db.Column(db.String)
    num_animal = db.Column(db.Numeric, name="Nº ANIMAL")  # Aspas simples
    lote = db.Column(db.String)
    raca = db.Column(db.String)
    categoria = db.Column(db.String)
    ecc = db.Column(db.Numeric)
    ciclicidade = db.Column(db.Numeric)
    protocolo = db.Column(db.String)
    implante_p4 = db.Column(db.String, name="IMPLANTE P4")  # Aspas simples
    empresa = db.Column(db.String)
    gnrh_na_ia = db.Column(db.Numeric, name="GnRH NA IA")  # Aspas simples
    pgf_no_d0 = db.Column(db.Numeric, name="PGF NO D0")  # Aspas simples
    dose_pgf_retirada = db.Column(db.String, name="Dose PGF retirada")  # Aspas simples
    marca_pgf_retirada = db.Column(db.String, name="Marca PGF retirada")  # Aspas simples
    dose_ce = db.Column(db.String, name="Dose CE")  # Aspas simples
    ecg = db.Column(db.String)
    dose_ecg = db.Column(db.String, name="DOSE eCG")  # Aspas simples
    touro = db.Column(db.String)
    raca_touro = db.Column(db.String, name="RAÇA TOURO")  # Aspas simples
    empresa_touro = db.Column(db.String, name="EMPRESA TOURO")  # Aspas simples
    inseminador = db.Column(db.String)
    num_iatf = db.Column(db.String, name="Nº da IATF")  # Aspas simples
    dg = db.Column(db.Numeric)
    vazia_com_ou_sem_cl = db.Column(db.Numeric, name="VAZIA COM OU SEM CL")  # Aspas simples
    perda = db.Column(db.Numeric)