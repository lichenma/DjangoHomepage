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

