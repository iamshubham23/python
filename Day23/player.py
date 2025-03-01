from turtle import Turtle
STARTING_POSITION=(0,-280)
FINISH_LINE_Y=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def go_up(self):
        new_y=self.ycor() + 15
        self.goto(self.xcor(),new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)    

    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True    
        else:
            False