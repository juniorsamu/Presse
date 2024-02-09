from app import db 
import datetime
from flask_login import UserMixin

class Utilisateur(db.Model, UserMixin):
	id= db.Column(db.Integer, primary_key = True , autoincrement= True)
	nom = db.Column(db.String(50), unique = False, nullable = False) 
	prenom = db.Column(db.String(50), unique = False, nullable = False) 
	email = db.Column(db.String(50), unique = False, nullable = False) 
	mot_passe = db.Column(db.String(50), unique = False, nullable = False) 
	admin = db.Column(db.Boolean, unique = False, nullable = False, default=False) 
	articles = db.relationship('Article', backref = 'Utilisateur')

	def __repr__(self):
		return f'User{self.nom}'
		

#personne = Utilisateur(nom = "John", prenom = 'Doe')
#print (personne)


class Article(db.Model):
	id = db.Column(db.Integer, primary_key = True) 
	titre = db.Column(db.String(255), unique = False, nullable = False) 
	contenue = db.Column(db.String(50), unique=False, nullable=True)
	utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
	created_at = db.Column(db.Date, default = datetime.datetime.now())
	categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))
	image = db.Column(db.String, unique=False, nullable=False)
	prix = db.Column(db.Integer, unique=False, nullable=False)

class Categorie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.String(255), unique = False, nullable = False) 
	article = db.relationship('Article',backref='Categorie',lazy=True)