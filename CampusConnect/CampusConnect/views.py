from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from CampusConnect.fakeB import FakeData

user_posts = []
# Abigail
def map(request):
    template = "map.html"
    return render(request, template)

def home(request):
    global user_post
    return render(request, "index.html")


def clubs(request):
    return render(request, "hub.html")

def post(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        print(f"Name: {name}, Message: {message}")

        global user_post
        user_post.append({'name': name, 'message': message})

        return redirect('home')
    
    return render(request, "posting.html")

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {'fname': fname})
            
        else:
            messages.error(request, "Invalid Credentials")
        
    return render(request, "signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "Your account has been created.")
 
        return redirect('signin')
        
        
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

def profile(request):
    return render(request, "profile.html")
