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





