# Day 20 and 21 Snake Game

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

FOOD_COUNT = 6

"""Screen setup"""
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Timmy Snake Game")
screen.tracer(0)

"""Initial 3 segments of snake named Timmy"""
timmy = Snake()
scoreboard = Scoreboard()
food_list = []
for i in range(FOOD_COUNT):
    new_food = Food()
    food_list.append(new_food)

"""Snake Movement"""
screen.listen()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")
screen.onkey(timmy.left, "Left")
screen.onkey(timmy.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    timmy.move()

    """Detect collision with food"""
    for food in food_list:
        if timmy.head.distance(food) < 15:
            scoreboard.increase_score()
            timmy.extend()
            if food.shape() == "turtle":
                screen.update()
                scoreboard.increase_score() 
            food.refresh()

    """Detect collision with wall"""
    if timmy.head.xcor()>290 or timmy.head.xcor()<-290 or timmy.head.ycor()>290 or timmy.head.ycor()<-290:
        game_is_on = False
        scoreboard.game_over()

    """Detect collision with tail"""
    for segment in timmy.segments[1:]:
        if timmy.head.distance(segment)<5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()