import random
from colorama import init, Fore


def maze_gen(width, height):
    # global variables
    wall = "x"
    cell = " "
    u = "u"
    start = "U"
    goal = "O"

    def init_maze(width: int, height: int):
        maze = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(u)
            maze.append(row)
        return maze

    # init colorama
    init()

    def print_maze(maze):
        for i in range(0, len(maze)):
            for j in range(0, len(maze[0])):
                if maze[i][j] == u:
                    print(Fore.WHITE, f"{maze[i][j]}", end="")
                elif maze[i][j] == cell:
                    print(Fore.GREEN, f"{maze[i][j]}", end="")
                else:
                    print(Fore.RED, f"{maze[i][j]}", end="")
            print("\n")

    def num_of_cells_around(coord, maze):
        num_cell = 0
        y, x = coord[0], coord[1]
        if maze[y - 1][x] == cell:
            num_cell += 1
        if maze[y + 1][x] == cell:
            num_cell += 1
        if maze[y][x - 1] == cell:
            num_cell += 1
        if maze[y][x + 1] == cell:
            num_cell += 1
        return num_cell

    maze = init_maze(width, height)
    # print_maze(maze)

    start_x = int(random.random() * width)
    start_y = int(random.random() * height)

    # So the starting point is not at edge of maze
    while start_x == 0 or start_x == width - 1:
        start_x = int(random.random() * width)
    while start_y == 0 or start_y == height - 1:
        start_y = int(random.random() * height)

    maze[start_y][start_x] = cell
    walls = []
    walls.append((start_y, start_x - 1))
    walls.append((start_y - 1, start_x))
    walls.append((start_y + 1, start_x))
    walls.append((start_y, start_x + 1))

    maze[start_y][start_x - 1] = wall
    maze[start_y - 1][start_x] = wall
    maze[start_y + 1][start_x] = wall
    maze[start_y][start_x + 1] = wall

    def add_wall_top(y, x):
        if y != 0:
            if maze[y - 1][x] != cell:
                maze[y - 1][x] = wall
            if (y - 1, x) not in walls:
                walls.append((y - 1, x))

    def add_wall_bot(y, x):
        if y != height - 1:
            if maze[y + 1][x] != cell:
                maze[y + 1][x] = wall
            if (y + 1, x) not in walls:
                walls.append((y + 1, x))

    def add_wall_right(y, x):
        if x != width - 1:
            if maze[y][x + 1] != cell:
                maze[y][x + 1] = wall
            if (y, x + 1) not in walls:
                walls.append((y, x + 1))

    def add_wall_left(y, x):
        if x != 0:
            if maze[y][x - 1] != cell:
                maze[y][x - 1] = wall
            if (y, x - 1) not in walls:
                walls.append((y, x - 1))

    while walls:
        rand_wall = walls[int(random.random() * len(walls)) - 1]
        y, x = rand_wall[0], rand_wall[1]
        # left wall
        if x != 0 and x != width - 1:
            if maze[y][x + 1] == cell and maze[y][x - 1] == u:
                if num_of_cells_around(rand_wall, maze) < 2:
                    # Make wall into cell
                    maze[y][x] = cell
                    # From that wall - make surrounded, unvisited cells into new walls
                    add_wall_top(y, x)
                    add_wall_bot(y, x)
                    add_wall_left(y, x)
                walls.remove((y, x))
                continue

            # right wall
            if maze[y][x - 1] == cell and maze[y][x + 1] == u:
                if num_of_cells_around(rand_wall, maze) < 2:
                    # Make wall into cell
                    maze[y][x] = cell
                    # From that wall - make surrounded, unvisited cells into new walls
                    add_wall_top(y, x)
                    add_wall_bot(y, x)
                    add_wall_right(y, x)
                walls.remove((y, x))
                continue

        # top wall
        if y != 0 and y != height - 1:
            if maze[y - 1][x] == u and maze[y + 1][x] == cell:
                if num_of_cells_around(rand_wall, maze) < 2:
                    # Make wall into cell
                    maze[y][x] = cell
                    # From that wall - make surrounded, unvisited cells into new walls
                    add_wall_top(y, x)
                    add_wall_left(y, x)
                    add_wall_right(y, x)
                walls.remove((y, x))
                continue

            # bot wall
            if maze[y + 1][x] == u and maze[y - 1][x] == cell:
                if num_of_cells_around(rand_wall, maze) < 2:
                    # Make wall into cell
                    maze[y][x] = cell
                    # From that wall - make surrounded, unvisited cells into new walls
                    add_wall_bot(y, x)
                    add_wall_left(y, x)
                    add_wall_right(y, x)
                walls.remove((y, x))
                continue

        walls.remove((y, x))

    # Mark unvisited cells as wall
    for i in range(0, height):
        for j in range(0, width):
            if maze[i][j] == u:
                maze[i][j] = wall

    # Set entrance and exit
    for i in range(0, width):
        if maze[1][i] == cell:
            maze[1][i] = start
            beginning = (1, i)
            break

    for i in range(width - 1, 0, -1):
        if maze[height - 2][i] == cell:
            maze[height - 1][i] = goal
            end = (height - 1, i)
            break

    return maze, beginning, end
