#criar tabela do banco de dados
from main import database
from datetime import datetime


#tabela usuarios
class Usuarios(database.Model):  #Model é uma classe do flask
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False, unique=True)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)  #relacao desta tabela com de Post
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

#tabela de posts
class Post(database.Model):
     id = database.Column(database.Integer, primary_key=True)
     titulo =  database.Column(database.String, nullable=False)
     corpo =  database.Column(database.Text, nullable=False)
     data_criacao =  database.Column(database.DataTime, nullable=False, default=datetime.now)
     id_usuario = database.Column(database.Integer,
                                  database.ForeignKey('usuario.id'), nullable=False)#relacao desta tabela com de Usuario



