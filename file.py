import os

def renameFiles():
    filesList = os.listdir(r"E:\PythonProjects\test")
    currentDir = os.getcwd()
    os.chdir(r"E:\PythonProjects\test")
    for fileName in filesList:
        os.rename(fileName,fileName.translate(None, "0123456789"))
    os.chdir(curr)
renameFiles()