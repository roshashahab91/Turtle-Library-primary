#Imports all functions and modules from the turtle library so we can use them directly without prefixing them with turtle..
from turtle import * 

#Moves the turtle forward by 100 pixels in the direction it is currently facing, drawing a line as it moves.
#The number in parentheses tells the turtle how many units to move forward.
forward(100)

#Moves the turtle backward by 100 pixels (opposite to the direction it is facing) without changing its heading.
#The number in parentheses tells the turtle how many units to move backward.
backward(100)

#Turns the turtle’s heading 90 degrees counterclockwise (to the left).
#The number in parentheses tells the turtle how many degrees to turn left.
left(90)

#Turns the turtle’s heading 90 degrees clockwise (to the right).
#The number in parentheses tells the turtle how many degrees to turn right.
right(90)


#Keeps the drawing window open until you manually close it, preventing the program from exiting immediately.
done()