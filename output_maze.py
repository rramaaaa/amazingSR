from maze import MazeGenerator


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


def to_hexa(nums: list[list[int]]):
    for lst in nums:
        for num in lst:
            print(hex(num)[2:], end="")
        print()



obj = MazeGenerator()
grid = obj.Create_Grid(10, 10)
out = obj.Generate_Maze(grid)
res = output(out)
to_hexa(res)
