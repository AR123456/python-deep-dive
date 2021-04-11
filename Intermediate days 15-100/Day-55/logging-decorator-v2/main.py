# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args,**kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0],args[1],args[2])
        print(f"It returned: {result}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(in1,in2,in3):
    return in1+in2+in3
a_function(1,2,3)