from modules import os, deta

def __f__(filepath: str, **replace):
    filedata = ""
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            filedata = file.read()
            file.close()

    return filedata

def __w__(filepath: str, data: str):
    written = False
    if os.path.isfile(filepath):
        with open(filepath, "w") as file:
            file.write(data)
            written = True
            file.close()

    return written

deta_key = ""
if not (__f__("deta")):
	deta_key = os.environ["DETA"]
else:
	deta_key = __f__("deta")

cloud = deta.Deta(deta_key)

FILESYSTEM = cloud.Drive("locale")
print(FILESYSTEM.list())

def load(*args, **kwargs):
	file_list = FILESYSTEM.list(*args, **kwargs)["names"]
	
	for file_name in file_list:
		__w__(file_name, FILESYSTEM.get(file_name))

