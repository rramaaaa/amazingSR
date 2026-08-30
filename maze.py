import random


class MazeGenerator:
    class Cell:
        def __init__(
                self, row: int, column: int,
                maxrow: int, maxcolumn: int
                ) -> None:
            self.Top: bool = True
            self.Bottom: bool = True
            self.Right: bool = True
            self.Left: bool = True
            self.Lock: bool = False
            self.Row: int = row
            self.Column: int = column
            self.cell_direction: list[str] = self.Check_Directions(
                    maxrow, maxcolumn
                    )

        def Check_Directions(self, maxrow: int, maxcolumn: int) -> list[str]:
            directions: list[str] = ["Top", "Left", "Bottom", "Right"]

            if self.Column == 0:
                directions.remove("Left")
            if self.Row == 0:
                directions.remove("Top")
            if maxrow == self.Row:
                directions.remove("Bottom")
            if maxcolumn == self.Column:
                directions.remove("Right")
            return directions

    def Create_Grid(
            self, rows: int, columns: int
            ) -> list[list[Cell]]:
        self.grid = []
        for i in range(rows):
            cell: list[MazeGenerator.Cell] = []
            self.grid.append(cell)
            for j in range(columns):
                cell.append(self.Cell(i, j, rows - 1, columns - 1))
        return self.grid

    def backward(
            self, grid: list[list[Cell]], current_cell: Cell,
            next_step: str
            ) -> Cell:
        if next_step == "N" or next_step == "Top":
            current_cell = grid[current_cell.Row - 1][current_cell.Column]

        if next_step == "S" or next_step == "Bottom":
            current_cell = grid[current_cell.Row + 1][current_cell.Column]

        if next_step == "W" or next_step == "Left":
            current_cell = grid[current_cell.Row][current_cell.Column - 1]

        if next_step == "E" or next_step == "Right":
            current_cell = grid[current_cell.Row][current_cell.Column + 1]

        return current_cell

    def forward(
            self, grid: list[list[Cell]], current_cell: Cell,
            next_step: str
            ) -> tuple[Cell, str]:
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

    def remove_walls(self) -> list[list[Cell]]:
        for i in range(len(self.grid) * 5):
            rand_row = random.choice(self.grid)
            rand_c = random.choice(rand_row)
            if rand_c.cell_direction:
                random_wall = random.choice(rand_c.cell_direction)
                if random_wall == "Top":
                    rand_c.Top = False
                    rand_c.cell_direction.remove("Top")
                    neighbor = self.grid[rand_c.Row - 1][rand_c.Column]
                    neighbor.Bottom = False

                if random_wall == "Bottom":
                    rand_c.Bottom = False
                    rand_c.cell_direction.remove("Bottom")
                    neighbor = self.grid[rand_c.Row + 1][rand_c.Column]
                    neighbor.Top = False

                if random_wall == "Left":
                    rand_c.Left = False
                    rand_c.cell_direction.remove("Left")
                    self.grid[rand_c.Row][rand_c.Column - 1].Right = False

                if random_wall == "Right":
                    rand_c.Right = False
                    rand_c.cell_direction.remove("Right")
                    self.grid[rand_c.Row][rand_c.Column + 1].Left = False

        return self.grid

    def Generate_Maze(
            self, grid: list[list[Cell]],
            perfect: str) -> list[list[Cell]]:
        cells = []
        moves = []
        visited = []
        for row in range(len(grid)):
            for element in grid[row]:
                if not element.Lock:
                    cells.append(element)

        start_random_point = random.choice(cells)
        point = start_random_point

        while cells:

            if point not in visited:

                visited.append(point)
                cells.remove(point)

                if not point.cell_direction:
                    continue

                direction = random.choice(point.cell_direction)
                point.cell_direction.remove(direction)

                next_point = self.backward(grid, point, direction)

                if next_point not in visited and not next_point.Lock:
                    point, move = self.forward(grid, point, direction)
                    moves.append(move)

            else:
                if len(point.cell_direction) != 0:
                    direction = random.choice(point.cell_direction)
                    point.cell_direction.remove(direction)

                    next_point = self.backward(grid, point, direction)

                    if next_point not in visited and not next_point.Lock:
                        point, move = self.forward(grid, point, direction)
                        moves.append(move)

                else:
                    if len(point.cell_direction) == 0:
                        if moves[-1] == "N":
                            next_direction = "S"

                        elif moves[-1] == "S":
                            next_direction = "N"

                        elif moves[-1] == "E":
                            next_direction = "W"

                        else:
                            next_direction = "E"

                        point = self.backward(grid, point, next_direction)
                        moves.pop()

        if perfect == "True":
            return grid

        grid = self.remove_walls()

        return grid
