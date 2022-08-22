import turtle
from LHR import Lefthandrule
from dijkstra import *
from tkinter import *
from util import *

"""
Wall object of shape square and color white
Forbids the algo from going there
"""


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


"""
Path object of shape square and color yellow
Displays shortest path from start to goal
"""


class Path(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


"""
Visited object of shape square and color orange
Shows cells that have been visited
"""


class Visited(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("orange")
        self.penup()
        self.speed(0)


"""
Goal object of shape square and color green
"""


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


"""
User object of shape square and color blue
User controlled object to traverse the maze
"""


class User(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def usr_up(self):
        if [self.xcor(), self.ycor() + 24] not in walls:
            self.goto(self.xcor(), self.ycor() + 24)
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")

    def usr_down(self):
        if [self.xcor(), self.ycor() - 24] not in walls:
            self.goto(self.xcor(), self.ycor() - 24)
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")

    def usr_left(self):
        if [self.xcor() - 24, self.ycor()] not in walls:
            self.goto(self.xcor() - 24, self.ycor())
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")

    def usr_right(self):
        if [self.xcor() + 24, self.ycor()] not in walls:
            self.goto(self.xcor() + 24, self.ycor())
            if [self.xcor(), self.ycor()] in finish:
                print("Player has reached goal")


# Initializes and builds maze based on a string file with the indivual letter representing different objects
def build_maze(maze):
    for y in range(len(maze[0])):
        for x in range(len(maze)):
            ch = maze[y][x]

            x_cord = -348 + (x * 24)
            y_cord = 348 - (y * 24)

            # 'x' stands for walls
            if ch == "x":
                walls.append([x_cord, y_cord])
                wall.goto(x_cord, y_cord)
                wall.stamp()

            # 'O' stands for goal
            elif ch == "O":
                goal.goto(x_cord, y_cord)
                finish.append([x_cord, y_cord])
                walls.append([x_cord, y_cord - 24])
                goal.stamp()

            # 'U' stands for user
            elif ch == "U":
                user.goto(x_cord, y_cord)

            # 'L' stands for the left hand rule pointer
            elif ch == "L":
                lhr.goto(x_cord, y_cord)


# Runner method for dijkstra algo
def run_dijkstra(maze):
    visited = Visited()
    solution = Path()
    rev, path, cost = dijkstra(maze)
    update_path(maze, path, rev, visited, solution)
    build_maze(maze)


# 30x30 maze
maze = [
    list("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    list("xULx         x               x"),
    list("x  x  xxxxx  x  xxxxx   x    x"),
    list("x  x  x   x  x  x   x   x    x"),
    list("x  xxxx   x  x  x   x   x    x"),
    list("x         x  x  x   x   x x  x"),
    list("x   xxxxxxx  x  x   x     x xx"),
    list("x               x   x        x"),
    list("x   x  xxxxx  xxx   xx       x"),
    list("x   x  x   x  x      xx   x  x"),
    list("x   x  x   x  x           x  x"),
    list("xxxxx  x   x  xxxx    x   x  x"),
    list("x      x              x   x  x"),
    list("x   xxxx   x  xxxxxxx x      x"),
    list("x          x  x  x       x   x"),
    list("x   xxxxxxxx  x  x  xxx  x   x"),
    list("x   x         x  x  x    xxxxx"),
    list("x   x  xxxxxxxx  xxxx   xx   x"),
    list("x  xx         x         x    x"),
    list("x  x    xxx   x         x    x"),
    list("x  x    x          xxxxxxxx  x"),
    list("xxxxxxxxxxxxxxx   xx      x  x"),
    list("x             x   x    x     x"),
    list("x             x   x    x  x  x"),
    list("x   xxxxx  x xx   x    x  x  x"),
    list("x   x   x  x  x   x    x  x  x"),
    list("x   x      x  x   x    x  x  x"),
    list("x   xxxxxxxxxxx   xxx  x  x  x"),
    list("x                      x  x  x"),
    list("xxxxxxxxxxxxxxxxxxxxxxxxOxxxxx"),
]

# initialize classes and vars
wall = Wall()
goal = Goal()
user = User()
finish = []
walls = []
need_lhr = False
lhr = Lefthandrule(finish, walls)

# Initialize window
win = turtle.Screen()
win.bgcolor("black")
win.title("Maze Game")
win.setup(800, 900)
canvas = win.getcanvas()

# Buttons to run dijkstra and lhr
button_dijkstra = Button(canvas.master, text="Dijkstra", font="ariel", command=lambda: run_dijkstra(maze))
button_dijkstra.place(x=40, y=850)
button_lhr = Button(canvas.master, text="Left Hand Rule", font="ariel", command=lambda: lhr_solver(lhr, win))
button_lhr.place(x=120, y=850)


build_maze(maze)

# User controls
turtle.listen()
turtle.onkey(user.usr_up, "Up")
turtle.onkey(user.usr_down, "Down")
turtle.onkey(user.usr_left, "Left")
turtle.onkey(user.usr_right, "Right")


while True:
    win.update()
