from turtle import Turtle
POSITION_COORDINATES = [0, -20, -40]


class Snake:
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def create_snake(self):
        global POSITION_COORDINATES
        for position in POSITION_COORDINATES:
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(position, 0)
            self.segments.append(segment)

    def extend_snake(self):
        x = self.segments[len(self.segments)-1].xcor()
        y = self.segments[len(self.segments)-1].ycor()
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(x, y)
        self.segments.insert(len(self.segments)-1, new_segment)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)