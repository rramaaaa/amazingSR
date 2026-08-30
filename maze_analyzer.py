from maze import MazeGenerator
from shortest_path import Finding_shortest_path


def output(grid: list[list[MazeGenerator.Cell]]) -> list[list[int]]:
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


def to_hexa(grid: list[list[MazeGenerator.Cell]],
            nums: list[list[int]],
            entry_row: int, entry_column: int,
            exit_row: int, exit_column: int
            ) -> None:

    for lst in nums:
        for num in lst:
            print(hex(num)[2:], end="")
        print()

    print()
    print(f"{entry_row},{entry_column}")
    print(f"{exit_row},{exit_column}")

    entry = (entry_row, entry_column)
    ext = (exit_row, exit_column)
    _, moves = Finding_shortest_path(grid, entry, ext)
    for move in moves:
        print(move, end="")
    print()
