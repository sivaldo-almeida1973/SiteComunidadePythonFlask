from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuarios, Post

with app.app_context():
    database.create_all()
    #database.drop_all()  # Descomente esta linha se quiser dropar todas a
