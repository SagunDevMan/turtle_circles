#program: Make a circle outside of another circle
#author: SD
#date: 2/28/2023


import turtle

#sets the starting y coord
starting_number = 50
#starting loop increment 
x = 0
turtle.showturtle()
starting_number1 = starting_number
turtle.penup()
#if x is 10 or greater, then stop the program
while x < 10: # 10 can be changed to get more circles
    #turns the turtle 180 degrees, so the circles are all facing the same direction
    turtle.right(180)
    #if x is not 0, then make the circle, if it is, then don't
    if not x == 0:
        turtle.circle(starting_number1)
    #subtract the starting number from the initial number, so y can change
    starting_number1 = starting_number1 - starting_number
    turtle.penup()
    turtle.goto(0, starting_number1)
    turtle.pendown()
    turtle.right(180)
    #print the y coord
    print("y =", starting_number1)
    x += 1
    
