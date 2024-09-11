from django.urls import path, include
from .views import *

urlpatterns = [  
    path('singup', user_singup, name='user_singup'),
    path('user_logout', user_logout, name='user_logout'),
    # other urls
]
