# file not found
try:
    with open("a_file.txt") as file:
        file.read()
    a_dictionary = {"key":"value"}
    print(a_dictionary["sdfsde"])
except FileNotFoundError:
    print("There was an error")
except KeyError as error_message:
    print(f"This is the KeyError message: {error_message}")









