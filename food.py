from turtle import Turtle
import random

food_colors = ["red","orange","yellow","green","blue","purple"]
food_shapes = ["square","turtle","circle","triangle"]

class Food(Turtle):
    def __init__(self):
        super().__init__() # inherits from the Turtle class
        self.shape(random.choice(food_shapes))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(food_colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """New Food location"""
        self.color(random.choice(food_colors))
        self.shape(random.choice(food_shapes))
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)