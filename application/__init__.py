from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()
db_name = 'userTodo.db'


def my_app_created():

    app = Flask(__name__)

    ##################################### INITIATING DATABASE ##########################################
    app.config['SECRET_KEY'] = 'mmmmmmmmmmmmm:::: secret'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'

    db.init_app(app)

    ##################################### Registration ##########################################
    # get the blueprint from the routes file and register it here
    from .routes import myRoutes
    app.register_blueprint(myRoutes, url_prefix='/')

    ##################################### Creating DATABASE ##########################################
    from .models import User, Todos
    createDataBase(app)

    ##################################### INITIATING LoginManager ##########################################
    login_manager = LoginManager()
    login_manager.login_view = 'app.login'  # this was a challenge to understand
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # same as filter_by but it will get by default the primary_key
        return User.query.get(int(id))
    return app


def createDataBase(app):
    if not os.path.exists('application/' + db_name):
        db.create_all(app=app)
        print('Database has been created ################ ')
    else:
        print(' ############# Already DB created ################ ')
