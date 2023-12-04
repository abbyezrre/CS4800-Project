# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session
from user import *
from map import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *
from search import *
from posting import PostingController
from login import *
from signup import *
# create the application object
app = Flask(__name__)


@app.route('/')
def home():
  
    return render_template('home.html', user_post=session.get('user_post'))  # render a template


#Helen - signin
@app.route('/signin', methods=['GET', 'POST'])
def login():
    error = None
    user= None
    if request.method == 'POST':
        #made username variable global - Elvin
        global username 
        #pulling info from html input
        username = request.form.get("username")
        password = request.form.get("password")

        login = loginPage(username, password)
        login.login()
        if login.loginStatus is True: 

            return redirect(url_for('home'))
        else:
            error = login.error


    return render_template('signin.html', error=error)

 

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
    #pulls user info from database
    dbase = pullingUserInfo()
    
    #so far updates user profile from datatbase, will work on edit function 
    try :
       
        f = dbase.get_fullname(username)
        b = dbase.get_bio(username)
        update = render_template('profile.html', fullname = f, bio = b)
        #TO DO: still need to add image and major maybe?
        return update
    except:
        #throws error if not signed in
        
        return render_template('home.html', error = "please sign in")  

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


@app.route('/clubs')
def index():
    user_info = pullingClubInfo()
    clubs = [
        #pulling the infomation from database of clubs to the website
        {'name': user_info.get_club("Computer Science") , 'description': user_info.get_eventinfo("Computer Science") , 'contact': user_info.get_contact("Computer Science"), 'logo': user_info.get_image("Computer Science")},
        {'name': user_info.get_club("Gaming") , 'description': user_info.get_eventinfo("Gaming") , 'contact': user_info.get_contact("Gaming"), 'logo': user_info.get_image("Gaming")},
  
        # Add more clubs as needed
    ]
    return render_template('clubs.html', clubs=clubs)
   
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)