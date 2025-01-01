from turtle import Turtle

SLITHER = 20
SNAKE_LEN = 3
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SNAKE_COLOUR = "GreenYellow"
SNAKE_COLOUR_2 = "OliveDrab"
SNAKE_SHAPE = "square"

class Snake:
    def __init__(self):
        self.segs = []
        self.make_snake()
        self.head = self.segs[0]

    def make_snake(self):
        for x in range(0, (-SLITHER * SNAKE_LEN - 19), -SLITHER):
            new_seg = Turtle(SNAKE_SHAPE)
            new_seg.up()
            new_seg.color(SNAKE_COLOUR)
            new_seg.goto(x, 0)
            self.segs.append(new_seg)

    def move(self):
        for segNum in range(len(self.segs) - 1, 0, -1):
            next_seg_num = segNum - 1
            x_nsm = self.segs[next_seg_num].xcor()
            y_nsm = self.segs[next_seg_num].ycor()
            self.segs[segNum].goto(x_nsm, y_nsm)
        self.head.forward(SLITHER)

    def reset(self):
        for seg in self.segs:
            seg.hideturtle()
        self.segs.clear()
        self.make_snake()
        self.head = self.segs[0]

    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.head.setheading(DOWN)

    def eat(self):
        new_seg = Turtle(SNAKE_SHAPE)
        new_seg.color(SNAKE_COLOUR)
        new_seg.up()
        last_seg_x = self.segs[-1].xcor()
        last_seg_y = self.segs[-1].ycor()
        seg_head = self.segs[-1].heading()
        new_seg.goto(last_seg_x, last_seg_y)
        new_seg.setheading(seg_head)
        self.segs.append(new_seg)

    def ouch(self):
        for seg in self.segs:
            seg.color(SNAKE_COLOUR_2)
