import time
import turtle
import sys
import keyboard
from collections import OrderedDict


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Path(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


class Visited(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("orange")
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
        if self.heading() == 90:
            if [x_cor - 24, y_cor] in walls:
                if [x_cor, y_cor + 24] not in walls:
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
        if self.heading() == 270:
            if [x_cor + 24, y_cor] in walls:
                if [x_cor, y_cor - 24] not in walls:
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
        if self.heading() == 0:
            if [x_cor, y_cor + 24] in walls:
                if [x_cor + 24, y_cor] not in walls:
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
        if self.heading() == 180:
            if [x_cor, y_cor - 24] in walls:
                if [x_cor - 24, y_cor] not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
        return True


def dijkstra():
    unvisited = {}
    for y in range(len(maze[0])):
        for x in range(len(maze)):
            unvisited[(x, y)] = float("inf")
            unvisited[(1, 1)] = 0
    visited = {}
    rev_path = {}
    while unvisited:
        curr_cell = min(unvisited, key=unvisited.get)
        x, y = curr_cell[0], curr_cell[1]
        visited[curr_cell] = unvisited[curr_cell]

        # goal reached
        if curr_cell == (29, 24):
            break
        for direction in "NESW":
            if maze[x][y] != "x":
                if direction == "N":
                    child_cell = (x - 1, y)
                elif direction == "E":
                    child_cell = (x, y + 1)
                elif direction == "S":
                    child_cell = (x + 1, y)
                elif direction == "W":
                    child_cell = (x, y - 1)
                if child_cell in visited:
                    continue
                temp_dist = unvisited[curr_cell] + 1
                if temp_dist < unvisited[child_cell]:
                    unvisited[child_cell] = temp_dist
                    rev_path[child_cell] = curr_cell
        unvisited.pop(curr_cell)
    fwd_path = {}
    goal = (29, 24)
    while goal != (1, 1):
        fwd_path[rev_path[goal]] = goal
        goal = rev_path[goal]
    fwd_path = OrderedDict(reversed(list(fwd_path.items())))
    return rev_path, fwd_path, visited[(29, 24)]


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


def build_maze(maze):
    for y in range(len(maze[0])):
        for x in range(len(maze)):
            ch = maze[y][x]

            x_cord = -348 + (x * 24)
            y_cord = 348 - (y * 24)

            if ch == "x":
                walls.append([x_cord, y_cord])
                wall.goto(x_cord, y_cord)
                wall.stamp()

            elif ch == "O":
                goal.goto(x_cord, y_cord)
                goal.stamp()
                finish.append([x_cord, y_cord])
                walls.append([x_cord, y_cord - 24])

            elif ch == "U":
                user.goto(x_cord, y_cord)

            elif ch == "L":
                lhr.goto(x_cord, y_cord)


def update_path(maze, path, mapping):
    for y, x in mapping:
        if maze[y][x] == "x":
            continue
        else:
            x_cord = -348 + (x * 24)
            y_cord = 348 - (y * 24)
            visited.goto(x_cord, y_cord)
            visited.stamp()
            time.sleep(0.1)

    for y, x in path:
        x_cord = -348 + (x * 24)
        y_cord = 348 - (y * 24)
        solution.goto(x_cord, y_cord)
        solution.stamp()
        time.sleep(0.1)


def end_program():
    win.exitonclick()
    sys.exit()


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

wall = Wall()
goal = Goal()
user = User()
visited = Visited()
lhr = Lefthandrule()
finish = []
walls = []
solution = Path()


win = turtle.Screen()
win.bgcolor("black")
win.title("Maze Game")
win.setup(800, 800)

build_maze(maze)
rev, path, cost = dijkstra()
# for x, y in path:
#     maze[x][y] = "v"


turtle.listen()
turtle.onkey(user.usr_up, "Up")
turtle.onkey(user.usr_down, "Down")
turtle.onkey(user.usr_left, "Left")
turtle.onkey(user.usr_right, "Right")

update_path(maze, path, rev)

# def lhr_solver():
#     not_goal = True
#     goal_found = True
#     while True:
#         while goal_found:
#             if not_goal:
#                 not_goal = lhr.try_right(not_goal)
#                 not_goal = lhr.try_down(not_goal)
#                 not_goal = lhr.try_left(not_goal)
#                 not_goal = lhr.try_up(not_goal)
#             else:
#                 print("Left Hand Rule has reached goal")
#                 goal_found = False
#         if keyboard.is_pressed("r"):
#             return
#         win.update()

# lhr_solver()


while True:
    win.update()
# print(unvisited)


print(path)
# print(deez)
