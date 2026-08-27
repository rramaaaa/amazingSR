from maze import MazeGenerator

def Maze_Printer(grid: list[list["MazeGenerator.Cell"]], rows: int, columns: int, path: list[tuple[int, int]] = None) -> None:

    for i in range(columns):
        print("████", end="")
    print("██")

    rows_num = rows * 2 + 1
    for row in range(1, rows_num):
        i = (row - 1) // 2
        print("█", end="")
        for column in range(columns):
            if row % 2 != 0:
                if grid[i][column].Lock:
                    print("████", end="")
                elif grid[i][column].Right:
                    print("   █", end="")
                else:
                    print("    ", end="")
            else:
                if grid[i][column].Bottom:
                    print("████", end="")
                else:
                    print("   █", end="")
        print("█")