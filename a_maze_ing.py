import sys
import os
from parsing import read_config, Check_Corners, Ckech_not_in_lock
from maze import MazeGenerator
from maze_printer import Maze_Printer
from fortytwo_lock import FortyTwo_Lock, FortyTwo_Check
from maze_analyzer import to_hexa, output


def menu(input_num: int):
    if ent == 1:
        os.system("clear")
        grid = obj.Create_Grid(rows, columns)
        grid = FortyTwo_Lock(grid, rows, columns)
        Ckech_not_in_lock(grid, int(entry_row), int(entry_column), int(exit_row), int(exit_column))
        grid = obj.Generate_Maze(grid, perfect)
        grid = FortyTwo_Check(grid, rows, columns)
        Maze_Printer(grid, rows, columns)
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
    Check_Corners(rows, columns, int(entry_row), int(entry_column), int(exit_row), int(exit_column))

    if rows < 12 or columns < 10:
        print("Maze size is too small")
        obj = MazeGenerator()
        grid = obj.Create_Grid(rows, columns)
        grid = obj.Generate_Maze(grid, perfect)
        Maze_Printer(grid)

    elif rows > 50 or columns > 50:
        raise ValueError("Maze size is too large!\nPlease enter height and width values smaller than 50")

    else:
        obj = MazeGenerator()
        grid = obj.Create_Grid(rows, columns)
        grid = FortyTwo_Lock(grid, rows, columns)
        Ckech_not_in_lock(grid, int(entry_row), int(entry_column), int(exit_row), int(exit_column))
        grid = obj.Generate_Maze(grid, perfect)
        grid = FortyTwo_Check(grid, rows, columns)
        Maze_Printer(grid, rows, columns)
        print()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

        while True:
            try:
                ent = int(input("Choice? (1-4): "))
                menu(ent)


            except KeyboardInterrupt as e:
                raise KeyboardInterrupt("\n")


except KeyboardInterrupt :
    print("\nQuitting the program")
except Exception as e:
        print(e)

#print(file_name)
