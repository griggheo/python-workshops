# example 1 - manual decoration

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("hello!")

# decoration:
say_hello = my_decorator(say_hello)
print(type(say_hello))
say_hello()

# example 2 - syntactic sugar with @

def my_decorator2(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator2
def say_goodbye():
    print("Good-bye!")

say_goodbye()

# introducing functools.wraps

def my_decorator_plain(f):
     def wrapper(*args, **kwds):
         print('Calling decorated function')
         return f(*args, **kwds)
     return wrapper
@my_decorator_plain
def example1():
     """Docstring"""
     print('Called example1 function')
example1()
print(example1.__name__)
print(example1.__doc__)


from functools import wraps
def my_decorator_with_wraps(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print('Calling decorated function')
         return f(*args, **kwds)
     return wrapper
@my_decorator_with_wraps
def example2():
     """Docstring"""
     print('Called example2 function')
example2()
print(example2.__name__)
print(example2.__doc__)


# real-life example - timing a function

import time

def timer(func):
    """Print the run time of the decorated function"""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)]) 

waste_some_time(10)
waste_some_time(100)

# real-life example: requiring users to be logged in so they can see a particular page
"""
from flask import Flask, g, request, redirect, url_for
from functools import wraps
app = Flask(__name__)

def login_required(func):
    # Make sure user is logged in before proceeding
    @wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
"""

