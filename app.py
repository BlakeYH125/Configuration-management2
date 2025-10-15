import sys

params = {
    "Package name": "",
    "File path": "",
    "Mode": "",
    "Version": "",
    "Graph name": "",
    "Max depth": -1,
    "Substring": ""
}

args = sys.argv[1:]

if len(args) != 7:
    print("Неверное количество параметров.")
    exit(-1)
else:
    params["Package name"] = args[0]
    params["File path"] = args[1]
    params["Mode"] = args[2]
    params["Version"] = args[3]
    params["Graph name"] = args[4]
    params["Max depth"] = args[5]
    params["Substring"] = args[6]

for k, v in params.items():
    print(f"{k}: {v}")
