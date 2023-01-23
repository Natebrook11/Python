import turtle
import time

# Set up turtle
t = turtle.Turtle()

# Draw first circle
t.penup()
t.goto(-75, 0)
t.pendown()
t.circle(50)
# Draw second circle
t.penup()
t.goto(75, 0)
t.pendown()
t.circle(50)
# Draw large box with rounded top borders
t.penup()
t.goto(-25, 75)
t.pendown()
t.forward(50)
t.right(90)
t.forward(250)
t.right(90)
t.forward(50)
t.right(90)
t.forward(250)

text = "You like them kimetz?"

while True:

    # Write text
    t.penup()
    t.goto(0, -255)
    t.pendown()
    t.color("Black")
    t.write({text}, align="center", font=("Arial", 30, "normal"))
    # Wait for 3 seconds before starting again
    time.sleep(3)

    text = "Yes :)"

    t.clear

t.hideturtle()
turtle.done()
