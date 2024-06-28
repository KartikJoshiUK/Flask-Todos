# Imports
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from dotenv import load_dotenv
from services.db import db
from services.login import login_manager
import routes
import os

#  Initialization
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db)




# Routes
app.register_blueprint(routes.indexRouter)
app.register_blueprint(routes.templatesRouter, url_prefix="/templates")
app.register_blueprint(routes.formRouter, url_prefix="/form")
app.register_blueprint(routes.dbRouter, url_prefix="/db")
app.register_blueprint(routes.authRouter, url_prefix="/auth")

# Server
if __name__ == "__main__":
    app.run(debug=True)