from maze import MazeGenerator


def Create_block(grid: list[list[MazeGenerator.Cell]], row: int, column: int):
    for i in range(8):
        for j in range(8):
            if grid[row][column].Top:
                print(" ", end="")
            elif grid[row][column].Bottom:
                print(" ", end="")
            elif grid[row][column].Left:
                print(" ", end="")
            elif grid[row][column].Right:
                print(" ", end="")
            else:
                print("█",end="")
        print()
            


def Maze_Printer(grid: list[list[MazeGenerator.Cell]]):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            Create_block(grid, row, column)
        print()
    #return cell_walls

#so = MazeGenerator.Generate_Maze(MazeGenerator.Create_Grid(6, 6, 6))
#print(print_maze(so))

obj = MazeGenerator()
grid = obj.Create_Grid(20, 20)
obj.Generate_Maze(grid)
Maze_Printer(grid)
