from turtle import Turtle
ALINGMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()