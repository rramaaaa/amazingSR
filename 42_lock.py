from maze import MazeGenerator

def FortyTwo(grid: list[list[MazeGenerator.Cell]], rows: int, columns: int):
    Mid_Row: int = rows/2
    Mid_Column: int = columns/2
    grid[Mid_Row][Mid_Column].Bottom = True
    grid[Mid_Row][Mid_Column].Right = True
    grid[Mid_Row][Mid_Column].Left = True
    grid[Mid_Row][Mid_Column].Top = True

    for column in range(3):
        print()



obj = MazeGenerator