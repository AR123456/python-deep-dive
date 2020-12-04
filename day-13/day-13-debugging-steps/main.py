############DEBUGGING#####################

# # Describe Problem - print 20 when i =20 
## def my_function():
#   #  does not work -for i in range(1,20):
#   for i in range(1,21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug - this sometimes works but not always 
# #from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 6)  - includes 6 
# # fixed index starts at 0 
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: - never catch =1994 
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
#   #  no lower bound 
# elif year < 1980:
#   print("You are not a GenZ or Millenial")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") - this needs to be int
# age = int(input("How old are you?"))
# if age > 18:
# # print("You can drive at age {age}.") - no f to print the age and need to indent 
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # word_per_page == int(input("Number of words per page: "))  - this needs to be one = sign 
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  # b_list.append(new_item) - this line needs to be indented
    b_list.append(new_item)

  print(b_list)

mutate([1,2,3,5,8,13])