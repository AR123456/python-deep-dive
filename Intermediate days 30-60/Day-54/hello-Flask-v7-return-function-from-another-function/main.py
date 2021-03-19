

# functions can be returned form other functions

# note indentation
def outer_function():
    print("I am outer ")
    # scope - this function is only accessable inside the outer function
    def nested_function():
        print("I am inner")

# to call - note indentation we are in the outer function
    # can return the nested function
    return nested_function
# outer_function()
# inter function is equal to the the output of the outer function - which is the nested function
inner_function = outer_function()
inner_function()