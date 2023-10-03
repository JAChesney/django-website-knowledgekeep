from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

# Create your views here.
def home(request):
    return render(request, 'mainfiles/home.html', {}) 

def userlogout(request):
    logout(request)
    return redirect('/')

def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)

        user = UserProfile.objects.get(email=email)
        print(user)

        if not user:
            print('User does not exist')

        # Authenticate user
        user = authenticate(email=email, password=password)

        print(user)

        # Log user in
        if not user:
            print('Error logging in!')

        
        login(request, user)

        # Redirecting to home
        return redirect('/')
    
    return render(request, 'mainfiles/login.html', {})

def signup(request):
    print(request.method)
    # Once using POST add the name to the header and check
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)

        # Check whether user already exist

        # Adding user to database
        user = UserProfile(full_name=username, email=email)
        user.set_password(password)
        user.save()

        user = UserProfile.objects.get(email=email)

        # Authenticate user
        user = authenticate(email=email, password=password)

        print(user)

        # Log user in
        if not user:
            print('Error logging in!')

        
        login(request, user)

        # Redirecting to home
        return redirect('/')

    return render(request, 'mainfiles/signup.html', {})