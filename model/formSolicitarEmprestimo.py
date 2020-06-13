from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired

class FormSolicitarEmprestimo(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired('Escolha um usuário')])
    numeroMatricula = IntegerField('Número Matrícula', validators=[DataRequired('Escolha um usuário')])
    numeroEquipamento = StringField('Número Equipamento', validators=[DataRequired('Escolha pelo menos um equipamento')])
    dtEmprestimo = StringField('Data Empréstimo', validators=[DataRequired('Escolha a data do empréstimo')]) 
    dtDevolucao = StringField('Data Devolução.', validators=[DataRequired('Escolha a data da devolução do empréstimo')])
