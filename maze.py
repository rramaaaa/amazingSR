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


    def Create_Grid(self, rows: int, columns: int) -> list[list[Cell]]:
        self.grid: list = list()
        for i in range(rows):
            cell: list = []
            self.grid.append(cell)
            for j in range(columns):
                cell.append(self.Cell(i, j, rows - 1, columns - 1))
                #print(grid[i][j].Row, grid[i][j].Column)
        return self.grid


    def backward(self, grid: list[list], current_cell: Cell, next_step: str) -> Cell:
        if next_step == "N" or next_step == "Top":
            current_cell = grid[current_cell.Row - 1][current_cell.Column]

        if next_step == "S" or next_step == "Bottom":
            current_cell = grid[current_cell.Row + 1][current_cell.Column]

        if next_step == "W" or next_step == "Left":
            current_cell = grid[current_cell.Row][current_cell.Column - 1]

        if next_step == "E" or next_step == "Right":
            current_cell = grid[current_cell.Row][current_cell.Column + 1]

        return current_cell
            

    def forward(self, grid: list[list], current_cell: Cell, next_step: str) -> tuple[Cell, str]:
        move = ""

        if next_step == "Top":
            current_cell.Top = False
            current_cell = grid[current_cell.Row - 1][current_cell.Column]
            current_cell.Bottom = False
            move = "N"
    
        if next_step == "Bottom":
            current_cell.Bottom = False
            current_cell = grid[current_cell.Row + 1][current_cell.Column]
            current_cell.Top = False
            move = "S"

        if next_step == "Left":
            current_cell.Left = False
            current_cell = grid[current_cell.Row][current_cell.Column - 1]
            current_cell.Right = False
            move = "W"

        if next_step == "Right":
            current_cell.Right = False
            current_cell = grid[current_cell.Row][current_cell.Column + 1]
            current_cell.Left = False
            move = "E"

        return current_cell, move


    def Generate_Maze(self, grid: list[list[Cell]], perfect: str) -> list[list[Cell]]:
        cells = []
        moves = []
        visited = []
        for row in range(len(grid)):
            for element in grid[row]:
                cells.append(element)

        total_cells = len(cells)
    
        start_random_point = random.choice(cells) 
        point = start_random_point

        while cells:
       
            if point not in visited:
                visited.append(point)
                cells.remove(point)
                direction = random.choice(point.cell_direction)
                point.cell_direction.remove(direction)

                if self.backward(grid, point, direction) not in visited:
                    point, move = self.forward(grid, point, direction)
                    moves.append(move)

            else:
                if len(point.cell_direction) != 0:
                    direction = random.choice(point.cell_direction)
                    point.cell_direction.remove(direction)

                    if self.backward(grid, point, direction) not in visited:
                        point, move = self.forward(grid, point, direction)
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

                    point = self.backward(grid, point,next_direction)
                    moves.pop()
        if perfect == "True":
            return grid

        for i in range(len(grid)*2):
            random_row = random.choice(grid)
            random_cell = random.choice(random_row)
            if random_cell.cell_direction:
                random_wall = random.choice(random_cell.cell_direction)
                if random_wall == "Top":
                    random_cell.Top = False
                    random_cell.cell_direction.remove("Top")
                    grid[random_cell.Row - 1][random_cell.Column].Bottom = False

                if random_wall == "Bottom":
                    random_cell.Bottom = False
                    random_cell.cell_direction.remove("Bottom")
                    grid[random_cell.Row + 1][random_cell.Column].Top = False

                if random_wall == "Left":
                    random_cell.Left = False
                    random_cell.cell_direction.remove("Left")
                    grid[random_cell.Row][random_cell.Column - 1].Right = False

                if random_wall == "Right":
                    random_cell.Right = False
                    random_cell.cell_direction.remove("Right")
                    grid[random_cell.Row][random_cell.Column + 1].Left = False

        return grid


#obj = MazeGenerator()
#print(obj.Generate_Maze(obj.Create_Grid(4, 4)))
#obj = MazeGenerator()
#grid = obj.Create_Grid(16, 16)
#grid = obj.Generate_Maze(grid, "False")
#Maze_Printer(grid)
#obj.Maze_Printer(grid)
