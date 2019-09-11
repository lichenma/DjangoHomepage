## Building First Python and Django Application 

Shoutout to the awesome tutorials at scotch and I will be going through another one to familiarize myself with the Python language and the Django framework. 

Without further adieu let's get started. Python is a high level general purpose programming language. What this means is that you can use it to code up anything from a simple game to a website supporting millions of users per month. 

Advantages of Python: 

1. Easily readable syntax 
2. Awesome community around the language 
3. Easy to learn 
4. Useful for many tasks from basic shell scripting to advanced web development 


## When Not to Use Python 

If there are more specialized tool or specialized requirements for a task, it might be better to use another language. For example, when using an embedded system languages such as C, C++ and Java dominate. 


## Python 2 vs Python 3 

Python 3 introduced changes into the language which required applications written in Python 2 to be rewritten in order to work with the Python 3 branch. Currently many libraries required in this project have now been ported to Python 3 

This project will be using Python 3. 


## Coding Samples 

### Conditional Logic 

Here is some simple code to check if the user's age is over 18 and if it is, print `Access allowed` or `Access not allowed` otherwise. 


```Python 
# read in age 
age = int(input("what is your age?"))

if age>= 18:
    print("Access allowed")
elif age< 18 and age > 0: 
    print("Access not allowed")
else: 
    print("Invalid age")
```


The `input()` function is used to read in keyboard input as strings so we cast the value to an integer in order to use the comparator. 

### Abstract Data Types 

Python has many abstract data types which hold collections of items. An example is a `list` which can be used to hold variables of any type. The following code shows how to create a list and iterate through it to print each item to the terminal. 

```Python 
# create a list called my_list
my_list = [1, 2, 3, "python", 39, [1, 2]]

# go through the list and print everything 
for item in my_list:
    print item
```

This code above creates a list with numbers, a string, and a list. We are using a `for-in` loop to iterate through the list but we can also access values in the list using zero-indexed indecies. For example to retrieve the string `"python"` we can write: 

```python
print(my_list[3])
```


### Dictionaries 

Another useful data type which Python offers out of the box is dictionaries (very useful for leetcode). Dictionaries store key-value pairs, kind of like JSON objects. Creating a dictionary is quite simple as well. 

```python 
# create a dictionary 
person = {
    "name": "Lichen",
    "age": 20,
    "hobbies": ["Travelling", "Basketball", "Coding"]
}

# iterate through the dict and print the keys 
for key in person: 
    print(key)

# iterate through the dict's keys and print their values
for key in person: 
    print(person[key])

```


Now that we have an introduction to Python, we can take a look at Django. `Django` is a Python web framework. It is free and open source and has been around since 2005 - it is very mature and comes with excellent documentation and awesome features included by default. Some excellent tools it provides are: 

1. Excellent light weight server for development and testing 
2. Good templating language 
3. Security features like CSRF included right out of the box 

There are a myriad of other useful things included in Django but we will discover them as we go along. 


## Setting up 

Before we can get started with getting a Django website up and running, we need to grab a copy of the latest Python version from the Python website. 

To make sure it is installed, open up a terminal and type: 

```
$ py --version
```


## Setting up the Environment 

To avoid polluting our global scope with unnecessary packages, we are going to use a virtual environment to store our packages. One excellent virtual environment manager available for free is `virtualenv`. We will be using Python's package manager `pip` to install this and other packages like `Django` which we will require later on. First we need to install `virtualenv`. 

```
$ pip install virtualenv 
```

Once that is done, create a folder called `projects` and `cd` into it 

```
mkdir projects 
```

Now inside the projects folder, create another folder called `hello`. This folder will hold our app. 

```
mkdir hello
```

At this point we need to create the environment to hold our requirements. We will do this inside the `hello` folder. 


```
virtualenv -p /usr/local/bin/python3 env 
```

The `-p` switch tells virtualenv the path to the python version that you want to use. Feel free to switch out the path after it with your own Python installation path. The name `env` is the environment name. You can also change it to something else which fits the name of the project. 

Once that is done, we should have a folder called `env` inside your `hello` folder. The structure should now look something like this: 

```
projects
├─hello
│   ├── env
```

Now we can activate the environment and start coding! 


```bash
source env/bin/activate
```

You will now see a prompt with the environment name. This means that the environment is active. 

```
(env)
```


# Installing Django 

We can simply do this using pip install 

```bash 
pip install django
```


# Creating an App 

Now that we have Django installed, we can use its start script to create a skeleton project. This is as simple as using its admin script in the following way. 


```
django-admin startproject helloapp
```

Running this command creates a skeleton django app with the following structure: 

```
helloapp
├─helloapp
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

When you look into the `helloapp` folder that was created, you will find a file called `manage.py` and another folder called `helloapp`. This is the main project folder and contains the project's settings in a file called `settings.py` and the routes in your project in the file called `urls.py`. Let's take a look at the contents of the `settings.py` file: 




```python 
"""
Django settings for helloapp project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%+zia!d%ae26m!k=)a3-l-+kw@8f3f$eic7m@v*djq@!_%h-j0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helloapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'helloapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
```



# Changing App Settings 

Now let's change a couple of the settings. Open up the `settings.py` file and find a section called Installed Apps which looks something like this: 


```python
# helloapp/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```


Django operates on the concept of `apps`. An app is a self contained unit of code which can be executed on its own. An app can do many things such as serve a webpage on the browser or handle user authentication or anything else you can think of. Django comes with some default apps preinstalled such as authentication and session manager apps. Any apps we will create or third-party apps we will need will be added at the bottom of the `Installed Apps` list after the default apps installed. 


Before we create a custom app, let's change the application timezone. Django uses the `tz database` timezones and looks like this: 

```python 
# helloapp/settings.py

TIME_ZONE = 'UTC'
```

If you want, change it to something resembling this as appropriate for your timezone. 

```python
# helloapp/settings.py
TIME_ZONE = 'America/SanFranciso
```




# Creating your Own App 

It is important to note that Django apps follow the `Model, View, Template paradigm`. In a nutshell, the app gets data from a `model`, the `view` does soemthing to the data and then renders a `template` containing the processed information. As such, Django `templates correspond to views` in traditional MVC and Django `views can be likened to the controllers` found in traditional MVC. 


Now, lets create an app - `cd` into the first `helloapp` folder and type: 

```
python manage.py startapp intro
```

Running this command creates an app called `intro`. Your file structure should look something like this: 

```
helloapp
├── helloapp
│        ├── __init__.py
│        ├── settings.py
│        ├── urls.py
│        └── wsgi.py
├── intro
│        ├── __init__.py
│        ├── admin.py
│        ├── apps.py
│        ├── migrations
│        ├── models.py
│        ├── tests.py
│        └── views.py
└── manage.py
```

To get Django to recognize our brand new app, we need to add the app name to the `Installed Apps` list in our `settings.py` file. 


```python 
# helloapp/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'intro'
]
```


Once that is done we can run our server and check the output. We mentioned that `Django comes with a built in lightweight web server` which, while useful during development, should not be used in production. We can run the server as follows: 


```bash 
$ python manage.py runserver
```


The output should resemble the following: 


```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

June 04, 2016 - 07:42:08
Django version 1.9.6, using settings 'helloapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

We can see that there is a warning that we have unapplied migrations - we will ignore that warning for now. Now if we go to the browser and access `http://127.0.0.1:8000/` we should see the Django welcome page if all is running smoothly. 


We will be replacing this welcome page with our own template but first let's talk migrations. 



# Migrations 

Migrations make is easy for programmers to **change the database schema (model) without having to lose any data.** Any time that a new database model is created, running migrations will update the database tables to use the new schema without wiping out all of the data or forcing the user to go through the process of dropping and recreating the database. 


Django comes with some migrations already created for its default apps. If your server is still running stop it using the exit command `CTRL + C`. We can now apply the migrations by typing: 

```
$ python manage.py migrate
```

The output should look something like this: 

```
Operations to perform:
  Apply all migrations: sessions, auth, contenttypes, admin
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying sessions.0001_initial... OK
```

Running the server now will not show any warnings. 


# Urls and Templates 

When we ran the server, the default Django page was shown. We need Django to access our `intro` app when someone goes to the home page URL which is `/`. For that, we need to define a URL which will tell Django where to look for the homepage template. 


Open up the `urls.py` file inside the inner `helloapp` folder. It should look something like this. 



```python 
# helloapp/urls.py
 """helloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```



As you can see, there is an existing URL pattern for the Django admin site which comes by default with Django. Let's add our own url to point to our intro add. Edit the file to look like this: 


```python
# helloapp/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('howdy.urls')),
]
```



Note that we have added an import for `include` from django.conf.urls and added a url pattern for an empty route. When someone accesses the homepage, (in our case `http://localhost:8000`), Django will look for more url definitions in the `intro` app. Since there are none, running the app will produce a huge stack trace due to an `ImportError`. 


```
ImportError: No module named 'intro.urls'
```

Let's fix that, go to the `intro` app folder and create a file called `urls.py`. The `intro` app folder should now look like this. 


```
├── intro
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
```

Inside the new `urls.py` file, write this: 


```python
# intro/urls.py 
from django.conf.urls import url 
from intro import views 

urlpatterns = [
    path('$', views.HomePageView.as_view()), 
]
```

This code imports the views from our `intro` app and expects a view called `HomePageView` to be defined. Since we don't have one, open the `views.py` file in the `intro` app and write this code. 


```python
# intro/views.py
from django.shortcuts import render
from django.views.generic import TemplateView 

# Create the views here 
class HomePageView(TemplateView): 
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
```

This file defines a view called `HomePageView`. Django views take in a `request` and return a `response`. In our case, the method `get` expects a HTTP GET request to the url defined in our `urls.py` file. On a side note, we could rename our method to `post` to handle HTTP POST requests. 



Once a HTTP GET request has been received, the method renders a template called `index.html` which is just a normal HTML file which could have special Django template tags written alongside normal HTML tags. If you run the server now, you will see an error page which says: **TemplateDoesNotExist at /**

This is because we do not have any templates at all. Django looks for templates in a `templates` folder inside the application so we are going to create one for the `intro` app folder. 


```
$ mkdir templates
```

Go into the newly created templates folder and create a file called `index.html`: 

```bash
(env) hello/helloapp/howdy/templates
> touch index.html
```

Inside the `index.html` file, we have the following code: 

```html 
<!-- intro/templates/index.html -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Hello!</title>
    </head>
    <body>
        <h1>This is an introductory Django project!</h1>
    </body>
</html>
```

Now let's run the server: 

```
$ python manage.py runserver
```

Now we can see that the template has rendered if we start up the server again! 


# Linking pages 

Let's add another page. In the `intro/templates` folder, add a file called `about.html`. Inside it write this HTML code: 


```html
<!-- intro/templates/about.html -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Hello!</title>
    </head>
    <body>
        <h1>Welcome to the about page</h1>
        <p>
            This page was written by some dude called Lichen Ma 
        </p>
        <a href="/">Go back home</a>
    </body>
</html>
```

Once done let's edit the original `index.html` page to look like this: 

```html
<!-- intro/templates/index.html -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Hello!</title>
    </head>
    <body>
        <h1>This is an introductory Django project!</h1>
        <a href="/about/">About Me</a>
    </body>
</html>
```





