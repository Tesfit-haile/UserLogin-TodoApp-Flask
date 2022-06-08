################# Steps to follow #################################

### Step 1: create the project folder
### Step 2: create the templates, static, app.py
### Step 3: create the __init__.py file
### Step 4: create the routes.py file

### Step 5: create the venv in the project before starting installing the packages
# then  python3 - m venv .venv
# then activate the .venv
# then pip freeze > requirements.txt  # for listing all the packages
# pip install - r requirements.txt  # later on for installing the packages

### step 6: create an app_creater func at the __init__.py file 
>>> then it's going to be sent to the app.py file to be created and run
>>> then it's going to be imported by the routes.py in order to create a Blueprint of the project
>>> then it's going to be returned to the __init__.py file to be registered 
>>> then it's going to be run by the app.py     

#### Now build the templates >>> first build the base.html then all the others will inherit from it.


### Step 7: check if you have a "POST" methods at the login and sign_up file
### Step 8: Now check if U can grab them through the routes from the form
### Step 9: Do validation , hashing the password
### Step 10: Then ADD them to the database ( you need to create DB at the __init__.py file)
### Step 11: Check if you can login 
### Step 12: do the authentication ( login_user, logout_user, current_user ) add restrictions to the routes
### step 13: to do the authentication first import flask-Manager and initiate it 
>>>>>>>>>>>  Step 14: challenging at the LoginManager() during initialization .
>>>>>>>>>>> during the authentication not necessary to pass the current_user through the routes
>>>>>>>>>>> in order to say if current_user.is_authenticated: U can do it with out passing it.


### step 15: 