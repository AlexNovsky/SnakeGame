from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600) #Setting a screen size
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen() #adding listener to the screen
screen.onkey(snake.up, "Up") #UP key support
screen.onkey(snake.down, "Down") #DOWN key support
screen.onkey(snake.left, "Left") #LEFT key support
screen.onkey(snake.right, "Right") #RIGHT key support

game_is_on = True
while game_is_on:
    # Starting a game
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()
        snake.move()

    # Detecting collision with the tail
    for segment in snake.segments[1:]: #Slicing!
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10: #Collision detection
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
