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
            cell.append(Cell(i, j, row - 1, columns - 1))
    return grid

def Check_Directions(cell: Cell) -> Cell:
    directions = ["Top", "Left", "Bottom", "Right"]

    if cell.Column == 0:
        cell.Left = False
    if cell.Row == 0:
        cell.Top = False
    if cell.MaxRow == cell.Row:
        cell.Bottom = False
    if cell.MaxColumn == cell.Column:
        cell.Right = False



def perfect(grid: list[list]):
    visited = []
    start_point = random.random(grid)
    visited.append(start_point)

