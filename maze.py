import time
import turtle
import sys


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Lefthandrule(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)

    def try_up(self, not_goal):
        x_cor = round(self.xcor(), 0)
        y_cor = round(self.ycor(), 0)
        if [x_cor, self.ycor()] in finish:
            return False
            # end_program()
        if(self.heading() == 90):
            if ([x_cor - 24, y_cor] in walls):
                if ([x_cor, y_cor+24] not in walls):
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
        if [x_cor, y_cor] in finish:
            return False
            # end_program()
        if(self.heading() == 270):
            if ([x_cor + 24, y_cor] in walls):
                if ([x_cor, y_cor-24] not in walls):
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
        if [self.xcor(), self.ycor()] in finish:
            return False
            # end_program()
        if(self.heading() == 0):
            if ([x_cor, y_cor+24] in walls):
                if ([x_cor + 24,  y_cor] not in walls):
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
        if [self.xcor(), self.ycor()] in finish:
            return False
            # end_program()
        if(self.heading() == 180):
            if ([x_cor, y_cor-24] in walls):
                if ([x_cor - 24, y_cor] not in walls):
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
        return True


class User(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def usr_up(self):
        if([self.xcor(), self.ycor()+24] not in walls):
            self.goto(self.xcor(), self.ycor()+24)
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")

    def usr_down(self):
        if([self.xcor(), self.ycor()-24] not in walls):
            self.goto(self.xcor(), self.ycor()-24)
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")

    def usr_left(self):
        if([self.xcor()-24, self.ycor()] not in walls):
            self.goto(self.xcor()-24, self.ycor())
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")

    def usr_right(self):
        if([self.xcor()+24, self.ycor()] not in walls):
            self.goto(self.xcor()+24, self.ycor())
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")


def build_maze(maze):
    for y in range(len(maze[0])):
        for x in range(len(maze)):
            ch = maze[y][x]

            x_cord = -348+(x*24)
            y_cord = 348-(y*24)

            if ch == "x":
                walls.append([x_cord, y_cord])
                wall.goto(x_cord, y_cord)
                wall.stamp()

            if ch == "O":
                goal.goto(x_cord, y_cord)
                goal.stamp()
                finish.append([x_cord, y_cord])
                walls.append([x_cord, y_cord-24])

            if ch == "U":
                user.goto(x_cord, y_cord)

            if ch == "L":
                lhr.goto(x_cord, y_cord)


def end_program():
    win.exitonclick()
    sys.exit()


# 30x30 maze
maze = ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "xULx         x               x",
        "x  x  xxxxx  x  xxxxx   x    x",
        "x  x  x   x  x  x   x   x    x",
        "x  xxxx   x  x  x   x   x    x",
        "x         x  x  x   x   x x  x",
        "x   xxxxxxx  x  x   x     x xx",
        "x               x   x        x",
        "x   x  xxxxx  xxx   xx       x",
        "x   x  x   x  x      xx   x  x",
        "x   x  x   x  x           x  x",
        "xxxxx  x   x  xxxx    x   x  x",
        "x      x              x   x  x",
        "x   xxxx   x  xxxxxxx x      x",
        "x          x  x  x       x   x",
        "x   xxxxxxxx  x  x  xxx  x   x",
        "x   x         x  x  x    xxxxx",
        "x   x  xxxxxxxx  xxxx   xx   x",
        "x  xx         x         x    x",
        "x  x    xxx   x         x    x",
        "x  x    x          xxxxxxxx  x",
        "xxxxxxxxxxxxxxx   xx      x  x",
        "x             x   x    x     x",
        "x             x   x    x  x  x",
        "x   xxxxx  x xx   x    x  x  x",
        "x   x   x  x  x   x    x  x  x",
        "x   x      x  x   x    x  x  x",
        "x   xxxxxxxxxxx   xxx  x  x  x",
        "x                      x  x  x",
        "xxxxxxxxxxxxxxxxxxxxxxxxOxxxxx"]

wall = Wall()
goal = Goal()
user = User()
lhr = Lefthandrule()
finish = []
walls = []
not_goal = True

win = turtle.Screen()
win.bgcolor("black")
win.title("Maze Game")
win.setup(800, 800)


build_maze(maze)
turtle.listen()
turtle.onkey(user.usr_up, 'Up')
turtle.onkey(user.usr_down, 'Down')
turtle.onkey(user.usr_left, 'Left')
turtle.onkey(user.usr_right, 'Right')

while True:
    if not_goal:
        not_goal = lhr.try_right(not_goal)
        not_goal = lhr.try_down(not_goal)
        not_goal = lhr.try_left(not_goal)
        not_goal = lhr.try_up(not_goal)
    win.update()


print("Left Hand Rule has reached goal")
