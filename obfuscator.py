from random import Random
import sys
import os
import codecs


if len(sys.argv) <= 2:
    sys.exit("usage: obfuscator.py [-file/-folder] [path]")

working = os.getcwd().replace("\\", "/") + "/"
option = sys.argv[1]
path = sys.argv[2]

if path.__contains__(" "):
    sys.exit("Path can only contain letters and numbers")


def __obfuscate__(path, outputPath, folder=False, file=False) -> str:  # TODO Folder Encoding
    try:
        # File Encoding
        if file:
            with open(path, "r") as f:
                file_content = f.read()
                encoded_file_content = codecs.encode(
                    bytes(file_content, 'utf-8'), 'base64').decode('utf-8').replace("\n", "")
                if path.endswith(".py"):
                    new_file_content = f"""import codecs; exec(codecs.decode(b"{encoded_file_content}", 'base64').decode('utf-8'))"""
                else:
                    new_file_content = encoded_file_content

            with open(outputPath, "w") as f:
                f.write(new_file_content)

        # Folder Encoding -----> DOES NOT WORK WELLs
        elif folder:
            for file in os.listdir(path.replace("\\", "//").replace("/", "//")):

                with open(path + "/" + file, "r") as f:
                    file_content = f.read()
                    encoded_file_content = codecs.encode(
                        bytes(file_content, 'utf-8'), 'base64').decode('utf-8').replace("\n", "")
                    if file.endswith(".py"):
                        new_file_content = f"""import codecs; exec(codecs.decode(b"{encoded_file_content}", 'base64').decode('utf-8'))"""
                    else:
                        new_file_content = encoded_file_content

                if file != "desktop.ini":
                    with open(outputPath + "/" + file.split(".")[0] + "-obf." + file.split(".")[-1], "w") as f:
                        f.write(new_file_content)
        else:
            pass
    except Exception as e:
        sys.exit("Error Accured while trying to encode files\n" + str(e))


def obfuscate_base(path, folder=False, cwd=False, file=False) -> str:
    try:
        if file:
            ofolder = os.path.join(working, "obf")
            os.mkdir(ofolder)
        elif folder:
            ofolder = os.path.join(path, "obf")
            os.mkdir(ofolder)
        else:
            pass
    except OSError:
        pass
    except:
        sys.exit("An error Accured while trying to create output folder")

    if folder:
        if cwd:
            outputFolder = path + "/obf/"
            __obfuscate__(path,
                          outputFolder, folder=True)
        else:
            outputFolder = path + "/obf/"
            __obfuscate__(path, outputFolder,
                          folder=True)

    elif file:
        outputFile = working + "obf/" + \
            path.split(".")[1] + "-obf." + path.split(".")[-1]

        __obfuscate__(
            working + path.replace("./", ""), outputFile, file=True)

    else:
        sys.exit("usage: obfuscator.py [-file/-folder] [path]")


if option == "-file":
    obfuscate_base(path, file=True)

elif option == "-folder":
    if path.startswith("./"):
        path = working + path.replace("./", "")
        obfuscate_base(path, folder=True)
    else:
        obfuscate_base(path, folder=True, cwd=True)
