from flask import Blueprint, render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
from .models import User
from application import my_app_created
from flask_login import login_required, login_user, logout_user, current_user


# this need to be registered at the __init__.py file
myRoutes = Blueprint('app', __name__)

app = my_app_created()
bcrypt = Bcrypt(app)


@login_required
@myRoutes.route('/')
def home():
    return render_template('/home.html')


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

    return render_template('sign_up.html')


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


@login_required
@myRoutes.route('/logout')
def logout():
    logout_user()
    return redirect('/login')
