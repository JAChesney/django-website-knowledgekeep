from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, Papers
import datetime
from dateutil.relativedelta import relativedelta
import razorpay
import json
from django.http import HttpResponse

# Create your views here.
def home(request):
    papers = Papers.objects.all().order_by('id')[:3][::-1]
    return render(request, 'mainfiles/home.html', {'papers': papers}) 

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

def addpaper(request):

     # uploading file
    if request.method == 'POST':
        paper_title = request.POST['paper-title']
        paper_type = request.POST['paper-type']
        paper_description = request.POST['paper-description']
        short_description = request.POST['short-paper-description']
        published = request.POST['is-published']
        paper_file = request.FILES['file']

        # saving details to paper table
        paper = Papers(user=request.user, paper_name=paper_title, paper_description=paper_description, type=paper_type, is_published=published == 'yes', file=paper_file, short_description=short_description)
        paper.save()

    return render(request, 'mainfiles/addpaper.html', {})

def access_denied(request):
    return render(request, 'mainfiles/access-denied.html', {})

def papers(request):
    papers = Papers.objects.filter(reviewed=True)
    print(papers)
    return render(request, 'mainfiles/papers.html', {'papers': papers})

def description(request, row_id):
    try:
        single_row = Papers.objects.get(id=row_id)
    except Papers.DoesNotExist:
        pass # Handle the case when the row doesn't exist

    context = {
        'single_row': single_row,
    }
    return render(request, 'mainfiles/description.html', context)

def useraccount(request):
    # checking whether user has subscribed
    if request.user.has_subscribed:
        # get plan
        plan = int(request.user.subscription_type[0]) 
        ends_on = (request.user.subscribed_on + relativedelta(months=12 if plan == 1 else plan)).strftime("%d/%m/%Y")

        return render(request, 'mainfiles/user-account.html', { 'ends_on': ends_on})
    return render(request, 'mainfiles/user-account.html', {})

def subscription(request):
    if request.method == 'POST':
        plan = request.POST['plan']
        user = UserProfile.objects.get(email=request.user.email)
        user.has_subscribed = True
        user.subscription_type = plan
        user.subscribed_on = datetime.datetime.now()
        user.save()

        # Redirecting to home
        return HttpResponse(json.dumps({
            'status': 'ok'
        }))
    
    return render(request, 'mainfiles/subscription.html', {})

def razorpay_order(request):
    plan = request.POST['plan']

    # get amount
    if plan == '3months':
        price = '49'
    elif plan == '6months':
        price = '89'
    else:
        price = '129'

    client = razorpay.Client(auth=("rzp_test_6sinDDTQYunkhF", "kcSpttFexXxpoitahsj7BgIv"))
    data = {"amount": int(price) * 100, "currency": "INR", "receipt": str(datetime.datetime.now())}
    payment = client.order.create(data=data)
    return HttpResponse(json.dumps(payment))