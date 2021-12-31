
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home,name='home'),
    path("about",views.about,name='about'),
    path("servises",views.servises,name='servises'),
    path("contact",views.contact,name='Contact')

]
