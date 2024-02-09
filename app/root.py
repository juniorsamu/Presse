from app import app, db , bcrypt , login_manager,ALLOWED_EXTENSIONS                  
from flask import render_template, flash , redirect , url_for , request
from app.forms import LoginForm , UserForm , ArticlesForm , CatForm 
from app.model import Utilisateur, Article,Categorie
from flask_login import login_user
import urllib.request
import os
from werkzeug.utils import secure_filename
 


def allowed_file(filename):		# c'est pour permettre l'execution de certain extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@login_manager.user_loader  # verifie si l'utilisateur s'est inscrit avant de se connecter par le moyen de l'id
def load_user(user_id):
	return Utilisateur.query.get(user_id)

@app.route("/article", methods=['POST', 'GET'])		# route qui à permis de receuillir et d'enregistrer les articles
def article():
	Articles_Form= ArticlesForm()	
	Articles_Form.categorie.choices = [(c.id, c.nom) for c in Categorie.query.all()] 
	if Articles_Form.validate_on_submit():
		name = Articles_Form.name.data
		categorie = Articles_Form.categorie.data
		text = Articles_Form.text.data
		prix = Articles_Form.prix.data
		
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = 'Articles_'+secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			
		article=Article(image=filename, titre=name, contenue=text ,prix=prix,categorie_id=categorie)
			
		#envoie de donnée dans la BD
		db.session.add(article)
		db.session.commit()
		flash("Article enrégistré avec succes!!")


	return render_template('eng_article.html', Aform = Articles_Form)	# l'enregistrement se fait grace au formulaire 'eng_article.html'

@app.route("/index", methods=['POST', 'GET'])             # affichage des articles enregistrés sur le formulaire par la page index.html
def index():
	article = Article.query.order_by(Article.titre)
	return render_template('index.html',articles = article)


@app.route("/index/<int:d>", methods=['POST', 'GET'])             # pour gerer le article en fonction des categories
def ix(d):
	article = Article.query.filter_by(categorie_id=d)
	return render_template('index.html',articles = article)

@app.route("/categorie",methods=['POST', 'GET'])		 #Creation des categories d'articles
def cat():
	cat_Form=CatForm()
	if cat_Form.validate_on_submit():
		nom = cat_Form.nom.data
		categorie=Categorie(nom = nom)
		
		#envoie de donnée dans la BD
		db.session.add(categorie)
		db.session.commit()
	return render_template("categorie.html",Ccat_Form= cat_Form)


@app.route("/login", methods=['POST', 'GET'])		 # la connection des utilisateurs et vérification de des identifiants 
def login():										#	(s'il s'est inscrit il accede à la page au cas echéant il doit se s'inscrire d'abord)
		login_form = LoginForm()
		if login_form.validate_on_submit():
			email = login_form.email.data
			password = login_form.password.data
			#envoie de donnée dans la BD

			user = Utilisateur.query.filter_by(email=email).first()

			if not user:
				flash(" Ce mail n'a pas été enregistré")
				print("ERROR MAIL NOT EXIST")
				return redirect(url_for('login'))

			pswd_unhashed = bcrypt.check_password_hash(user.mot_passe, password)

			print("ERRRROR ",pswd_unhashed)

			if not pswd_unhashed:
				flash("Mot de passe saisie incorrect")
				print("PASSWORD INCORRECT")
				return redirect(url_for('login'))

			login_user(user)
			flash("Vous etes connecté")
			return redirect(url_for('index'))

		return render_template('login.html', form = login_form)



@app.route("/user", methods=['POST', 'GET'])	# route pour acceder et remplire le formulaire d'inscription des utilisateurs
def user():
	user_form= UserForm()
	if user_form.validate_on_submit():
		nom = user_form.nom.data
		prenom = user_form.prenom.data
		email = user_form.email.data
		password = user_form.password.data
		pw_hash = bcrypt.generate_password_hash('password').decode("utf-8")

		#envoie de donnée dans la BD
		user = Utilisateur(nom=nom, prenom=prenom, email=email, mot_passe=pw_hash)
		

		db.session.add(user)
		db.session.commit()
		flash("Utilisateur enrégistré avec succes!!")


	return render_template('user.html', form = user_form)

@app.route("/acce")		#
def debut():
	return render_template('acceuil2.html')

@app.route("/accesoire")	# pour acceder à la page accessoire
def debut1():
	return render_template('accessoire.html')

@app.route("/parfum")		# pour acceder à la page parfum
def debut2():
	return render_template('parfum.html')

@app.route("/acc")		# pour acceder à la page acceuil	
def deb():
	return render_template('acc.html')