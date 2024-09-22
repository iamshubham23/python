# from turtle import Turtle,Screen
# timmy_the_turtle= Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("NavyBlue")
#timmy_the_turtle.circle(20)
# timmy_the_turtle.forward(99)
# #timmy_the_turtle.right(90)

# for _ in range(4):
#timmy_the_turtle.forward(10)
#     timmy_the_turtle.right(90)

# for _ in range(0,15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# screen=Screen()
# screen.exitonclick() 

# import turtle as t
# tim=t.Turtle()

#draw a triangle,square,pentagon,hexagon,heptagon,octagon,nonagon,decagon
# from turtle import Turtle,Screen
# import random
# timm=Turtle()
# timm.shape("turtle")
# for _ in range(0,3):
#     timm.forward(110) 
#     timm.right(120)

# for _ in range(0,4):
#     timm.forward(110)
#     timm.right(90)

# for _ in range(0,5):
#     timm.forward(110)
#     timm.right(72) 

# for _ in range(0,6):
#     timm.forward(110)
#     timm.right(60)
# for _ in range(0,7):
#     timm.forward(110)
#     timm.right(51.4)    

# colours=["black","NavyBlue","IndianRed","SlateGray"]

# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         timm.forward(110)
#         timm.right(angle)

# for shape_side_n in range(3,10):
#     timm.color(random.choice(colours))
#     draw_shape(shape_side_n)        
# screen=Screen()
# screen.exitonclick()

#Draw a Random Walk
# import turtle as t
# import random
# walk=t.Turtle()
# walk.shape("turtle")
# directions=[0,90,180,270]
# t.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_color=(r,g,b)
#     return random_color 
# for _ in range(0,150):
#     walk.forward(30)
#     walk.setheading(random.choice(directions))
#     walk.color(random_color())
#     walk.pensize(15)
#     walk.speed("fastest")
        


#Make a Spirograph
# import turtle as t
# import random
# timm=t.Turtle()
# t.colormode(255)
# timm.shape("turtle")
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     color=(r,g,b)
#     return color
# timm.speed("fastest")
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timm.circle(100)
#         timm.setheading(timm.heading()+ size_of_gap)
#         timm.color(random_color())
        
# draw_spirograph(5)    
# screen=t.Screen()
# screen.exitonclick()

# import colorgram
# rgb_colors=[]
# colors=colorgram.extract('image.jpg',16)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_colors=(r,g,b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)


import turtle as turtle_module
import random
turtle_module.colormode(255)
import random
timm=turtle_module.Turtle()
colors_list=[(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47)]
timm.speed("fastest ")
timm.setheading(225)
timm.forward(300)
timm.setheading(0)
number_of_dots=100
for dot_count in range(1,number_of_dots+1):
    timm.dot(20,random.choice(colors_list))
    timm.forward(50)
    if dot_count %10==0:
        timm.setheading(90)    
        timm.forward(50)
        timm.setheading(180)
        timm.forward(500)
        timm.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()
