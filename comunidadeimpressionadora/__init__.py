from flask import Flask
from flask_sqlalchemy import SQLAlchemy  #import banco de dados
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

#cria o app
# Configurações existentes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = 'b80d378ec0e5b92e0af2b623a35c0cac'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "home"

# Inicialize Flask-Migrate
migrate = Migrate(app, database)
login_manager.login_view = 'login'  #todos os links que tem login_required  , irá ser direcionado para a pagina de login
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes
from comunidadeimpressionadora.models import Usuarios  # Adicione esta linha
