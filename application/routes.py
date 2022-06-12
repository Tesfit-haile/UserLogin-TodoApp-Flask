from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_bcrypt import Bcrypt
from .models import User, Todos
from application import my_app_created, db
from flask_login import login_required, login_user, logout_user, current_user

# this need to be registered at the __init__.py file
myRoutes = Blueprint('app', __name__)

app = my_app_created()
bcrypt = Bcrypt(app)


@myRoutes.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # first get a user from db in order to show him only his record

    fetchedAllTodo = Todos.query.filter_by(user_id=current_user.id)

    if request.method == 'GET':
        return render_template('/home.html', fetchedAllTodo=fetchedAllTodo, editTodo=None)

    if request.method == 'POST':
        todo_name = request.form.get('todo')
        new_todo = Todos(todoName=todo_name, user_id=current_user.id)
        print('Todo created ################', current_user.id)

        db.session.add(new_todo)
        db.session.commit()
        print(Todos.show_all_todos(new_todo))
        flash('New Todo added to db', category='success')

        # if u don have this it'll give you home page with no todo
        return render_template('/home.html', fetchedAllTodo=fetchedAllTodo, editTodo=None)


################################################################################################
@myRoutes.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #### get data from the form #####
        name = request.form.get('first_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmed_pwd = request.form.get('confirm password')

        #### do validation here #####
        if len(name) < 3:
            flash('Firs-Name must be at least 3 characters', category='error')
        elif len(password) < 3:
            flash('Password must be at least 3 characters', category='error')
        elif password != confirmed_pwd:
            flash('Password must be same', category='error')
        else:
            # ADD to Database ##### but hash the pwd with the b
            newUser = User(
                name=name,
                email=email,
                password=bcrypt.generate_password_hash(password)
            )

            User.add_to_db(newUser)
            login_user(newUser, remember=True)

            print(User.show_all_user(newUser))
            flash('Registered successfully', category='success')
            return redirect('/login')

    return render_template('sign_up.html')


################################################################################################
@myRoutes.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        fetched_user = User.query.filter_by(email=email).first()
        if fetched_user:
            if bcrypt.check_password_hash(fetched_user.password, password):
                flash('Welcome correct password !', category='success')
                login_user(fetched_user, remember=True)
                return redirect('/')
            else:
                flash('Incorrect password !', category='error')
        else:
            flash('Invalid password or email', category='error')

    return render_template('login.html')


################################################################################################
@myRoutes.route('/updateTodo/<todoId>', methods=['GET', 'POST'])
def updateTodo(todoId):
    if request.method == 'POST':

        todoTodUpdate = Todos.query.get(int(todoId))
        todoTodUpdate.todoName = request.form.get('name')
        db.session.commit()
        flash('Updated Success!', category='success')

        return redirect('/')


################################################################################################

@myRoutes.route('/deleteTodo/<todoId>', methods=['GET'])
def deleteTodo(todoId):
    deleteTodo = Todos.query.get(int(todoId))
    db.session.delete(deleteTodo)
    db.session.commit()
    print(deleteTodo, 'Todo has deleted')
    flash(f' >>> { [ deleteTodo ] }, has been deleted', category='success')
    return redirect('/')

################################################################################################
################################################################################################
################################################################################################


################################################################################################
@myRoutes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@myRoutes.route('/test', methods=['GET'])
def test():
    return render_template('test.html')
