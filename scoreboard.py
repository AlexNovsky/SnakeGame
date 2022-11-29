from turtle import Turtle
ALINGMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hscore = 0
        self.high_score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def write_hscore(self):
        with open("score_base.txt", "w") as file:
            file.write(f"{self.high_score}")

    def read_hscore(self):
        with open("score_base.txt") as file:
            self.hscore = file.read()

    def update_scoreboard(self):
        self.clear()
        self.read_hscore()
        self.write(f"Score: {self.score}  Highest score: {self.hscore}", align=ALINGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_hscore()
        self.score = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
