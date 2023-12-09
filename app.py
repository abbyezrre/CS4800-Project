# written by: Isaac (posting & club)
# tested by: Isaac (posting $ clubs)
# debugged by: Isaac (posting & club)

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
#from clubs import ClubsController

# create the application object
app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def home():
    user = None
    #helen
    # if user is logged in, show "hello FirstName" of the user
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
    #made username variable global - Elvin
    global username
    if request.method == 'POST':
        
        #pulling info from html input
        username = request.form.get("username")
        password = request.form.get("password")

        #creating login class
        login = loginPage(username, password)
        #checks to see if passwords match
        login.checkpassword()
        #if logins match, username is saved in the session and user is redirected to the home page
        if login.loginStatus is True: 
            session['username'] = username
            return redirect(url_for('home'))
        #shows login error 
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
        #if it finds a match for a club, itll display the club image
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
        #creating signup class with
        signup = signupPage(username, fname, lname, pass1, pass2, email)
        
        signup.signup()
        
        if signup.signupStatus == True:
            return redirect(url_for('login'))
        
        else:
            error = signup.error
        

    return render_template('signup.html', error=error)



# posting route - Isaac
@app.route('/posting', methods=['GET', 'POST'])
def posting():
    # instantiate the PostingController class
    posting_controller = PostingController()


    # retrieve the last 5 posts from the database using the correct method
    last_5_posts = posting_controller.get_last_5_documents()


    # render the posting.html template and pass the posts to it
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
     


@app.route('/clubs')
def index():
    #clubs_controller = ClubsController()
    #clubs = clubs_controller.get_clubs_info()
    user_info = pullingClubInfo()
    clubs = [
        # pulling the infomation from database of clubs to the website
        {'name': user_info.get_club("Computer Science") , 'description': user_info.get_eventinfo("Computer Science") , 'contact': user_info.get_contact("Computer Science"), 'logo': user_info.get_image("Computer Science")},
        {'name': user_info.get_club("Gaming") , 'description': user_info.get_eventinfo("Gaming") , 'contact': user_info.get_contact("Gaming"), 'logo': user_info.get_image("Gaming")},
        {'name': user_info.get_club("Theatre"), 'description': user_info.get_eventinfo("Theatre"), 'contact': user_info.get_contact("Theatre"), 'logo': user_info.get_image("Theatre")},
        {'name': user_info.get_club("Anthropology"), 'description': user_info.get_eventinfo("Anthropology"), 'contact': user_info.get_contact("Anthropology"), 'logo': user_info.get_image("Anthropology")},
        {'name': user_info.get_club("Women's Club"), 'description': user_info.get_eventinfo("Women's Club"), 'contact': user_info.get_contact("Women's Club"), 'logo': user_info.get_image("Women's Club")},
        {'name': user_info.get_club("Math"), 'description': user_info.get_eventinfo("Math"), 'contact': user_info.get_contact("Math"), 'logo': user_info.get_image("Math")},
        {'name': user_info.get_club("SIAM"), 'description': user_info.get_eventinfo("SIAM"), 'contact': user_info.get_contact("SIAM"), 'logo': user_info.get_image("SIAM")},
        {'name': user_info.get_club("Accounting & Finance"), 'description': user_info.get_eventinfo("Accounting & Finance"), 'contact': user_info.get_contact("Accounting & Finance"), 'logo': user_info.get_image("Accounting & Finance")},
        {'name': user_info.get_club("Black Student Union"), 'description': user_info.get_eventinfo("Black Student Union"), 'contact': user_info.get_contact("Black Student Union"), 'logo': user_info.get_image("Black Student Union")},
        {'name': user_info.get_club("Geography"), 'description': user_info.get_eventinfo("Geography"), 'contact': user_info.get_contact("Geography"), 'logo': user_info.get_image("Geography")},
        {'name': user_info.get_club("NASA"), 'description': user_info.get_eventinfo("NASA"), 'contact': user_info.get_contact("NASA"), 'logo': user_info.get_image("NASA")},
        {'name': user_info.get_club("Photography"), 'description': user_info.get_eventinfo("Photography"), 'contact': user_info.get_contact("Photography"), 'logo': user_info.get_image("Photography")},
        {'name': user_info.get_club("Pre-dental Society"), 'description': user_info.get_eventinfo("Pre-dental Society"), 'contact': user_info.get_contact("Pre-dental Society"), 'logo': user_info.get_image("Pre-dental Society")},
        {'name': user_info.get_club("Sociology"), 'description': user_info.get_eventinfo("Sociology"), 'contact': user_info.get_contact("Sociology"), 'logo': user_info.get_image("Sociology")},
        {'name': user_info.get_club("The Outlet"), 'description': user_info.get_eventinfo("The Outlet"), 'contact': user_info.get_contact("The Outlet"), 'logo': user_info.get_image("The Outlet")},
        {'name': user_info.get_club("Warriors Chemistry"), 'description': user_info.get_eventinfo("Warriors Chemistry"), 'contact': user_info.get_contact("Warriors Chemistry"), 'logo': user_info.get_image("Warriors Chemistry")},
        {'name': user_info.get_club("InterVarsity Christian Fellowship"), 'description': user_info.get_eventinfo("InterVarsity Christian Fellowship"), 'contact': user_info.get_contact("InterVarsity Christian Fellowship"), 'logo': user_info.get_image("InterVarsity Christian Fellowship")},
        {'name': user_info.get_club("Language"), 'description': user_info.get_eventinfo("Language"), 'contact': user_info.get_contact("Language"), 'logo': user_info.get_image("Language")},
        {'name': user_info.get_club("Honors Endeavor"), 'description': user_info.get_eventinfo("Honors Endeavor"), 'contact': user_info.get_contact("Honors Endeavor"), 'logo': user_info.get_image("Honors Endeavor")},
        {'name': user_info.get_club("Eco Warriors"), 'description': user_info.get_eventinfo("Eco Warriors"), 'contact': user_info.get_contact("Eco Warriors"), 'logo': user_info.get_image("Eco Warriors")},
        #Add more clubs as needed
    ]

    return render_template('clubs.html', clubs=clubs)
   
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)