from modules import os
from process.database import FILESYSTEM

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
    
    if f(filepath):
        FILESYSTEM.put(filepath, f(filepath))

    return written


def bot_prefixes():
    raw = f("locale/prefix").split("\n")
    prefixes = {}

    for raw_prefix in raw:
        category = raw_prefix[:1]
        prefix = raw_prefix[2:]

        if category not in prefixes:
            prefixes[category] = []
        
        prefixes[category].append(prefix)
    
    return prefixes

