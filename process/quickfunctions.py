import os


def f(filepath: str, **replace):
    filedata = ""
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            filedata = file.read()
            file.close()

    for string in replace:
        filedata.replace(f"[[{string}]]", replace[string])

    return filedata


def w(filepath: str, method: str, data: str):
    written = False
    if os.path.isfile(filepath):
        with open(filepath, method) as file:
            file.write(data)
            written = True
            file.close()

    return written
