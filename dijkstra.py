from collections import OrderedDict
import time


def dijkstra(maze, beginning, end):
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

        # end reached
        if curr_cell == end:
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
    cost = visited[end]
    while end != beginning:
        fwd_path[rev_path[end]] = end
        end = rev_path[end]
    fwd_path = OrderedDict(reversed(list(fwd_path.items())))
    return rev_path, fwd_path, cost


def update_path(maze, path, mapping, visited, solution, end):
    for y, x in mapping:
        if maze[y][x] == "x" or (y, x) == end:
            continue
        else:
            x_cord = -348 + (x * 24)
            y_cord = 348 - (y * 24)
            visited.goto(x_cord, y_cord)
            visited.stamp()

    for y, x in path:
        x_cord = -348 + (x * 24)
        y_cord = 348 - (y * 24)
        solution.goto(x_cord, y_cord)
        solution.stamp()
