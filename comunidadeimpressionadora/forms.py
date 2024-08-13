from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuarios
from flask_login import  current_user

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
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    botao_submit_editarperfil = SubmitField('Confirmar Edição')



    def validate_email(self, email):  #validação do email
        #verificar se mudou o email
        if current_user.email != email.data:
            usuario = Usuarios.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuario com esse e-mail. Cadastre-se com outro e-mail')





