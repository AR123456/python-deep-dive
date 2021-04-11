## Python Decorator Function
#  a decorator_function is just a function that wraps another
#  function and gives that function some additional functionality.
# the decorator_function can do some stuff and control the calling of the function passed in
#####   this function takes another function as an input
def decorator_function(function):
    #inside this decorator function nest the wrapper_function
    def wrapper_function():
        # the wrapper_function triggers the actual funtion that was passed into the decorator_function
        function()
    # returning the wrapper without parens
    return wrapper_function
