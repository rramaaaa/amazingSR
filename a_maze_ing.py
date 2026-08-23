import sys
from paths import read_config, Check_Corners
from maze import MazeGenerator
from maze_printer import Maze_Printer

#try:
file_name = sys.argv[1]
config = read_config(file_name)
print(config)
columns = int(config["WIDTH"])
rows = int(config["HEIGHT"])
#entry_row, entry_column = int(config["ENTRY"])
#exit_row, exit_column = int(config["EXIT"])
#Check_Corners(rows, columns, entry_row, entry_column, exit_row, exit_column)
obj = MazeGenerator()
grid = obj.Create_Grid(rows, columns)
obj.Generate_Maze(grid)
#obj.Imperfect_Maze(grid)
Maze_Printer(grid)

#except Exception as e:
#    print(e)

#print(file_name)