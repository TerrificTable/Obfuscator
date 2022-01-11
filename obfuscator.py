import sys
import os


if len(sys.argv) <= 2:
    sys.exit("usage: obfuscator.py [-file/-folder] [path]")

working = os.getcwd().replace("\\", "/")
option = sys.argv[1]
path = sys.argv[2]

if path.__contains__(" "):
    sys.exit("Path can only contain letters and numbers")


if option == "-file":
    print(working + "/" + path)

elif option == "-folder":
    if path.startswith("./"):
        print(working + "/" + path.replace("./", "") + "/")
    else:
        print(working + "/" + path + "/")
