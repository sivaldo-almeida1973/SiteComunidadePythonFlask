from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuarios
import bcrypt

# Configurando o contexto da aplicação
with app.app_context():
    # Consultando todos os usuários
    usuarios = Usuarios.query.all()

    # Atualizando as senhas
    for usuario in usuarios:
        # Verificação adicional para garantir que usuario.senha não seja None e seja uma string
        if usuario.senha and isinstance(usuario.senha, str) and not usuario.senha.startswith("$2b$"):
            # Criptografando a senha
            senha_crypt = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            usuario.senha = senha_crypt
            print(f"Senha criptografada para o usuário: {usuario.email}")

    # Salvando as alterações no banco de dados
    database.session.commit()
    print("Todas as senhas foram atualizadas.")
