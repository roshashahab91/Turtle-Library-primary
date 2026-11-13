#Imports all functions and modules from the turtle library so we can use them directly without prefixing them with turtle..
from turtle import *

#Sets the background color of the drawing window. The string in parentheses (e.g., "red") specifies the color name or hex code.
bgcolor("red")

#Sets both the pen color and the fill color at the same time.
color("blue")

#Sets the thickness (width) of the pen line. The number in parentheses specifies the size in pixels (e.g., 10 makes a thick line).
pensize(10)

#Changes specifically the pen’s drawing color. The string inside parentheses specifies the color (e.g., "green").
pencolor("green")

#Changes the appearance of the turtle cursor itself. 
# The string in parentheses (e.g., "turtle", "arrow", "circle", "square") determines the shape icon.
shape("turtle")


#Keeps the drawing window open until you manually close it, preventing the program from exiting immediately.
done()