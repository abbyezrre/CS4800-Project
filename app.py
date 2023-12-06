# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session
from user import *
from map import *
from uProfile import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *
from search import *
from posting import PostingController
from clubs import ClubsController
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url

@app.route('/')
def home():
    return render_template('home.html', user_post=session.get('user_post'))  # render a template


#Helen - signin
@app.route('/signin', methods=['GET', 'POST'])
def login():
    error = None
<<<<<<< HEAD
    if request.method == 'POST':
        #creating user object
        user = User()
        #made username variable global - Elvin
        global username 
=======
    user= None
    global username
    if request.method == 'POST':
        
        
>>>>>>> fb70b7bed65a2d05232431274408ecad2dce5ab6
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

 # map page - Abigail 
 # connects to map controller and the html        
@app.route('/map', methods= ['GET', 'POST'])
def map():
    
    if request.method == 'POST':
        map = Map()
    
        roomnumber = request.form.get("roomnumber")
        roomImage = map.searchMap(roomnumber)
        
        if roomImage is True:
            return render_template('map.html', img = roomImage)
    
    return render_template('map.html')

#helen - search function
#needs the UI to be updated 
@app.route('/search', methods= ['GET', 'POST'])
def search():
    output = []
    input = ""
    if request.method == "POST":
        #gets search query from html
        searchInput = request.form.get("search")
        #creates searching object with searchInput
        searching = searchBar(searchInput)
        #searches to see if query exists in the database
        searching.search()
        #appends array with first name and last name of user
        output.append(searching.output)
        input += searchInput
        
    output = sum(output,[])
    return render_template('search.html', output=output, input=input, len = len(output))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #copied from signup.py, coded by Abby
    #modifications by Helen for connecting the controller to Flask
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
    
#kim - post function
@app.route('/posting', methods=['GET', 'POST'])
def post():
    user_post = session.get('user_post', [])

    if request.method == 'POST':
        #get data from form
        name = request.form.get("name")
        message = request.form.get("message")

        posting_post = PostingController()

        posting_post.post_feed(name, message)
        #append post to user posts
        user_post.append({'name': name, 'message': message})
        #session['user_post'] = user_post


    return render_template('posting.html', user_post=user_post)

# profile function - Elvin
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    username =session.get("username")
    
 
    error = None
    fullname = None
    age = None
    major = None
    bio = None

<<<<<<< HEAD
=======
    #creates profile class
    user = Profile(username)

    
    if username is not None:
        
        user.displayFullname(username)
        fullname = user.fullname

        user.displayAge(username) 
        age = user.age

        #user.displayMajor(username) - will add later
        user.displayBio(username)
        bio = user.bio

        return render_template('profile.html', fullname = fullname, age = age, bio = bio) 
     
    else:
        user.check_sign_in()
        error = user.error

        return render_template('home.html', error = error) 
     
#  # map page - Abigail 
#  # connects to map controller and the html        
# @app.route('/map', methods= ['GET', 'POST'])
# def map():
    
#     if request.method == 'POST':
#         map = Map()
    
#         roomnumber = request.form.get("roomnumber")
#         roomImage = map.searchMap(roomnumber)
        
#         if roomImage is True:
#             return render_template('map.html', img = roomImage)
    
#     return render_template('map.html')

# map page - Abigail
# looked over the code since we were having problems displaying the image... adjusted the code to have the images pull from the database - Isaac
# connects to map controller and the html 
"""
@app.route('/map', methods=['GET', 'POST'])
def display_map():
    # using the database
    map= Map()
    map_image_data = None

    if request.method == 'POST':
        # inserted in the html page in the searchbar
        room_number = request.form.get('roomnumber')

        # get image from database on the room number
        map_image_data = map.searchMap(room_number)
    else:
        # default display without form submission (this should be the map campus)
        map_image_data = map.searchMap("Campus Map")
    
    return render_template('map.html', mapimage=map_image_data)
"""

>>>>>>> fb70b7bed65a2d05232431274408ecad2dce5ab6
@app.route('/clubs')
def index():
    clubs_controller = ClubsController()
    clubs = clubs_controller.get_clubs_info()

   # clubs = [
        #pulling the infomation from database of clubs to the website
        #{'name': user_info.get_club("Computer Science") , 'description': user_info.get_eventinfo("Computer Science") , 'contact': user_info.get_contact("Computer Science"), 'logo': user_info.get_image("Computer Science")},
        #{'name': user_info.get_club("Gaming") , 'description': user_info.get_eventinfo("Gaming") , 'contact': user_info.get_contact("Gaming"), 'logo': user_info.get_image("Gaming")},
  
        # Add more clubs as needed
    #]
    return render_template('clubs.html', clubs=clubs)
   
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)