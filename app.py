# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from user import *
from map import *
from Database.StoringUserInfo import *

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url

@app.route('/')
def home():
    return render_template('home.html')  # render a template

@app.route('/signin', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #copied from login.py with modifications, need to update
        user = User()
        
        username = request.form.get("username")
        password = request.form.get("password")
        
        verifyUser = user.findUser(username)
        
        if verifyUser is True:
            if user.get_password() == password:
                return redirect(url_for('home'))
            else:
                error = 'Invalid Password. Please try again.'
        else:
            error = 'Invalid Username. Please try again.'
                
    return render_template('signin.html', error=error)

        
@app.route('/map', methods= ['GET', 'POST'])
def map():
    
    if request.method == 'POST':
        map = Map()
    
        roomnumber = request.form.get("roomnumber")
        roomImage = map.searchMap(roomnumber)
        
        if roomImage is True:
            return render_template('map.html', img = roomImage)
    
    return render_template('map.html')
         
        
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)