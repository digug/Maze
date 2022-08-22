import turtle
import keyboard


class Lefthandrule(turtle.Turtle):
    def __init__(self, finish, walls):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)
        self.finish = finish
        self.walls = walls

    def try_up(self, not_goal):
        x_cor = round(self.xcor(), 0)
        y_cor = round(self.ycor(), 0)
        if [x_cor, self.ycor()] in self.finish:
            return False
            # end_program()
        if self.heading() == 90:
            if [x_cor - 24, y_cor] in self.walls:
                if [x_cor, y_cor + 24] not in self.walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
        return True

    def try_down(self, not_goal):
        x_cor = round(self.xcor(), 0)
        y_cor = round(self.ycor(), 0)
        if [x_cor, y_cor] in self.finish:
            return False
            # end_program()
        if self.heading() == 270:
            if [x_cor + 24, y_cor] in self.walls:
                if [x_cor, y_cor - 24] not in self.walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
        return True

    def try_left(self, not_goal):
        x_cor = round(self.xcor(), 0)
        y_cor = round(self.ycor(), 0)
        if [self.xcor(), self.ycor()] in self.finish:
            return False
            # end_program()
        if self.heading() == 0:
            if [x_cor, y_cor + 24] in self.walls:
                if [x_cor + 24, y_cor] not in self.walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
        return True

    def try_right(self, not_goal):
        x_cor = round(self.xcor(), 0)
        y_cor = round(self.ycor(), 0)
        if [self.xcor(), self.ycor()] in self.finish:
            return False
            # end_program()
        if self.heading() == 180:
            if [x_cor, y_cor - 24] in self.walls:
                if [x_cor - 24, y_cor] not in self.walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
        return True
