from turtle import Screen

import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Classic Snake Game")
screen.tracer(0)

is_alive = True

snake = Snake()
screen.listen()

food = Food()
score = Score()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
while is_alive:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.add_cell()
        score.scorer()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        score.game_over()
        score.reset_score()
        snake.reset_positon()

    for cell in snake.snake[2:]:
        if snake.head.distance(cell) < 10:
            score.game_over()
            score.reset_score()
            snake.reset_positon()

screen.exitonclick()
