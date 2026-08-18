from collections.abc import Callable
import random

class Cell:
    def __init__(self, row: int, column: int, maxrow: int, maxcolumn: int) -> None:
        self.Top: bool = True
        self.Bottom: bool = True
        self.Right: bool = True
        self.Left: bool = True
        self.Row: int = row
        self.Column: int = column
        self.MaxRow: int = maxrow
        self.MaxColumn: int = maxcolumn

def Create_Grid(rows: int, columns: int) -> list[list: Callable]:
    grid: list = list()
    for i in range(rows):
        cell: list = []
        grid.append(cell)
        for j in range(columns):
            cell.append(Cell(i, j, rows - 1, columns - 1))
            #print(grid[i][j].Row, grid[i][j].Column)
    return grid

def Check_Directions(cell: Cell) -> list[str]:
    directions: list[str] = ["Top", "Left", "Bottom", "Right"]

    if cell.Column == 0:
        cell.Left = False
        directions.remove("Left")
    if cell.Row == 0:
        cell.Top = False
        directions.remove("Top")
    if cell.MaxRow == cell.Row:
        cell.Bottom = False
        directions.remove("Bottom")
    if cell.MaxColumn == cell.Column:
        cell.Right = False
        directions.remove("Right")
    return directions


def forbackward(grid: list[list], current_cell: Cell, next_step: str):
    if next_step == "Top" or next_step == "S":
        current_cell = grid[current_cell.Row - 1][current_cell.Column]
        move = "N"
    
    if next_step == "Bottom" or next_step == "N":
        current_cell = grid[current_cell.Row + 1][current_cell.Column]
        move = "S"

    if next_step == "Left" or next_step == "E":
        current_cell = grid[current_cell.Row][current_cell.Column - 1]
        move = "W"

    if next_step == "Right" or next_step == "W":
        current_cell = grid[current_cell.Row][current_cell.Column + 1]
        move = "E"

    return current_cell, move


def perfect(grid: list[list]):
    cells = []
    moves = []
    visited = []
    for row in range(len(grid)):
        for element in grid[row]:
            cells.append(element)
    
    #print(cells)

    random_row = random.choice(grid)
    point = random.choice(random_row)
    visited.append(point)
    #cells.remove(point)
    #directions = Check_Directions(point)
    #next_direction = random.choice(directions)
    
    directions = Check_Directions(point)

    while cells:
        #directions = Check_Directions(point)
        next_direction = random.choice(directions)
        directions.remove(next_direction)
        check_point, move = forbackward(grid, point, next_direction)
        moves.append(move)

        if len(directions) == 0:
            #next_direction = random.choice(directions)
            #directions.remove(next_direction)
        #else:
            back_direction = moves[-1]
            check_point, _ = forbackward(grid, point, back_direction)
            print(check_point)
            moves.pop()

            cells.remove(check_point)

        if check_point not in visited:
            visited.append(point)
            cells.remove(point)
            point = check_point






    











    '''
    visited = []
    random_row = random.choice(grid)
    point = random.choice(random_row)
    while cells:
        directions = Check_Directions(point)
        next_step = random.choice(directions)
        directions.remove(next_step)

        if len(directions) == 0:
            cells.remove(point)
            visited.append(point)
            random_row = random.choice(grid)
            point = random.choice(random_row)

        if next_step == "Top" and grid[point.Row - 1][point.Column] not in visited:
            cells.remove(point)
            visited.append(point)
            point = grid[point.Row - 1][point.Column]
            moves.append("N")

        elif next_step == "Bottom" and grid[point.Row + 1][point.Column] not in visited:
            cells.remove(point)
            visited.append(point)
            point = grid[point.Row + 1][point.Column]
            moves.append("S")

        elif next_step == "Left" and grid[point.Row][point.Column - 1] not in visited:
            cells.remove(point)
            visited.append(point)
            point = grid[point.Row][point.Column - 1]
            moves.append("W")

        elif next_step == "Right" and grid[point.Row][point.Column + 1] not in visited:
            cells.remove(point)
            visited.append(point)
            point = grid[point.Row][point.Column + 1]
            moves.append("E")

        else:
            continue
    return moves
    '''

print(perfect(Create_Grid(4, 4)))