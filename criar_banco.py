from comunidadeimpressionadora import database, app
from comunidadeimpressionadora.models import Usuarios, Post

with app.app_context():
    database.create_all()
