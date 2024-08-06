from flask import Flask
from flask_sqlalchemy import SQLAlchemy  #import banco de dados
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#cria o app
app = Flask(__name__)


#import secrets  #secrets.token_hex(16)
app.config['SECRET_KEY'] = 'b80d378ec0e5b92e0af2b623a35c0cac'   # chave de segurança
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'  #onde fica banco de dados(local)

#criar instancia banco de dados
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "home"


#precisa chamar o routes para colocar os links no ar
from comunidadeimpressionadora import routes
