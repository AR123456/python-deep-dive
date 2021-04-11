# Turtle
import turtle

#Panda

screen = turtle.Screen()
screen.title("US States Game ")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# pop up box
answer_state = screen.textinput(title="Guess a state ", prompt="Enter a state name ")


# an alterative to keeping window open so mouse click is not closing
turtle.mainloop()
# screen.exitonclick()