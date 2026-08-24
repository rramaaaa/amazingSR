def Check_Corners(width: int, height: int, entry_row: int, entry_column: int, exit_row: int, exit_column: int) -> None:
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

        if "WIDTH" not in info:
            raise KeyError("config file must have a WIDTH")

        if "HEIGHT" not in info:
            raise KeyError("Config file must have a HEIGHT")

        if "ENTRY" not in info:
            raise KeyError("Config file must have an ENTRY point")

        if "EXIT" not in info:
            raise KeyError("Config file must have an EXIT point")

        if "OUTPUT_FILE" not in info:
            raise KeyError("Config file must have an OUTPUT FILE")

        if "PERFECT" not in info:
            raise KeyError("Config file must have a PERFECT status")
    return info

#print(read_config("config.txt"))


