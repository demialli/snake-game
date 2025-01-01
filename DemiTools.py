from turtle import Turtle, Screen

def draw_grid():
    # draw chequer pattern!!
    screen = Screen()
    screen.setup(width=620, height=620, startx=350, starty=-50)
    screen.bgcolor("black")
    screen.colormode()

    hakkai = Turtle("square")
    hakkai.color("#28233d")
    hakkai.up()
    ypos = 300
    for i in range(15):
        for x in range(-300, 280, 40):
            hakkai.goto(x, ypos)
            hakkai.stamp()
        ypos -= 20
        for x in range(280, -300, -40):
            hakkai.goto(x, ypos)
            hakkai.stamp()
        ypos -= 20
    for x in range(-300, 280, 40):
        hakkai.goto(x, ypos)
        hakkai.stamp()

    # Set up the screen

    # Create a turtle for drawing the grid
    grid_turtle = Turtle()
    grid_turtle.speed(0)  # Fastest drawing speed
    grid_turtle.hideturtle()
    grid_turtle.color("lightgray")

    # Draw vertical lines
    for x in range(-300, 301, 50):
        grid_turtle.penup()
        grid_turtle.goto(x, -300)
        grid_turtle.pendown()
        grid_turtle.goto(x, 300)

    # Draw horizontal lines
    for y in range(-300, 301, 50):
        grid_turtle.penup()
        grid_turtle.goto(-300, y)
        grid_turtle.pendown()
        grid_turtle.goto(300, y)

    # Draw x and y axes
    grid_turtle.pensize(3)
    grid_turtle.color("white")
    grid_turtle.penup()
    grid_turtle.goto(-300, 0)
    grid_turtle.pendown()
    grid_turtle.goto(300, 0)

    grid_turtle.penup()
    grid_turtle.goto(0, -300)
    grid_turtle.pendown()
    grid_turtle.goto(0, 300)

    # Add axis labels
    label_turtle = Turtle()
    label_turtle.hideturtle()
    label_turtle.penup()
    label_turtle.color("white")

    for x in range(-300, 301, 50):
        label_turtle.goto(x, -20)
        label_turtle.write(str(x), align="center", font=("Arial", 8, "normal"))

    for y in range(-300, 301, 50):
        label_turtle.goto(-8, y)
        label_turtle.write(str(y), align="right", font=("Arial", 8, "normal"))

    # thick brat green boundary lines (horizontal/vertical)
    def draw_line(turtle, start_pos, heading, distance):
        turtle.up()
        turtle.goto(start_pos)
        turtle.setheading(heading)
        turtle.down()
        turtle.forward(distance)

    grid_turtle.pensize(5)
    grid_turtle.color("chartreuse3")

    # Draw the grid lines
    draw_line(grid_turtle, (-310, 310), 0, 620)  # Top horizontal line
    draw_line(grid_turtle, (-310, -310), 0, 620)  # Bottom horizontal line
    draw_line(grid_turtle, (-310, -310), 90, 620)  # Left vertical line
    draw_line(grid_turtle, (310, -310), 90, 620)  # Right vertical line
