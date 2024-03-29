from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time

BOUNDARY = 290

""" Screen Setup """
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.add_to_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > BOUNDARY
        or snake.head.xcor() < -BOUNDARY
        or snake.head.ycor() > BOUNDARY
        or snake.head.ycor() < -BOUNDARY
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:

            scoreboard.reset()
            snake.reset()

screen.exitonclick()