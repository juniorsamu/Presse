from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField , TextAreaField , IntegerField,FileField,SelectField
from wtforms.validators import DataRequired, Email , Length
from wtforms.widgets import PasswordInput
import datetime 

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Sign in')

#log = LoginForm()
#print(log.username) 

class UserForm(FlaskForm):		
	nom = StringField('Nom', validators = [DataRequired(), Length(min =2, max =20)])
	prenom = StringField('Prenom', validators = [DataRequired(), Length(min =2, max =20)])
	email = StringField('Email', validators= [DataRequired(), Email()])
	password = StringField('Password', widget= PasswordInput(hide_value=False))
	#remember_me = BooleanField('Remember me')
	submit = SubmitField('Envoyer')    

class ArticlesForm(FlaskForm):
	name = StringField('nom')
	categorie = SelectField(choices=['Categorie'])
	text = TextAreaField('Contenue')
	image=FileField(name='file',render_kw={'id': 'upload'})
	prix = IntegerField('prix')
	submit = SubmitField('valider')  

class CatForm(FlaskForm):
	nom = StringField('Nouvelle Categorie')
	submit = SubmitField('Ajouter')


