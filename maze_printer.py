from maze import MazeGenerator
import random

def Maze_Printer(grid: list[list["MazeGenerator.Cell"]], rows: int, columns: int, colors: list[str], path: list[tuple[int, int]] = None) -> None:


    #colors = ["\033[38;2;154;255;155m", "\033[38;2;181;235;237m", "\033[38;2;143;217;196m", "\033[38;2;169;180;210m"]
    #color_42 = ["\033[38;2;180;167;245m", "\033[38;2;244;168;150m", "\033[38;2;243;182;210m", "\033[38;2;245;230;168m"]

    walls_color = colors[0]
    forty_color = colors[1]

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
                    print( walls_color + "   █", end="")
        print(walls_color + "█")

    for i in range(columns):
        print(walls_color + "████", end="")
    print(walls_color + "██")