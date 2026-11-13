from turtle import *

# Draw the first line (pen is down by default)
forward(100)

# Lift the pen up so moving won't draw any lines
penup()  # or pu()

# Move forward without drawing a line
forward(50)

# Put the pen down again to resume drawing
pendown()  # or pd()

# Draw the second line
forward(100)

done()
