## Advanced Python Decorator Functions
# this class has 2 properties name and is_logged in
class User:
    def __init__(self, name):
        self.name = name
        #keeps track of user logged in or not
        self.is_logged_in = False
# this decorator function sets is logged in to ture
def is_authenticated_decorator(function):
    # call the funtcion passed in
    #unlimited postional **args
    #unlimited keyword **kwargs
    def wrapper(*args, **kwargs):
        #args[0] is user
        if args[0].is_logged_in == True:
            function(args[0])
    #return the wrapper as a function without the parens
    return wrapper

#call the decorator
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

# create user from the user class
new_user = User("angela")
# if this is set to false nothing happens
new_user.is_logged_in = True
# create blog post and pass in new user
create_blog_post(new_user)