import sys
from dijkstra import *


def lhr_solver(lhr, win):
    lhr.showturtle()
    not_goal = True
    goal_found = True
    while True:
        while goal_found:
            if not_goal:
                not_goal = lhr.try_right(not_goal)
                not_goal = lhr.try_down(not_goal)
                not_goal = lhr.try_left(not_goal)
                not_goal = lhr.try_up(not_goal)
            else:
                print("Left Hand Rule has reached goal")
                goal_found = False
        win.update()


def write_cost(cost, writer):
    writer.penup()
    writer.goto(-24 * 15, 25 * 15)
    writer.write("Shortest path cost: " + str(cost), font=("ariel", 20, "bold"), align="left")


def end_program(win):
    win.exitonclick()
    sys.exit()
