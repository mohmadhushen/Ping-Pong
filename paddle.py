from turtle import Turtle , Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
       
        self.shape("square")
        self.color("white")
        #turle size starts from 20 by 20 ..so now the peddle size reuired is 20 by 100 so it should 1/5
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
