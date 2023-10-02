from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mainfiles/home.html', {}) 

def userlogin(request):
    return render(request, 'mainfiles/login.html', {})

def signup(request):
    return render(request, 'mainfiles/signup.html', {})