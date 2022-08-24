from turtle import Turtle

snake_position = [(0, 0), (-20, 0), (-40, 0)]
move_speed = 20
up = 90
down = 270
right = 0
left = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in snake_position:
            self.create_cell(position)

    def reset_positon(self):
        for cell in self.snake:
            cell.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def create_cell(self, position):
        cell = Turtle("square")
        cell.color("white")
        cell.penup()
        cell.goto(position)
        self.snake.append(cell)

    def add_cell(self):
        self.create_cell(self.snake[-1].position())

    def move(self):
        for cell in range(len(self.snake) - 1, 0, -1):  # in formate range(start, end, step)
            x_co = self.snake[cell - 1].xcor()
            y_co = self.snake[cell - 1].ycor()
            self.snake[cell].goto(x_co, y_co)
        self.snake[0].forward(move_speed)

    def up(self):
        if self.snake[0].heading() != down:
            self.snake[0].setheading(up)

    def down(self):
        if self.snake[0].heading() != up:
            self.snake[0].setheading(down)

    def right(self):
        if self.snake[0].heading() != left:
            self.snake[0].setheading(right)

    def left(self):
        if self.snake[0].heading() != right:
            self.snake[0].setheading(left)
