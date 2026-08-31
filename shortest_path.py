from maze import MazeGenerator
from collections import deque


def Finding_shortest_path(
    grid: list[list[MazeGenerator.Cell]],
    entry: tuple[int, int],
    exit_point: tuple[int, int]
) -> tuple[list[tuple[int, int]], list[str]]:

    '''finding the shortest path through the maze'''

    height = len(grid)
    width = len(grid[0])

    q: deque[tuple[int, int]] = deque()
    visited: set[tuple[int, int]] = set()
    parent: dict[tuple[int, int], tuple[int, int, str]] = {}

    visited.add(entry)
    q.append(entry)

    while q:
        row, column = q.popleft()
        current = grid[row][column]

        if (row, column) == exit_point:
            break

        if not current.Top:
            neighbor = (row - 1, column)

            if (
                0 <= neighbor[0] < height
                and 0 <= neighbor[1] < width
                and neighbor not in visited
                and not grid[neighbor[0]][neighbor[1]].Lock
            ):
                visited.add(neighbor)
                parent[neighbor] = (row, column, "N")
                q.append(neighbor)

        if not current.Left:
            neighbor = (row, column - 1)

            if (
                0 <= neighbor[0] < height
                and 0 <= neighbor[1] < width
                and neighbor not in visited
                and not grid[neighbor[0]][neighbor[1]].Lock
            ):
                visited.add(neighbor)
                parent[neighbor] = (row, column, "W")
                q.append(neighbor)

        if not current.Bottom:
            neighbor = (row + 1, column)

            if (
                0 <= neighbor[0] < height
                and 0 <= neighbor[1] < width
                and neighbor not in visited
                and not grid[neighbor[0]][neighbor[1]].Lock
            ):
                visited.add(neighbor)
                parent[neighbor] = (row, column, "S")
                q.append(neighbor)

        if not current.Right:
            neighbor = (row, column + 1)

            if (
                0 <= neighbor[0] < height
                and 0 <= neighbor[1] < width
                and neighbor not in visited
                and not grid[neighbor[0]][neighbor[1]].Lock
            ):
                visited.add(neighbor)
                parent[neighbor] = (row, column, "E")
                q.append(neighbor)

    if exit_point not in visited:
        return [], []

    goal = exit_point
    s_path: list[tuple[int, int]] = []
    moves: list[str] = []

    while goal != entry:
        s_path.append(goal)

        parent_row, parent_column, direction = parent[goal]

        moves.append(direction)

        goal = (parent_row, parent_column)

    s_path.append(entry)

    s_path.reverse()
    moves.reverse()

    return s_path, moves
