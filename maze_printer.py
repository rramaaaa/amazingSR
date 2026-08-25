from maze import MazeGenerator

def Maze_Printer(grid: list[list["MazeGenerator.Cell"]], path: list[tuple[int, int]] = None) -> None:
    if path is None:
        path = []
        
    path_set = set(path)
    rows = len(grid)
    cols = len(grid[0])

    def h_wall(i, j):
        if i == 0 or i == rows:
            return True
        return grid[i - 1][j].Bottom

    def v_wall(i, j):
        if j == 0 or j == cols:
            return True
        return grid[i][j - 1].Right

    CORNERS = {
        (False, False, False, False): " ", (True,  False, False, False): "╵",
        (False, True,  False, False): "╷", (False, False, True,  False): "╴",
        (False, False, False, True):  "╶", (True,  True,  False, False): "│",
        (False, False, True,  True):  "─", (True,  False, True,  False): "┘",
        (True,  False, False, True):  "└", (False, True,  True,  False): "┐",
        (False, True,  False, True):  "┌", (True,  True,  True,  False): "┤",
        (True,  True,  False, True):  "├", (True,  False, True,  True):  "┴",
        (False, True,  True,  True):  "┬", (True,  True,  True,  True):  "┼",
    }

    def corner_char(i, j):
        up = v_wall(i - 1, j) if i > 0 else False
        down = v_wall(i, j) if i < rows else False
        left = h_wall(i, j - 1) if j > 0 else False
        right = h_wall(i, j) if j < cols else False
        return CORNERS[(up, down, left, right)]

    lines = []
    
    # ANSI Colors
    YELLOW_BG, YELLOW_FG = "\033[43m", "\033[33m"
    GREEN_BG, GREEN_FG = "\033[42m", "\033[32m"
    RESET = "\033[0m"

    for i in range(rows + 1):
        line = ""
        for j in range(cols):
            line += corner_char(i, j)
            line += "───" if h_wall(i, j) else "   "
        line += corner_char(i, cols)
        lines.append(line)

        if i < rows:
            cell_line = ""
            for j in range(cols):
                cell_line += "│" if v_wall(i, j) else " "
                

                if grid[i][j].Lock:
                    cell_line += f"{YELLOW_BG}{YELLOW_FG}███{RESET}"
            
                elif (i, j) in path_set:
                    cell_line += f"{GREEN_BG}{GREEN_FG}███{RESET}"
    
                else:
                    cell_line += "   "

            cell_line += "│" if v_wall(i, cols) else " "
            lines.append(cell_line)

    print("\n".join(lines))