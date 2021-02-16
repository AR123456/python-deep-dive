
#Exception Handling - file not found

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
# need to use a specific exception not just except:
except FileNotFoundError:
    # if the file is not found, create it
    file = open("a_file.txt", "w")
    file.write("Something")















