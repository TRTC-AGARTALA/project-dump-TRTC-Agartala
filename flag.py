import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Indian National Flag - Turtle Graphics")
screen.bgcolor("skyblue")
screen.setup(width=900, height=600)

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to draw rectangle
def rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()


# Flag dimensions
x = -350
y = 250
width = 700
height = 120

# Saffron
rectangle(x, y, width, height, "orange")

# White
rectangle(x, y - 120, width, height, "white")

# Green
rectangle(x, y - 240, width, height, "green")


# Ashoka Chakra
t.penup()
t.goto(0, 10)
t.pendown()
t.color("navy")

# Outer circle
t.circle(60)

# 24 spokes
for i in range(24):
    t.penup()
    t.goto(0, 10)
    t.setheading(i * 15)
    t.forward(60)
    t.pendown()
    t.goto(0, 10)


# Flag pole
t.penup()
t.goto(-350, 250)
t.setheading(270)
t.color("brown")
t.pendown()
t.pensize(8)
t.forward(450)

# Ground
t.penup()
t.goto(-430, -200)
t.setheading(0)
t.color("darkgreen")
t.pensize(5)
t.pendown()
t.forward(860)


# Text
t.penup()
t.goto(-180, -270)
t.color("navy")
t.write("JAI HIND 🇮🇳", font=("Arial", 30, "bold"))

# Keep window open
screen.mainloop()