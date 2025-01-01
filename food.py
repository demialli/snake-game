from turtle import Turtle
import random


def rgb_to_hex(col_tuple):
    """converts an rgb tuple to a hex color string :3
      input: ONE rgb tuple (from either fillcolor() or pencolor(), NOT color()! that gives two!)
      output: the color as an uppercase hex colorstring with a #"""
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    to_return = ""
    for i in range(3):
        dig1 = int(col_tuple[i] // 16)
        dig2 = int(col_tuple[i] % 16)
        final = digits[dig1] + digits[dig2]
        to_return += final
    return "#" + to_return

class Food(Turtle):
    def __init__(self, screen): # passing in screen so i can change the colormode here
        super().__init__()
        screen.colormode(255)
        self.up()
        self.colours = ["#fc0356", "#fc8803", "#fcd703", "#03fc13",
                        "#037bfc", "#8c03fc", "#fc03f0"]
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color(random.choice(self.colours))
        self.speed("fastest")
        self.spawn()

    def pick_colour(self):
        new_col = random.choice(self.colours)
        current_col = rgb_to_hex(self.fillcolor()).lower()
        while new_col == current_col: # to avoid getting the same colour twice!
            new_col = random.choice(self.colours)
        self.color(new_col)

    def spawn(self): # only on game start!
        self.pick_colour()
        rand_x = random.randint(-14, 14)
        rand_y = random.randint(-14, 14)
        self.goto(rand_x * 20, rand_y * 20)

    def refresh(self, snake): # for rest of game!
        self.pick_colour()
        rand_x = random.randint(-14, 14)
        rand_y = random.randint(-14, 14)
        for seg in snake.segs: # to (try and) avoid it refreshing under the snake
            while seg.xcor() == rand_x*20:
                rand_x = random.randint(-14, 14)
            while seg.ycor() == rand_y*20:
                rand_y = random.randint(-14, 14)
        self.goto(rand_x * 20, rand_y * 20)