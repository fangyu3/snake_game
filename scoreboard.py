from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Read high score from file
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Store highscore on file
            with open("data.txt","w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()