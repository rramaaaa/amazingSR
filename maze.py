import random


class MazeGenerator:
    class Cell:
        def __init__(
                self, row: int, column: int,
                maxrow: int, maxcolumn: int
                ) -> None:

            '''Initialize a maze cell'''

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

            '''Check the available directions for a cell'''

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

        '''Create a maze grid with the given dimensions'''

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

        '''Move backward to the neighboring cell'''

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

        '''Move to the next cell'''

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


    def How_Many_walls(self, cell: Cell) -> int:
        tot = 0
        if cell.Top:
            tot += 1
        if cell.Bottom:
            tot += 1
        if cell.Right:
            tot += 1
        if cell.Left:
            tot += 1

        return tot


    def remove_walls(self) -> list[list[Cell]]:

        '''Open random walls to make the maze imperfect'''

        rows = len(self.grid)
        columns = len(self.grid[0])

        for row in self.grid:
            for cell in row:
                tot_walls = self.How_Many_walls(cell)
                if tot_walls != 3 or cell.Lock:
                    continue

                walls = []
                if cell.Row > 0 and cell.Top:
                    walls.append("Top")

                if cell.Row < rows - 1 and cell.Bottom:
                    walls.append("Bottom")

                if cell.Column > 0 and cell.Left:
                    walls.append("Left")

                if cell.Column < columns - 1 and cell.Right:
                    walls.append("Right")

                if not walls:
                    continue

                random_wall = random.choice(walls)
                if random_wall == "Top":
                    cell.Top = False
                    self.grid[cell.Row - 1][cell.Column].Bottom = False

                elif random_wall == "Bottom":
                    cell.Bottom = False
                    self.grid[cell.Row + 1][cell.Column].Top = False

                elif random_wall == "Left":
                    cell.Left = False
                    self.grid[cell.Row][cell.Column - 1].Right = False

                elif random_wall == "Right":
                    cell.Right = False
                    self.grid[cell.Row][cell.Column + 1].Left = False

        return self.grid

    def Generate_Maze(
            self, grid: list[list[Cell]],
            perfect: str, seed: int | None = None) -> list[list[Cell]]:

        '''Generate the maze by visiting cells and removing walls'''

        if seed:
            random.seed(seed)
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

        if perfect:
            return grid

        grid = self.remove_walls()

        return grid
