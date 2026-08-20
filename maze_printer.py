from maze import MazeGenerator


def print_maze(cell: MazeGenerator.Cell):
    row = 3
    column = 3
    cell_walls = []
    for row in range(row):
        if row == 0:
            if cell.Top:
                for column in range(column):
                    cell_walls.append("█")
    return cell_walls

so = MazeGenerator.Cell(5, 5, 6, 6)
print(print_maze(so))
