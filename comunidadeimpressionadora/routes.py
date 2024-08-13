#rotas do site(links)
from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuarios, Post
from flask_login import login_required, current_user, login_user, logout_user

lista_usuarios = ['Lucas','Lice','Sivaldo','Vanusa','Gute']

@app.route('/')   #pagina de inicio
def home():
    return render_template('home.html')#render retorna tudo da pagina home.html

@app.route('/contato')  #pagina de contatos
def contato():
    return render_template('contato.html')


@app.route('/usuarios')  # página de usuários
@login_required
def usuarios():  # o primeiro parâmetro (lista_usuarios) vai para a página HTML
    lista_usuarios = Usuarios.query.all()
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)  # o segundo é a variável da lista


@app.route("/criarconta", methods=['GET', 'POST'])
def criarConta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit() and 'botao_submit_criarConta' in request.form:
        senha_crypt = bcrypt.generate_password_hash(form_criarconta.senha.data)
        existing_user = Usuarios.query.filter_by(email=form_criarconta.email.data).first()
        if existing_user:
            flash('Email já cadastrado. Por favor, use outro email.', 'alert-danger')
            return redirect(url_for('criarConta'))
        usuario = Usuarios(username=form_criarconta.username.data,
                           email=form_criarconta.email.data,
                           senha=senha_crypt)
        try:
            database.session.add(usuario)
            database.session.commit()
            flash(f'Conta criada para o email: {form_criarconta.email.data}', 'alert-success')
            return redirect(url_for('home'))
        except Exception as e:
            database.session.rollback()
            flash(f"Erro ao criar conta: {e}", 'alert-danger')
    return render_template('criarconta.html', form_criarConta=form_criarconta)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuarios.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next') #  Obtém o valor do parâmetro next da URL.
            if par_next:  # Verifica se par_next tem um valor.
                return redirect(par_next)  #Redireciona para a URL especificada em par_next se ela existir.
            else:  #Caso contrário, executa o bloco else
                return redirect(url_for('home'))  #Redireciona para a página home se par_next não tiver um valor.
        else:
            flash('Falha no Login. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('login.html', form_login=form_login)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/sair')  #importar logout_user
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
     foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
     return render_template('perfil.html', foto_perfil=foto_perfil)



@app.route('/post/criar')
@login_required
def criar_post():
        return render_template('criarpost.html')

