
# Functions inputs/fucntionality/output
def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

# Python functions are first class objects, the can be passed around as arguments
# treated like an  int/string/float
# we can take functions and build another function that uses the functions

def calculate(calc_function,n1,n2):
    return calc_function(n1,n2)

result = calculate(multiply,2,3)
print(result)