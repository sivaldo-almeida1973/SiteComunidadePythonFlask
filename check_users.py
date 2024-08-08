# check_users.py
from comunidadeimpressionadora import app, database, Usuarios

with app.app_context():
    usuarios = Usuarios.query.all()
    for usuario in usuarios:
        print(usuario.username, usuario.email, usuario.senha)
