import sys
import os


if len(sys.argv) <= 2:
    sys.exit("usage: obfuscator.py [-file/-folder] [path]")

working = os.getcwd().replace("\\", "/") + "/"
option = sys.argv[1]
path = sys.argv[2]

if path.__contains__(" "):
    sys.exit("Path can only contain letters and numbers")


def obfuscate(path, folder=False, cwd=False, file=False) -> str:
    try:
        ofolder = os.path.join(working, "obf")
        os.mkdir(ofolder)
    except OSError:
        pass
    except:
        sys.exit("An error Accured while trying to create output folder")

    if folder:
        if cwd:
            outputFolder = working + path.split("/")[-1] + "/obf/"
        else:
            outputFolder = path.split("/")[-1] + "/obf/"

    elif file:
        outputFile = working + "obf/" + \
            path.split(".")[0] + "-obf." + path.split(".")[1]

        with open(outputFile, "w+") as f:
            pass


if option == "-file":
    obfuscate(path, file=True)

elif option == "-folder":
    if path.startswith("./"):
        path = working + path.replace("./", "")
        obfuscate(path, folder=True)
    else:
        obfuscate(path, folder=True, cwd=True)
