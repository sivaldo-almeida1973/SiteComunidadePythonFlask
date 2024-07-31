from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Ola, mundo !</p>"

@app.route("/contato")
def contato():
    return "<p>Entre em contato com a gente vieiralmeida@gmail.com!</p>"


if __name__ == "__main__":
    app.run(debug=True)
