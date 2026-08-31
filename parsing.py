from maze import MazeGenerator


def Check_Corners(height: int, width: int,
                  entry_row: int, entry_column: int,
                  exit_row: int, exit_column: int
                  ) -> None:

    '''Check that the entry and exit are inside the maze'''

    if entry_row < 0 or entry_row >= height:
        raise ValueError("entry row is outside the maze!")

    if entry_column < 0 or entry_column >= width:
        raise ValueError("entry column is outside the maze!")

    if exit_row < 0 or exit_row >= height:
        raise ValueError("exit row is outside the maze!")

    if exit_column < 0 or exit_column >= width:
        raise ValueError("exit column is outside the maze!")

    if entry_row == exit_row and exit_column == exit_column:
        raise ValueError("entry and exit point can't be the same!")


def Check_not_in_lock(grid: list[list[MazeGenerator.Cell]],
                      entry_row: int, entry_column: int,
                      exit_row: int, exit_column: int
                      ) -> None:

    '''Check that the entry and exit are not inside the 42 lock'''

    if grid[entry_row][entry_column].Lock:
        raise ValueError("The entry point is placed on the locked 42 point")

    if grid[exit_row][exit_column].Lock:
        raise ValueError("The exit point is placed on the locked 42 point")


def read_config(file_name: str) -> dict[str, str]:

    '''Read and validate the maze configuration file'''

    with open(file_name, 'r') as file:
        info = {}
        for line in file:
            if line.startswith("#") or line == "\n":
                continue
            else:
                line = line.strip()
                parts = line.split("=")
                if len(parts) != 2:
                    raise ValueError(
                        "please enter a correct format! '(KEY=VAlUE)'"
                        )
                key, value = parts
                info[key.lower()] = value.lower()

        if "width" not in info:
            raise KeyError("config file must have a WIDTH")

        if "height" not in info:
            raise KeyError("Config file must have a HEIGHT")

        if "entry" not in info:
            raise KeyError("Config file must have an ENTRY point")

        if "exit" not in info:
            raise KeyError("Config file must have an EXIT point")

        if "output_file" not in info:
            raise KeyError("Config file must have an OUTPUT FILE")

        if "perfect" not in info:
            raise KeyError("Config file must have a PERFECT status")

    return info
