# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session
from user import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url

@app.route('/')
def home():
    return render_template('home.html', user_post=session.get('user_post'))  # render a template


#Helen
@app.route('/signin', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #creating user object
        user = User()
        
        #pulling info from html input
        username = request.form.get("username")
        password = request.form.get("password")
        
        #returns true or false if user exists in database
        verifyUser = user.findUser(username)
        
        if verifyUser is True:
            #redirects to homepage if passwords match
            if user.get_password() == password:
                return redirect(url_for('home'))
            else:
                error = 'Invalid Password. Please try again.'
        else:
            error = 'Invalid Username. Please try again.'
                
    return render_template('signin.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #copied from signup.py, coded by Abby
    #modifications by Helen in app.py for connecting the controller to Flask
    #modifications by Helen to check if user exists in the database before user can sign up, and to check if passwords match
    error = None
    if request.method == 'POST':
        
        #create a new user
        newUser = StoringUserInfo()
        #create database of usernames
        usernameList = pullingUserInfo().get_allFieldInfo('username')
        
        #gets input from html and stores it as username, pass1, and pass2
        username = request.form.get("username")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")
        
        #checks to see if username is taken
        if username in usernameList:
            error = 'Username is taken. Try again'
        else:
            newUser.set_username(username)
            newUser.set_firstname(request.form.get("fname"))
            newUser.set_lastname(request.form.get("lname"))
            #checks to see if passwords match
            if pass1 == pass2:
                newUser.set_password(request.form.get("pass1"))
                newUser.create_new_document()
                #redirects to login page
                return redirect(url_for('login'))
            else:
                error = "Passwords don't match. Try again"
        
        #TO DO: uncomment out after database can store email
        #newUser.set_(request.form.get("email"))
    
    return render_template('signup.html', error=error)
    

@app.route('/posting', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form.get("name")
        message = request.form.get("message")

        user_post = session.get('user_post', [])
        user_post.append({name, message})
        session['user_post'] = user_post


    return render_template('posting.html', user_post=user_post)

    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)