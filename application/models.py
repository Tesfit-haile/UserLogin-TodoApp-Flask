from application import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
# from application import my_app_created


# app = my_app_created() #### it doesn't let me do this, No clue why /???
# bcrypt = Bcrypt(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # no need a confirmed pwd column
    todos = db.relationship('Todos',  backref='user')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f" >>> {self.name}-{self.email} - {self.password} <<< "

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def show_all_user(self):
        all_users = self.query.all()
        return [user.name for user in all_users]


########################## ToDo todo_database ######################################


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todoName = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, todoName, user_id):
        self.todoName = todoName
        self.user_id = user_id

    def __repr__(self):
        return f"{self.todoName}----- by >>> user_id of >>> {self.user_id}"

    def show_all_todos(self):
        allTodo = self.query.all()
        return [todo.todoName for todo in allTodo]
