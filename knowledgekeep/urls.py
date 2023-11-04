from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userlogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.userlogout, name='logout'),
    path('addpaper/', views.addpaper, name='addpaper'),
    path('papers/', views.papers, name='papers'),
]
