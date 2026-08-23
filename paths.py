def Check_Corners(width: int, height: int, entry_row: int, entry_column: int, exit_row: int, exit_column: int):
    if entry_row < 0 or entry_row >= height:
        raise ValueError("entry row is outside the maze!")

    if entry_column < 0 or entry_column >= width:
        raise ValueError("entry column is outside the maze!")

    if exit_row < 0 or exit_row >= height:
        raise ValueError("exit row is outside the maze!")

    if exit_column < 0 or exit_column >= width:
        raise ValueError("exit column is outside the maze!")
    

def read_config(file_name: str) -> dict[str, str]:
    with open(file_name, 'r') as file:
        info = {}
        for line in file:
            if line.startswith("#") or line == "\n":
                continue
            else:
                line = line.strip()
                key, value = line.split("=")
                info[key] = value
    return info

#print(read_config("config.txt"))


