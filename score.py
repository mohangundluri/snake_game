from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(230, 280)
        self.hideturtle()
        self.color("blue")
        self.write(f"Score : {self.score}", align="center", font=('Times New Roman', 15, 'normal'))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=('Times New Roman', 15, 'normal'))

    def game_over(self):
        self.penup()
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=('Times New Roman', 25, 'normal'))