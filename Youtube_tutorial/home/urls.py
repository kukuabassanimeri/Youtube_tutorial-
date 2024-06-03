from django.contrib import admin
from django.urls import path
from . import views
#from .views import register
from .views import signup

urlpatterns = [
    path('home/', views.home, name='home'),
    #path('text/', views.text, name='text'),
    path('signup/', signup, name='signup'),
    
]
