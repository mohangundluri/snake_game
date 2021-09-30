from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.6, 0.6)
        self.color("green")
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.food_location()

    def food_location(self):
        self.showturtle()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)