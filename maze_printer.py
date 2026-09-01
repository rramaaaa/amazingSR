from maze import MazeGenerator


def Maze_Printer(
        grid: list[list["MazeGenerator.Cell"]],
        rows: int, columns: int, entry: tuple[int, int],
        ext: tuple[int, int], colors: list[str]
        ) -> None:

    '''Print maze without path'''

    walls_color = colors[0]
    forty_color = colors[1]
    entry_color = "\033[38;2;255;255;255m"
    exit_color = "\033[38;2;255;255;255m"

    for i in range(columns):
        print(walls_color + "████", end="")
    print(walls_color + "██")

    rows_num = rows * 2
    for row in range(1, rows_num):
        i = (row - 1) // 2
        print(walls_color + "█", end="")
        for column in range(columns):
            if row % 2 != 0:
                if grid[i][column].Lock:
                    print(forty_color + "████", end="")
                elif (i, column) == entry:
                    if grid[i][column].Right:
                        print(entry_color + " 🕷 " + walls_color + "█", end="")
                    else:
                        print(entry_color + " 🕷  ", end="")

                elif (i, column) == ext:
                    if grid[i][column].Right:
                        print(exit_color + " 🕸 " + walls_color + "█", end="")
                    else:
                        print(exit_color + " 🕸  ", end="")

                elif grid[i][column].Right:
                    print(walls_color + "   █", end="")
                else:
                    print("    ", end="")
            else:
                if grid[i][column].Lock:
                    color = forty_color
                else:
                    color = walls_color
                if grid[i][column].Bottom:
                    print(color + "████", end="")
                else:
                    print(walls_color + "   █", end="")
        print(walls_color + "█")

    for i in range(columns):
        print(walls_color + "████", end="")
    print(walls_color + "██")


def Maze_Printer_withPath(grid: list[list[MazeGenerator.Cell]],
                          rows: int, columns: int,
                          entry: tuple[int, int],
                          ext: tuple[int, int],
                          colors: list[str],
                          path: list[tuple[int, int]]
                          ) -> None:

    '''Print Maze with path'''

    wall_color = colors[0]
    forty_color = colors[1]
    path_color = "\033[38;2;255;255;255m"
    entry_color = "\033[38;2;255;255;255m"
    exit_color = "\033[38;2;255;255;255m"

    for i in range(columns):
        print(wall_color + "████", end="")
    print(wall_color + "██")

    rows_num = rows * 2
    for row in range(1, rows_num):
        i = (row - 1) // 2
        print(wall_color + "█", end="")
        for column in range(columns):
            if row % 2 != 0:
                if grid[i][column].Lock:
                    print(forty_color + "████", end="")
                elif (i, column) == entry:
                    if grid[i][column].Right:
                        print(entry_color + " 🕷 " + wall_color + "█", end="")
                    else:
                        print(entry_color + " 🕷  ", end="")

                elif (i, column) == ext:
                    if grid[i][column].Right:
                        print(exit_color + " 🕸 " + wall_color + "█", end="")
                    else:
                        print(exit_color + " 🕸  ", end="")

                elif (i, column) in path:
                    if grid[i][column].Right:
                        print(path_color + " ▫ " + wall_color + "█", end="")
                    else:
                        print(path_color + " ▫  ", end="")

                elif grid[i][column].Right:
                    print(wall_color + "   █", end="")
                else:
                    print("    ", end="")

            else:
                if grid[i][column].Lock:
                    color = forty_color
                else:
                    color = wall_color

                if grid[i][column].Bottom:
                    print(color + "████", end="")
                else:
                    print(wall_color + "   █", end="")
        print(wall_color + "█")

    for column in range(columns):
        print(wall_color + "████", end="")
    print(wall_color + "██")
