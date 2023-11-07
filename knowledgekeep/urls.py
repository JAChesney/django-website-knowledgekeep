from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userlogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.userlogout, name='logout'),
    path('addpaper/', views.addpaper, name='addpaper'),
    path('papers/', views.papers, name='papers'),
    path('description/<int:row_id>/', views.description, name='description'),
    path('user-account/', views.useraccount, name='user-account'),
    path('subscription/', views.subscription, name='subscription'),
    path('razorpay_order/', views.razorpay_order, name='razorpay_order'),
    path('access-denied/', views.access_denied, name='access-denied')
]
