from flask import Flask , render_template, url_for, request, flash, redirect
from forms import  FormaLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy  #import banco de dados

app = Flask(__name__)

lista_usuarios = ['Lucas','Lice','Sivaldo','Vanusa','Gute']
#import secrets  #secrets.token_hex(16)
app.config['SECRET_KEY'] = '4c3d52b66f6fa4b91148674a18888e92'   # chave de segurança
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade-db'  #onde fica banco de dados(local)

#criar instancia banco de dados
database = SQLAlchemy(app)




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
    form_criarConta =  FormCriarConta()      #depois disso jogar para dentro do site no login.html

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:  #validando formularios
        #fez login com sucesso exibir msg de login bem sucedido
        flash(f'Login feito com sucesso no e-mail:! {form_login.email.data}','alert-success')# data -e o que foi preenchido no campo email
        #redirecionar para homepage  (importar flash, redirect)
        return redirect(url_for('home'))

    if form_criarConta.validate_on_submit() and 'botao_submit_criarConta' in request.form:
         flash(f'Conta criada para o email: {form_criarConta.email.data}',  'alert-success')
        #criou conta com sucesso
         #redireciona , depois disso ajeita no base.html para exibir msg
         return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarConta=form_criarConta)


if __name__ == "__main__":
    app.run(debug=True)
