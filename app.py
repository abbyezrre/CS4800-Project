# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session
from user import *
from map import *
from uProfile import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *
from search import *
from posting import PostingController
from login import *
from signup import *
# create the application object
app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def home():
    user = None
    if session.get('username') is not None:
        user = session.get('username')
        username = User()
        username.findUser(user)
        user = username.firstname
        
    return render_template('home.html',user=user, user_post=session.get('user_post'))  # render a template


#Helen - signin
@app.route('/signin', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #creating user object
        user = User()
        #made username variable global - Elvin
        global username 
    user= None
    global username
    if request.method == 'POST':
        
        
        #pulling info from html input
        username = request.form.get("username")
        password = request.form.get("password")

        login = loginPage(username, password)
        login.checkpassword()
        if login.loginStatus is True: 
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = login.error


    return render_template('signin.html', error=error)

 # map page - Abigail 
 # connects to map controller and the html     
 # made changes to map function by implementing some parts of Issac's code so image pops on the page
@app.route('/map', methods= ['GET', 'POST'])
def map():
    map = Map()
    
    if request.method == 'POST':
        
    
        roomnumber = request.form.get("roomnumber")
        roomImage = map.searchMap(roomnumber)

    else:
        roomImage = None
    
    return render_template('map.html', img = roomImage)

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
 
        if searching.clubValid == True:
            clubImage = searching.getClubImage(searchInput)
        else:
            clubImage = None
        
    output = sum(output,[])
    return render_template('search.html', output=output, input=input, len = len(output), img=clubImage)
#helen - sign out
#clears session user
@app.route('/signout', methods=['GET', 'POST'])
def signout():
    user=None
    session.clear()
    return render_template('home.html',user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #copied from signup.py, coded by Abby
    #modifications by Helen for connecting the controller to Flask
    #modifications by Helen to check if user exists in the database before user can sign up, and to check if passwords match
    #modifications by Helen to turn it into a class
    error = None
    if request.method == 'POST':
        #gets input from html boxes
        username = request.form.get("username")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")
        email = request.form.get("email")
        signup = signupPage(username, fname, lname, pass1, pass2, email)
        
        signup.signup()
        
        if signup.signupStatus == True:
            return redirect(url_for('login'))
        
        else:
            error = signup.error
        

    return render_template('signup.html', error=error)


# ... (previous code)

# Posting route - Isaac
@app.route('/posting', methods=['GET', 'POST'])
def posting():
    # Instantiate the PostingController class
    posting_controller = storingPost()
    post = pullingPostInfo()

    if request.method == 'POST':
        # Get the post content from the form
        post_content = request.form.get('postContent')

        # Set the user and comment in the PostingController instance
        posting_controller.set_user("Isaac Flores")
        posting_controller.set_comment(post_content)

        # Create a new document in the MongoDB collection
        posting_controller.create_new_document()

    
    # Retrieve the last 5 posts from the database
    last_5_posts = post.get_last_5_documents()

    # Render the posting.html template and pass the posts to it
    return render_template('posting.html', posts=last_5_posts)

# profile function - Elvin
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    username =session.get("username")
    
 
    error = None
    fullname = None
    age = None
    major = None
    bio = None

@app.route('/clubs')
def index():
    user_info = pullingClubInfo()
    clubs = [
        # pulling the infomation from database of clubs to the website
        {'name': user_info.get_club("Computer Science") , 'description': user_info.get_eventinfo("Computer Science") , 'contact': user_info.get_contact("Computer Science"), 'logo': user_info.get_image("Computer Science")},
        {'name': user_info.get_club("Gaming") , 'description': user_info.get_eventinfo("Gaming") , 'contact': user_info.get_contact("Gaming"), 'logo': user_info.get_image("Gaming")},
  
        #Add more clubs as needed
    ]
    # for club in clubs: 
    #     print(f"Club: {club['name']}, Image Path: {club['logo']}")
    return render_template('clubs.html', clubs=clubs)
   
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)