from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Ola, mundo !</p>"

@app.route("/contato")
def contato():
    return "<h1>Entre em contato com a gente vieiralmeida@gmail.com!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
