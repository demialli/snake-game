from turtle import Screen
from snake import Snake
from food import Food
from time import sleep
from scoreboard import ScoreBoard
# import DemiTools


# TODO-1: add delays between direction processing to stop instadeath when turning too quick!!


# initialising constants
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
BOUND = 300
SLEEP_TIME = 2.5


# cleaning scoresheet
with open("scoresheet.txt", "r") as file:
    score_lines = file.readlines()
clean_lines = []
for line in score_lines:
    if "0" not in line:
        clean_lines.append(line)
with open("scoresheet.txt", "w") as file:
    file.writelines(clean_lines)


# screen setup
screen = Screen()
screen.setup(width=620, height=620, startx=350, starty=-50)
screen.setworldcoordinates(-300, -307.5, 307, 300)
screen.bgcolor("black")
screen.title("demi snake")
screen.tracer(0)
screen.colormode(255)

# DemiTools.draw_grid()


# object creation
snake = Snake()
food = Food(screen)
scoreboard = ScoreBoard()


# event listener commands w variant inputs
screen.listen()

screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")

screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")


# main game loop
game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh(snake)
        snake.eat()
        scoreboard.inc_score()

    if snake.head.xcor() < -BOUND or snake.head.xcor() > BOUND or snake.head.ycor() < -BOUND or snake.head.ycor() > BOUND:
        snake.ouch()
        screen.update()
        print("you hit the wall!! you lose :PP")
        scoreboard.reset_game(screen)
        sleep(SLEEP_TIME)
        snake.reset()
        food.refresh(snake)
        print("\n"*20)

    for seg in snake.segs[2:]:
        if snake.head.distance(seg) < 10:
            snake.ouch()
            screen.update()
            print("you bit your tail! you lose :PP")
            scoreboard.reset_game(screen)
            sleep(SLEEP_TIME)
            snake.reset()
            food.refresh(snake)
            print("\n" * 20)

# print(f"your final score was {scoreboard.score}!")
#
#
# print("hehehe... goodbye!")

screen.exitonclick() # leave me down here!!
