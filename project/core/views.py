from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def home(request):
    Blog=blog.objects.latest()
    trips=Trip.objects.all()
    context={
        'blog':Blog,
        'trips':trips
    }
    return render(request,'home/index.html',context)
def all_blogs(request):
    blogs=blog.objects.all()
    context={
       'blogs':blogs
    }   
    return render(request,'home/blog.html',context)
def trip_details(request,pk):
    trip=get_object_or_404(Trip,id=pk)
    return render(request,'home/trip.html',{'trip':trip})
def about(request):
    return render(request,'home/about.html')
