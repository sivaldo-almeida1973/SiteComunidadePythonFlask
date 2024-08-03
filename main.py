from flask import Flask , render_template, url_for
from forms import  FormaLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ['Lucas','Lice','Sivaldo','Vanusa','Gute']

app.config['SECRET_KEY'] = '4c3d52b66f6fa4b91148674a18888e92'   # chave de segurança
#import secrets
#secrets.token_hex(16)


@app.route('/')   #pagina de inicio
def home():
    return render_template('home.html')#render retorna tudo da pagina home.html

@app.route('/contato')  #pagina de contatos
def contato():
    return render_template('contato.html')


@app.route('/usuarios')  #pagina de usuarios
def usuarios():                         #o primeiro paramentro( lista_usuarios) vai para a pagina html
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)#o segundo é a variavel da lista

@app.route('/login', methods=['GET', 'POST']) #pagina de login
def login():
    form_login = FormaLogin()  #criar instancias e passa
    form_criaConta =  FormCriarConta()      #depois disso jogar para dentro do site no login.html
    return render_template('login.html', form_login=form_login, form_criarConta=form_criaConta)


if __name__ == "__main__":
    app.run(debug=True)
