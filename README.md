<div style="text-align: center;">
 # PART-1
</div>


## Reauirements
 - Python
 - Relational Database



 ## Django Fundamentals

 - Introduction to Django
 - Fundamental of web development
 - Setting up the development environment
 - first project 
 - 2 seasonal debugging techniques


### What is Django?
- Free and open-source framework for building web apps with Python. It's not the only one but a most famous one

- Companies using Django
  - youtube, Instagram, Spotify, dropbox


### Django features
 - The admin site: Managing our data
 - Object-relational mapper (ORM): abstract database
 - Authentication: for identifying users
 - Caching: caching data

**Core concept of web development**

There are two main parts of web development namely, client site and server site. let's say when we type something say for google.com {this is called URL: uniform resource locator} at the client site,
then a request goes to the server site and tells that the client wants to know about the home page of google.com. then information/data is sent back to the client site. This way of passing information 
is called HTTP. The information can be sent either by generating a home page {html file} or by sending the data. It's more convenient to send only data because the server site can be used to serve more clients.
and therefore the html pages are now part of the client's site. and the data processing is part of the server site. For example, react, and angular are on the client site, and Django for example is a part of the backend or
client site part 


**API:**
So if we push the responsibility of generating web pages to the client, the server essentially becomes a gateway to the data. At the server we can provide endpoints that  the client can talk to,
to get or save various pieces of data. For example, we  provide one endpoint to get  the list of products, other for order list and so on. All the endpoints together represent the interface that the 
client use to talk to the server. In technical terms, we say that the server provides an API (application interface programming). So our focus is to build an API using Django


### Setting up the development Environment

- Download the latest version of Python

- install pipenv by typing the following at the command prompt

       - pip install pipenv

  ## Creating the first Django project

- create a Django project by typing the following command

      - pipenv install django

- this will create a virtual environment and install Django into that Environment
- additionally, this will create also two files namely Pipfile and Pipfile. lock. Pipfile is like package.json for Java script project.
- to activate the virtual Environment in order to use Python interpreter in this environment not the global run the following command
   
      - pipenv shell

- we will use Django-admin to start a new project
  
       - django-admin

- django-admin is a utility that comes with Django
-to create a project run the following command

      - django-admin startproject projectname .

- the dot creates the project inside that folder where you are running your command

- After creating the project there will be several files inside it. Among them
 
  - __init__.py: which defines the directory as a package
  - Settings.py: where we will define our application setting 
  - urls.py: where we will define the URLs of our application
  - asgi.py and wsgi.py: used for deployment of our application

  
**Note** Outside the project directory there will be a manage.py file this is a wrapper  around Django admin. So going forward instead of Django-admin we're going to use this file. Because this
file takes the settings of this project into account. For example, another command run server if we run using the Django-admin run server we will get the error " Requested setting INSTALLED_APPS,
but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.)." so instead of running it we will use
"python manage.py run server port number" we can set the port number optionally. By default, it takes 8000. if another application is running using this default we should give a new port number.
if we run it we will get something like "Starting development server at http://127.0.0.1:8000/". If we run the https address in the browser we will get our application. compy paste onbly 127.0.0.1:8000/ to the browser.

## Creating the first app

Each Django project is a collection of various apps each providing certain functionality. In the settings module there are several apps that are default namely,

   - 'django.contrib.admin': gives an admin interface
   - 'django.contrib.auth': for authenticating users
   - 'django.contrib.contenttypes' : 
   - 'django.contrib.sessions': session is a temporary memory on
                                 server  for managing users data. We don't use it when we build Django API. so we will delete this
   - 'django.contrib.messages': used to display one-time notifications 
                                 to user
   - 'django.contrib.staticfiles': used for serving staticfiles such 
                                    as CSS, images and so on


We can create a new app of our own for this we need to run the following command 

      - python manage.py startapp appname

every app has the same structure inside it. Each has, __init__.py, admin.py, apps.py, models.py, tests.py, views.py. The most important thing is that every time we create an app we need to register it 
inside the settings.py of the main project.



## Writing views : 

we already know that every data exchange between client and server requires a request and a response, this is where we use **views** in Django. it receives a request and returns a response, so it can be called
a request handler.

- we need to map each view to a URL, so using the URL this view can be called


## Mapping URL to views

we need to create a URLS in the app folder, and also add that URL in the main project URL section


## Using templates

templates are used to return html content to the users. For using templates we need to create a folder inside the app folder, here inside the playground we create a template folder and inside it, 
we create a hello.html file which is a template. We need to create URLs in the view for each template.

## Debuging toolbar

Go to the following link and follow the instructions
link: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

## Models 

- are used to store and retrieve data

What will we learn?
  - introduction to data
  - building an e-commerce data model
  - organizing models in apps
  - Coding model classes

### Introduction to data modeling
  



