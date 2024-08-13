from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuarios

class FormCriarConta(FlaskForm):  # Formulário de criar conta
    username = StringField("Nome do Usuário", validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarConta = SubmitField('Criar Conta')

    def validate_email(self, email):  # Função de validar e-mail
        usuario = Usuarios.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar")

class FormLogin(FlaskForm):  # Formulário de Login
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer Login')



class FormEditarPerfil(FlaskForm):  # Formulário de editar perfil
    username = StringField("Nome do Usuário", validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    botao_submit_editarperfil = SubmitField('Confirmar Edição')






