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
screen=Screen()
screen.setup(500,400)
is_race_on=True
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race ? enter a color:")
y_position=[-150,-100,-50,0,50,100]
colors=["red","skyblue","yellow","green","blue","purple"]
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-240,y_position[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>240:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print(f"you have won ! the {winning_color} turtle is winner")
            else:
                print(f"you have lost ! the {winning_color} turtle is winner")

            rand_distance=random.randint(0,10)
            turtle.forward(rand_distance)


screen.exitonclick()

