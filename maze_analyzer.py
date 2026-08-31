from maze import MazeGenerator
from shortest_path import Finding_shortest_path


def output(grid: list[list[MazeGenerator.Cell]]) -> list[list[int]]:

    '''Convert maze walls into numeric values'''

    result = []
    for row in grid:
        res_row = []
        for column in row:
            num = 0
            if column.Top:
                num += 1
            if column.Right:
                num += 2
            if column.Bottom:
                num += 4
            if column.Left:
                num += 8
            res_row.append(num)
        result.append(res_row)

    return result


def Output_Maze(grid: list[list[MazeGenerator.Cell]],
                file_name: str,
                entry: tuple[int, int], ext: tuple[int, int]
                ) -> None:

    '''Generate the maze output file'''
    result = output(grid)
    with open(file_name, "w") as f:
        for row in result:
            for num in row:
                f.write(hex(num)[2:])
            f.write("\n")

        entry_row, entry_column = entry
        exit_row, exit_column = ext
        f.write("\n")
        f.write(f"{entry_row},{entry_column}")
        f.write("\n")
        f.write(f"{exit_row},{exit_column}")
        f.write("\n")

        _, moves = Finding_shortest_path(grid, entry, ext)
        for move in moves:
            f.write(move)
        f.write("\n")
