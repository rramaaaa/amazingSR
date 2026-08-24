from maze import MazeGenerator


def FortyTwo(grid: list[list[MazeGenerator.Cell]], rows: int, columns: int) -> list[tuple[int, int]]:
    i: int = rows // 2
    j: int = columns // 2

    grid[i][j - 1].Top = True
    grid[i - 1][j - 1].Bottom = True
    grid[i][j - 1].Bottom = True
    grid[i + 1][j - 1].Top = True
    grid[i][j - 1].Left = True
    grid[i][j - 2].Right = True
    grid[i][j - 1].Right = True
    grid[i][j].Left = True

    grid[i][j - 2].Top = True
    grid[i - 1][j - 2].Bottom = True
    grid[i][j - 2].Bottom = True
    grid[i + 1][j - 2].Top = True
    grid[i][j - 2].Right = True
    grid[i][j - 3].Left = True
    grid[i][j - 2].Left = True
    grid[i][j - 1].Right = True


    grid[i][j - 3].Top = True
    grid[i - 1][j - 3].Bottom = True
    grid[i][j - 3].Bottom = True
    grid[i - 1][j - 3].Top = True
    grid[i][j - 3].Right = True
    grid[i][j - 2].Left = True
    grid[i][j - 3].Left = True
    grid[i][j - 4].Right = True


    grid[i - 1][j - 3].Top = True
    grid[i - 2][j - 3].Bottom = True
    grid[i - 1][j - 3].Bottom = True
    grid[i][j - 3].Top = True
    grid[i - 1][j - 3].Right = True
    grid[i - 1][j - 2].Left = True
    grid[i - 1][j - 3].Left = True
    grid[i - 1][j - 4].Right = True

    grid[i - 2][j - 3].Top = True
    grid[i - 3][j - 3].Bottom = True
    grid[i - 2][j - 3].Bottom = True
    grid[i - 1][j - 3].Top = True
    grid[i - 2][j - 3].Left = True
    grid[i - 2][j - 4].Right = True
    grid[i - 2][j - 3].Right = True
    grid[i - 2][j - 2].Left = True


    grid[i + 1][j -1].Top = True
    grid[i + 1][j -1].Bottom = True
    grid[i + 1][j -1].Right = True
    grid[i + 1][j -1].Left = True 

    grid[i + 2][j- 1].Top = True 
    grid[i + 2][j- 1].Bottom = True
    grid[i + 2][j- 1].Left = True
    grid[i + 2][j- 1].Right = True 

    grid[i][j + 1].Top = True
    grid[i][j + 1].Bottom = True 
    grid[i][j + 1].Left = True
    grid[i][j + 1].Right = True

    grid[i][j + 2].Top = True
    grid[i][j + 2].Bottom = True 
    grid[i][j + 2].Right = True 
    grid[i][j + 2].Left = True

    grid[i][j + 3].Top = True
    grid[i][j + 3].Bottom = True
    grid[i][j + 3].Left = True
    grid[i][j + 3].Right = True

    grid[i - 1][j + 3].Top = True
    grid[i - 1][j + 3].Bottom = True
    grid[i - 1][j + 3].Right = True
    grid[i - 1][j + 3].Left = True

    grid[i - 2][j + 3].Top = True
    grid[i - 2][j + 3].Bottom = True
    grid[i - 2][j + 3].Left = True
    grid[i - 2][j + 3].Right = True


    grid[i - 2][j + 2].Top = True
    grid[i - 2][j + 2].Bottom = True
    grid[i - 2][j + 2].Left = True
    grid[i - 2][j + 2].Right = True

    grid[i - 2][j + 1].Top = True
    grid[i - 2][j + 1].Bottom = True
    grid[i - 2][j + 1].Right = True 
    grid[i - 2][j + 1].Left = True

    grid[i + 1][j + 1].Top = True
    grid[i + 1][j + 1].Bottom = True
    grid[i + 1][j + 1].Right = True
    grid[i + 1][j + 1].Left = True

    grid[i + 2][j + 1].Top = True
    grid[i + 2][j + 1].Bottom = True
    grid[i + 2][j + 1].Right = True
    grid[i + 2][j + 1].Left = True

    
    grid[i + 2][j + 2].Top = True
    grid[i + 2][j + 2].Bottom = True
    grid[i + 2][j + 2].Right = True
    grid[i + 2][j + 2].Left = True

    grid[i + 2][j + 3].Top = True
    grid[i + 2][j + 3].Bottom = True
    grid[i + 2][j + 3].Right = True
    grid[i + 2][j + 3].Left = True


    return grid
