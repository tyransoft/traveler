from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def user_singup(request):
   if request.method == "POST":
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')
      confirm_password=request.POST.get('confirmpassword')
      if password== confirm_password:
         if User.objects.filter(username=username).exists():
           return redirect('user_singup')
         else:
            if User.objects.filter(email=email).exists():
             return redirect('user_singup')
              
            else:
              user=User.objects.create_user(username=username,email=email,password=password)
              our_user=authenticate(username=username,password=password)
              if our_user is not None:
               login(request,user)
               return redirect('/')
             
      else:
        return redirect('user_singup')
   return render(request,'registration/singup.html')
def user_logout(request):
    logout(request)
    return redirect('/')