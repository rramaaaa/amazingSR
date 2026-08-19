from collections.abc import Callable
import random



class MazeGenerator:
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
            self.cell_direction: list[str] = self.Check_Directions()

        def Check_Directions(self) -> list[str]:
            directions: list[str] = ["Top", "Left", "Bottom", "Right"] 

            if self.Column == 0:
                directions.remove("Left")
            if self.Row == 0:
                directions.remove("Top")
            if self.MaxRow == self.Row:
                directions.remove("Bottom")
            if self.MaxColumn == self.Column:
                directions.remove("Right")
            return directions


    def Create_Grid(self, rows: int, columns: int) -> list[list: Callable]:
        grid: list = list()
        for i in range(rows):
            cell: list = []
            grid.append(cell)
            for j in range(columns):
                cell.append(self.Cell(i, j, rows - 1, columns - 1))
                #print(grid[i][j].Row, grid[i][j].Column)
        return grid

    def Check_Directions(self, cell: Cell) -> list[str]:
        directions: list[str] = ["Top", "Left", "Bottom", "Right"]

        if cell.Column == 0:
            directions.remove("Left")
        if cell.Row == 0:
            directions.remove("Top")
        if cell.MaxRow == cell.Row:
            directions.remove("Bottom")
        if cell.MaxColumn == cell.Column:
            directions.remove("Right")
        return directions


    def forbackward(self, grid: list[list], current_cell: Cell, next_step: str):
        move = ""

        if next_step == "Top" or next_step == "N":
            current_cell.Top = False
            current_cell = grid[current_cell.Row - 1][current_cell.Column]
            move = "N"
    
        if next_step == "Bottom" or next_step == "S":
            current_cell.Bottom = False
            current_cell = grid[current_cell.Row + 1][current_cell.Column]
            move = "S"

        if next_step == "Left" or next_step == "W":
            current_cell.Left = False
            current_cell = grid[current_cell.Row][current_cell.Column - 1]
            move = "W"

        if next_step == "Right" or next_step == "E":
            current_cell.Right = False
            current_cell = grid[current_cell.Row][current_cell.Column + 1]
            move = "E"

        return current_cell, move


    def Generate_Maze(self, grid: list[list[Cell]]):
        cells = []
        moves = []
        visited = []
        for row in range(len(grid)):
            for element in grid[row]:
                cells.append(element)
    
        start_random_point = random.choice(cells) 
        point = start_random_point
        
        while cells:
       
            if point not in visited:
                visited.append(point)
                cells.remove(point)
                direction = random.choice(point.cell_direction)
                point.cell_direction.remove(direction)
                point, move = self.forbackward(grid, point, direction)
                moves.append(move)

            else:
                if len(point.cell_direction) != 0:
                    direction = random.choice(point.cell_direction)
                    point.cell_direction.remove(direction)
                    point, move = self.forbackward(grid, point, direction)
                    moves.append(move)

                if len(point.cell_direction) == 0:
                    if moves[-1] == "N":
                        next_direction = "S"
            
                    elif moves[-1] == "S":
                        next_direction = "N"
                    
                    elif moves[-1] == "E": 
                        next_direction = "W"
                
                    else:
                        next_direction = "E"

                    point, _ = self.forbackward(grid, point,next_direction)
                    moves.pop()
        return moves

obj = MazeGenerator()
print(obj.Generate_Maze(obj.Create_Grid(16, 4)))