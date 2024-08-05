from main import app, database
from models import Usuarios, Post

# O contexto da aplicação é necessário para que o SQLAlchemy possa acessar a configuração do banco de dados.
# with app.app_context():
#     # Cria todas as tabelas definidas nos modelos importados (Usuarios e Post).
#     database.create_all()

#criar usuario
# with app.app_context():
#     usuario = Usuarios(username="Sivaldo", email="sivaldo@gmail.com", senha="123456")
#     usuario2 = Usuarios(username="lucas", email="lucas@gmail.com", senha="123457")
#     usuario3 = Usuarios(username="lice", email="lice@gmail.com", senha="123458")
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.add(usuario3)
#     database.session.commit()

#busca no banco
# with app.app_context():
#     meus_usuarios = Usuarios.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = meus_usuarios[0]
#     print(primeiro_usuario)
#     primeiro_usuario = Usuarios.query.first()
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.username)
#
#     usuario_teste = Usuarios.query.filter_by(email='sivaldo@gmail.com').first()
#     print(usuario_teste)
#     print(usuario_teste.username)


#criar um post
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Primeiro post sivaldo', corpo='sivaldo voando!')
#     database.session.add(meu_post)
#     database.session.commit()

with app.app_context():
    post = Post.query.first()
    print(post.titulo)
    print(post.autor.email)
    print(post.autor.username)




