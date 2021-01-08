sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# sent_list = sentence.split()
# new_dict ={new_key:new_value for item in list }
# result = {word:len(word) for word in sent_list}
result = {word:len(word) for word in sentence.split()}
print(result)

