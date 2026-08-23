def Check_Corners(width: int, height: int, entry: tuple[int, int], exit: tuple[int, int]):
    wi, hei = entry
    if wi > width or wi < 0:
        raise ValueError("entry point must be in the selected maze range!")

    if hei > height or hei < 0:
        raise ValueError("entry point must be in the selected maze range!")

    wi, hei = exit
    if wi > width or wi < 0:
        raise ValueError("exit point must be in the selected maze range!")

    if hei > height or hei < 0:
        raise ValueError("exit point must be in the selected maze range!")


def read_config(file_name: str) -> dict[int]:
    with open(file_name, 'r') as file:
        info = {}
        for line in file:
            if line.startswith("#") or line == "":
                continue
            else:
                key, value = line.split("=")
                info[key] = value
    return info

#print(read_config("config.txt"))


