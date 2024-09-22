# from turtle import Turtle,Screen
# tim=Turtle()
# screen=Screen()

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space",fun=move_forwards)
# screen.exitonclick() 

# from turtle import Turtle,Screen
# tim=Turtle()
# screen=Screen()

# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)    
# def turn_left():
#     new_heading=tim.heading()+10
#     tim.setheading(new_heading)
# def turn_right():
#     new_heading=tim.heading()-10
#     tim.setheading(new_heading)   

# def clear():
#     tim.clear() 
#     tim.penup
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(key="w",fun=move_forwards)
# screen.onkey(key="s",fun=move_backwards)
# screen.onkey(key="l",fun=turn_left)
# screen.onkey(key="r",fun=turn_right)
# screen.onkey(clear,"c")
# screen.exitonclick()

#Build a turtle Race
from turtle import Turtle,Screen
import random
timmy=Turtle(shape="turtle")
tommy=Turtle(shape="turtle")
tonny=Turtle(shape="turtle")
timm=Turtle(shape="turtle")
tim=Turtle(shape="turtle")
ton=Turtle(shape="turtle")
timmy.penup()
tommy.penup()
tonny.penup()
timm.penup()
tim.penup()
ton.penup()
screen=Screen()
screen.setup(500,400)
#user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race ? enter a color:")
timmy.goto(-240,-180)
tommy.goto(-240,-150)
tonny.goto(-240,-120)
timm.goto(-240,-90)
tim.goto(-240,-60)
ton.goto(-240,-30)

timmy.color("red")
tommy.color("orange")
tonny.color("SkyBlue")
timm.color("Brown")
tim.color("SlateGray")
ton.color("black")


screen.exitonclick()