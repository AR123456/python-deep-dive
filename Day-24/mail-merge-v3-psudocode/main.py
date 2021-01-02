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

#TODO Make the invites_names.txt into a list
name_list = open("./Input/Names/invited_names.txt", "r")
# print(name_list.readlines())
#TODO loop the list and add to the name var in the starting letter
for name in name_list:
    # print(name)
    with open("./Input/Names/invited_names.txt",mode="a")as file:
        file.write( (txt.replace(name,name)) )

#TODO save each appened letter into a new file written to the Ready to Send dir.