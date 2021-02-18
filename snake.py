from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        ## Setup Snake
        for coord in STARTING_POSITIONS:
            self.add_segment(coord)


    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            x_new = self.snake[seg_num - 1].xcor()
            y_new = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self,coord):
        snake_part = Turtle(shape="square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.goto(coord)
        self.snake.append(snake_part)

    def extend(self):
        self.add_segment(self.snake[-1].position())

