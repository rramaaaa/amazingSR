from maze import MazeGenerator

def Maze_Printer(grid: list[list[MazeGenerator.Cell]]) -> None:

    PINK = "\033[95m"
    RESET = "\033[0m"

    rows = len(grid)
    columns = len(grid[0])

    print(PINK + "┌" + RESET, end="")

    for cell in grid[0]:
        print("────", end="")

    print()

    for i in range(rows):

        print("│", end="")

        for j in range(columns):

            cell = grid[i][j]

            print("   ", end="")

            if cell.Right:
                print("│", end="")
            else:
                print(" ", end="")

        print()

        print("│", end="")

        for j in range(columns):

            cell = grid[i][j]

            if cell.Bottom:
                print("────", end="")
            else:
                print("   │", end="")

        print()

obj = MazeGenerator()
grid = obj.Create_Grid(20, 20)
obj.Generate_Maze(grid)
Maze_Printer(grid)