#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
#
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# f = open("./Input/Letters/starting_letter.txt", "r")
# print(f.readlines())
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# txt = "I like bananas"
#
# x = txt.replace("bananas", "apples")
#
# print(x)
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#
# txt = "     banana     "
#
# x = txt.strip()
#
# print("of all fruits", x, "is my favorite")

PLACEHOLDER ="[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name =name.strip()
        new_letter =letter_contents.replace(PLACEHOLDER,stripped_name)
        # print(new_letter)

