# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args,**kwargs):
        return
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(in1,in2,in3):
    return in1+in2+in3

print(a_function(1,2,3))