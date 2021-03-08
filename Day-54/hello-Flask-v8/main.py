import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #do something before
        function()
        #do something after
    return wrapper_function

#call the delay_decorator in front of the methods we want to daly
# use @
@delay_decorator
def say_hello():
     print("Hello")
@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you ?")

say_greeting()