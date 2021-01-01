#
# file= open("my_file.txt")
#
# contents =file.read()
# print(contents)
# #also need to close the file
# file.close()

####### another way to open a file that dosent require an explice file.close, does it for you
#this is read only mode - mode defaluts to "r
with open("my_file.txt")as file:
    contents = file.read()
    print(contents)

#######3 #write to a file
with open("my_new.txt", mode="w")as file:
    # This overwrites, or if no file exists it will be created
    file.write("Some new text ")

# write by appending to the file
with open("my_file.txt", mode="a")as file:
    file.write("\nAnd soup is good too ! ")

with open("my_file.txt")as file:
    contents = file.read() 
    print(contents)
