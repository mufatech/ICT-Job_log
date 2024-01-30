from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager
from flask_migrate import Migrate




app = Flask(__name__)
app.config.from_object(Config)



   
#load environment variables .env file
load_dotenv()

# load secret key from enviroment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


# load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'



@login_manager.user_loader
def load_user(user_id):

    from app.models.login import Admin
    return Admin.query.get(int(user_id))

     




from app.routes.root import *
from app.routes.admin import *
from app.models import *


if __name__ == '__main__':
    app.run()