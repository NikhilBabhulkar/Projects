from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import About
from home.models import Contact
from django.contrib.messages import constants as messages

# Create your views here.

def home(request):
    # context ={
    #     "name": input("Enter some thing : ")
    # }
    
    return render(request,'home.html')
    
# def about(request):
#     if request.method =="POST":
#         name=request.POST.get('name')
#         abou =about(name=name,date=datetime.today())
#         abou.save()
        
    #return render(request,'about.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        about = About(name=name,date=datetime.today())
        about.save()
    return render(request,'about.html')
def servises(request):
    return render(request,'servises.html')

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact =Contact(name=name,email=email)
        contact.save()
        #messages.SUCCESS(request,'Your Message Is send Successfully')
    return render(request,'contact.html')