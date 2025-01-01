from turtle import Turtle
ALIGN = "center"
FONT = ("Comic Sans MS", 20, "normal")


def get_hs():
    numbers = []
    with open("scoresheet.txt", "r") as file:
        for line in file:
            numbers.append(int(line.strip()))
    return max(numbers)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.highscore = get_hs()
        with open("high_scorer.txt", "r") as file:
            self.high_scorer = file.read()
        self.color("magenta")
        self.update()

    def new_highscore(self, screen):
        high_scorer = screen.textinput(title="NEW HIGH SCORE!!!", prompt="what's your name champ")
        self.high_scorer = high_scorer
        with open("high_scorer.txt", "r+") as file:
            file.write(high_scorer)

    def update(self):
        self.clear()
        self.color("magenta")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.color("cyan")
        self.goto(0, -295)
        self.write(f"High Score: {self.highscore} ({self.high_scorer})", align=ALIGN, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update()

    def reset_game(self, screen):
        death_turt = Turtle()
        death_turt.clear()
        death_turt.color("red")
        death_turt.up()
        death_turt.hideturtle()
        death_turt.goto(0,-40)
        death_turt.write("YOU DIEDED", align="center", font=("Courier", 50, "bold"))
        screen.update()
        with open("scoresheet.txt", "a") as file:
            file.write(str(self.score) + "\n")
        if self.score > self.highscore:
            self.new_highscore(screen)
            self.highscore = get_hs()
        self.score = 0
        death_turt.clear()
        self.update()

    # def you_died(self):
    #     self.color("red")
    #     self.goto(0,0)
    #     self.write("YOU DIED", align="center", font=("Courier", 50, "bold"))
