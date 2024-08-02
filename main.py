from flask import Flask , render_template, url_for

app = Flask(__name__)

lista_usuarios = ['Lucas','Lice','Sivaldo','Vanusa','Gute']

@app.route('/')
def home():
    return render_template('home.html')#render retorna tudo da pagina home.html

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():                         #o primeiro paramentro( lista_usuarios) vai para a pagina html
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)#o segundo é a variavel da lista

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
