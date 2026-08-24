import sys
from paths import read_config, Check_Corners
from maze import MazeGenerator
from maze_printer import Maze_Printer
from fortytwo_lock import FortyTwo

try:
    file_name = sys.argv[1]
    config = read_config(file_name)
    columns = int(config["WIDTH"])
    rows = int(config["HEIGHT"])
    entry_row, entry_column = config["ENTRY"].split(",")
    exit_row, exit_column = config["EXIT"].split(",")
    perfect = config["PERFECT"]
    Check_Corners(rows, columns, int(entry_row), int(entry_column), int(exit_row), int(exit_column))
    obj = MazeGenerator()
    grid = obj.Create_Grid(rows, columns)
    grid = obj.Generate_Maze(grid, perfect)
    #obj.Imperfect_Maze(grid)
    grid = FortyTwo(grid, rows, columns)
    Maze_Printer(grid)

except Exception as e:
    print(e)

#print(file_name)
