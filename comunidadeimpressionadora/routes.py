#rotas do site(links)
from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormaLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuarios, Post
from flask_login import login_required, current_user


lista_usuarios = ['Lucas','Lice','Sivaldo','Vanusa','Gute']

@app.route('/')   #pagina de inicio
def home():
    return render_template('home.html')#render retorna tudo da pagina home.html

@app.route('/contato')  #pagina de contatos
def contato():
    return render_template('contato.html')


@app.route('/usuarios')  #pagina de usuarios
def usuarios():                         #o primeiro paramentro( lista_usuarios) vai para a pagina html
    usuarios = Usuarios.query.all()
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)#o segundo é a variavel da lista



@app.route("/criarconta", methods=['GET', 'POST'])
def criarConta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit() and 'botao_submit_criarConta' in request.form:
        # Verifique se o email já existe no banco de dados
        existing_user = Usuarios.query.filter_by(email=form_criarconta.email.data).first()
        if existing_user:
            flash('Email já cadastrado. Por favor, use outro email.', 'alert-danger')
            return redirect(url_for('criarConta'))

        # Crie o novo usuário
        usuario = Usuarios(username=form_criarconta.username.data,
                           email=form_criarconta.email.data,
                           senha=bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8'))
        try:
            database.session.add(usuario)
            database.session.commit()

            # Verifique se o usuário foi adicionado
            added_user = Usuarios.query.filter_by(email=form_criarconta.email.data).first()
            if added_user:
                flash(f'Conta criada para o email: {form_criarconta.email.data}', 'alert-success')
            else:
                flash('Erro ao verificar a criação da conta.', 'alert-danger')

            return redirect(url_for('home'))
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao salvar no banco de dados: {e}")
            flash(f"Erro ao criar conta: {e}", 'alert-danger')
    return render_template('criarconta.html', form_criarConta=form_criarconta)


@app.route('/login', methods=['GET', 'POST']) #pagina de login
def login():
    form_login = FormaLogin()  #criar instancias e passa
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:  #validando formularios
        #fez login com sucesso exibir msg de login bem sucedido
        flash(f'Login feito com sucesso no e-mail:! {form_login.email.data}','alert-success')# data -e o que foi preenchido no campo email
        #redirecionar para homepage  (importar flash, redirect)
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login)





