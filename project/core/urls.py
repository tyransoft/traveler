from django.urls import path,include
from .views import *

urlpatterns = [
  path('',home,name='/'),
  path('blogs',all_blogs,name='all_blogs'),
  path('trip_details/<int:pk>',trip_details,name='trip'),
  path('about_me',about,name='about')
]