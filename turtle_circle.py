# -------------------------------------------
# Program: Make a circle outside of another circle
# Author: SD
# Date: 2/28/2023
# -------------------------------------------

import turtle

# Starting_number defines the starting y_coord, and how much it should go down by
starting_number = 50
# x is used for the while loop, so it should stay zero
x = 0


# Starting the turtle
turtle.showturtle()
turtle.penup()
starting_number1 = starting_number

# Increase the literal number to increase how long the program should run for.
# This also increase the amount of circles
while x < 20: 

    # Turns the turtle 180 degrees to the right so the all circles are the same direction
    turtle.right(180)

    # If x is not 0, then make the circle, if not don't
    # This resolves the bug, where the turtle would draw a circle at 0, 0 at the start of the program
    if not x == 0:
        turtle.circle(starting_number1)

    # Subtracts the starting_number1 by starting_number (default: 50) and assigns the difference to starting_number1
    # Ex: 50 - 50 = 0, 0 - 50 = -50, -50 - 50 = -100, and so on
    starting_number1 = starting_number1 - starting_number
    turtle.penup()
    turtle.goto(0, starting_number1)
    turtle.pendown()
    turtle.right(180)
    
    # Prints the y-coord 
    print("y =", starting_number1)

    x += 1
    
