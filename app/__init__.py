from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager , login_url

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

app.config['SECRET_KEY'] = "2a5r8q7jRWAx2A"
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///blog.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)

UPLOAD_FOLDER = 'app/static/Images/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



from app import root 
  
