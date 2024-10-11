

from django.urls import path

from . import views

urlpatterns = [

#url configuration module
path('hello/', views.say_hello)  # route:str, function reference

]

# always end our route with a forward slash