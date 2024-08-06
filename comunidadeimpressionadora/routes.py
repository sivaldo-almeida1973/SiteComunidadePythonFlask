#rotas do site(links)
from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.forms import FormaLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuarios

lista_usuarios = ['Lucas','Lice','Sivaldo','Vanusa','Gute']

@app.route('/')   #pagina de inicio
def home():
    return render_template('home.html')#render retorna tudo da pagina home.html

@app.route('/contato')  #pagina de contatos
def contato():
    return render_template('contato.html')


@app.route('/usuarios')  #pagina de usuarios
def usuarios():                         #o primeiro paramentro( lista_usuarios) vai para a pagina html
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)#o segundo é a variavel da lista


@app.route("/criarconta",  methods=['GET', 'POST'])
def criarConta():
    form_criarConta = FormCriarConta()
    if form_criarConta.validate_on_submit() and 'botao_submit_criarConta' in request.form:
        usuario = Usuarios(username=form_criarConta.username.data,
                       email=form_criarConta.email.data,
                       senha=form_criarConta.senha.data) #criar usuario
        database.session.add(usuario)#adicionar a sessao
        database.session.commit()##commit na sessao
        flash(f'Conta criada para o email: {form_criarConta.email.data}',  'alert-success')
        #criou conta com sucesso
        #redireciona , depois disso ajeita no base.html para exibir msg
        return redirect(url_for('home'))
    return render_template('criarconta.html', form_criarConta=form_criarConta)


@app.route('/login', methods=['GET', 'POST']) #pagina de login
def login():
    form_login = FormaLogin()  #criar instancias e passa
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:  #validando formularios
        #fez login com sucesso exibir msg de login bem sucedido
        flash(f'Login feito com sucesso no e-mail:! {form_login.email.data}','alert-success')# data -e o que foi preenchido no campo email
        #redirecionar para homepage  (importar flash, redirect)
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login)




