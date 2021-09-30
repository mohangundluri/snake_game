import turtle
import time
from snake import Snake
import food
import score

screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

snake = Snake()
score_board = score.Score()
food_dots = food.Food()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_going = True

while game_going:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food_dots) < 15:
        snake.extend_snake()
        food_dots.food_location()
        score_board.score_increase()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.game_over()
        game_going = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            game_going = False

screen.exitonclick()
