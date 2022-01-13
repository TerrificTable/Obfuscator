from random import Random
import sys
import os


if len(sys.argv) <= 2:
    sys.exit("usage: obfuscator.py [-file/-folder] [path]")

working = os.getcwd().replace("\\", "/") + "/"
option = sys.argv[1]
path = sys.argv[2]

if path.__contains__(" "):
    sys.exit("Path can only contain letters and numbers")


def __obfuscate__(path, folder=False, file=False) -> str:  # TODO Obfuscation
    pass


def obfuscate_base(path, folder=False, cwd=False, file=False) -> str:
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
            code = __obfuscate__(working + path.split("/")
                                 [-1] + "file", folder=True)  # TODO File
            with open(outputFolder + "", "w+") as f:  # TODO File
                f.write(code)

        else:
            outputFolder = path + "/obf/"
            code = __obfuscate__(path + "file", folder=True)  # TODO File
            with open(outputFolder + "", "w+") as f:  # TODO File
                f.write(code)

    elif file:
        outputFile = working + "obf/" + \
            path.split(".")[0] + "-obf." + path.split(".")[1]
        code = __obfuscate__(working + path, file=True)

        with open(outputFile, "w+") as f:
            f.write(code)


if option == "-file":
    obfuscate_base(path, file=True)

elif option == "-folder":
    if path.startswith("./"):
        path = working + path.replace("./", "")
        obfuscate_base(path, folder=True)
    else:
        obfuscate_base(path, folder=True, cwd=True)
