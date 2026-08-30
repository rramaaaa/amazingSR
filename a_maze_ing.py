import sys
import os
import random
from parsing import read_config, Check_Corners, Ckech_not_in_lock
from maze import MazeGenerator
from maze_printer import Maze_Printer, Maze_Printer_withPath
from fortytwo_lock import FortyTwo_Lock, FortyTwo_Check
from shortest_path import Finding_shortest_path
# from maze_analyzer import to_hexa, output


def menu(input_num: int,
         maze: list[list[MazeGenerator.Cell]],
         show_path: bool, entry: tuple[int, int],
         ext: tuple[int, int]
         ) -> None:

    if ent == 1:
        colors = ["\033[38;2;181;235;237m", "\033[38;2;245;230;168m"]

        os.system("clear")
        grid = obj.Create_Grid(rows, columns)
        grid = FortyTwo_Lock(grid, rows, columns)
        Ckech_not_in_lock(
            grid,
            int(entry_row), int(entry_column),
            int(exit_row), int(exit_column)
            )
        grid = obj.Generate_Maze(grid, perfect)
        grid = FortyTwo_Check(grid, rows, columns)
        Maze_Printer(grid, rows, columns, entry, ext, colors)
        print()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

        return grid

    elif ent == 2:
        os.system("clear")
        colors = ["\033[38;2;181;235;237m", "\033[38;2;245;230;168m"]

        if show_path:
            path, _ = Finding_shortest_path(maze, entry, ext)
            Maze_Printer_withPath(
                maze,
                rows, columns,
                entry, ext,
                colors, path)

        else:
            Maze_Printer(maze, rows, columns, entry, ext, colors)

        print()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

    elif ent == 3:
        os.system("clear")
        all_colors = [
            ["\033[38;2;243;182;210m", "\033[38;2;181;235;237m"],
            ["\033[38;2;197;179;230m", "\033[38;2;181;235;237m"],
            ["\033[38;2;154;255;155m", "\033[38;2;245;230;168m"],
            ["\033[38;2;181;235;237m", "\033[38;2;243;182;210m"],
            ["\033[38;2;85;191;194m", "\033[38;2;181;235;237m"],
            ["\033[38;2;141;216;232m", "\033[38;2;245;230;168m"],
            ["\033[38;2;243;182;210m", "\033[38;2;245;230;168m"]
        ]

        colors = random.choice(all_colors)
        if show_path:
            path, _ = Finding_shortest_path(maze, entry, ext)
            Maze_Printer_withPath(maze,
                                  rows, columns,
                                  entry, ext,
                                  colors, path)

        else:
            Maze_Printer(maze, rows, columns, entry, ext, colors)

        print()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

    elif ent == 4:
        exit()

    else:
        print("Please choice number (1-4)!")


try:
    file_name = sys.argv[1]
    config = read_config(file_name)
    columns = int(config["WIDTH"])
    rows = int(config["HEIGHT"])
    entry_row, entry_column = config["ENTRY"].split(",")
    exit_row, exit_column = config["EXIT"].split(",")
    perfect = config["PERFECT"]
    entry = (int(entry_row), int(entry_column))
    ext = (int(exit_row), int(exit_column))
    Check_Corners(rows, columns,
                  int(entry_row), int(entry_column),
                  int(exit_row), int(exit_column)
                  )

    if rows < 12 or columns < 10:
        print("Maze size is too small")
        obj = MazeGenerator()
        grid = obj.Create_Grid(rows, columns)
        grid = obj.Generate_Maze(grid, perfect)
        Maze_Printer(grid)

    elif rows > 50 or columns > 50:
        raise ValueError(
            "Maze size is too large!\n"
            "Please enter height and width values smaller than 50"
            )

    else:
        colors = ["\033[38;2;181;235;237m", "\033[38;2;245;230;168m"]

        obj = MazeGenerator()
        grid = obj.Create_Grid(rows, columns)
        grid = FortyTwo_Lock(grid, rows, columns)
        Ckech_not_in_lock(grid,
                          int(entry_row), int(entry_column),
                          int(exit_row), int(exit_column)
                          )
        grid = obj.Generate_Maze(grid, perfect)
        grid = FortyTwo_Check(grid, rows, columns)
        Maze_Printer(grid,
                     rows, columns,
                     entry, ext, colors)  # Light Cyan and Soft Yellow
        print()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

        path = False
        while True:
            try:
                ent = int(input("Choice? (1-4): "))
                if ent == 2:
                    if path:
                        path = False
                    else:
                        path = True
                if ent == 1:
                    grid = menu(ent, grid, path, entry, ext)
                else:
                    menu(ent, grid, path, entry, ext)

            except KeyboardInterrupt:
                raise KeyboardInterrupt("")


except KeyboardInterrupt:
    print("\nQuitting the program")
except Exception as e:
    print(e)


# res = output(grid)
# to_hexa(grid, res,
#        int(entry_row), int(entry_column),
#        int(exit_row), int(exit_column))
# print(file_name)
