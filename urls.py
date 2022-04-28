from .views import *
from django.urls import path


urlpatterns = [
    path('',index,name='index'),
    path('account/signup',register,name='register'),
    path('account/registration',registeration,name='registration'),
    path('checkuser',checkuser,name='checkuser'),
    path('forgot',forgot,name='forgot'),
    path('sendotp',sendotp,name='sendotp'),]