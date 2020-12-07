
import another_module
# print(another_module.another_variable)
# import turtle  or
# timmy = turtle.Turtle()

from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table =PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu","Electric"])
# table.add_row(["Squirtile","Water"])
# table.add_row(["Chamander","Fire"])

# Angelas solution

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charaander"])
table.add_column("Type",["Electric", "Water", "Fire"])

table.align ="l"
print(table)