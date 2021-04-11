# Turtle
import turtle

#Panda
import pandas
correct =0
screen = turtle.Screen()
screen.title("US States Game ")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
state_x = data["x"].to_list()
state_y = data["y"].to_list()

# pop up box
# answer_state = screen.textinput(title=f"Guess a state. You have {correct} of 50 so far ", prompt="Enter a state name ")
# for i in state_list:
#     if i == answer_state:
#         # print on screen
#         print(answer_state)
#         turtle.goto(-212, 20)
#         turtle.write(answer_state)
#         correct +=1

# if answer_state is one of the answers in the state list (column)
# print the state name at its give x,y cord
# increate count of states found
# show prompt to enter state again
# else just show prompt again

# Give up an print them all
for i in state_list:
    turtle.goto(state_x, state_y)
    turtle.write(state_list)






# an alterative to keeping window open so mouse click is not closing
turtle.mainloop()
# screen.exitonclick()