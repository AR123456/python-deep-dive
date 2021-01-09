# Turtle
import turtle

#Panda
import pandas

screen = turtle.Screen()
screen.title("US States Game ")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []


#put in while loop so it repeats
while len(guessed_states) < 50:

    # pop up box
    # using .title to make user answer begin with cap even if they typed all lower case
    answer_state = screen.textinput(title=f"Guess a state. You have {len(guessed_states)} of 50 so far ",
                                    prompt="Enter a state name ").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        # a row of data
        state_data = data[data.state == answer_state ]
        # x and y attributes of the row of data
        t.goto(int(state_data.x), int(state_data.y) )
        t.write(answer_state)
        # alternative way using data from the csv
        # t.write(state_data.state.item())



# states_to_learn



# an alterative to keeping window open so mouse click is not closing
# turtle.mainloop()
# screen.exitonclick()