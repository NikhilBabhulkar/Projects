from django.shortcuts import redirect, render
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username,password=password)
        #user =User.authenticate(username=username,password=password) 
        if user is not None:
            login(request,user)
            return redirect("/index")
        else:
            return redirect(request,'logout.html') 

    return render(request,'login.html')

def logout(request):
    logout(request)
    return render("/login")