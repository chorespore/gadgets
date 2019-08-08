# coding=utf-8
import os

fileType = [".png", ".pdf"]
files = os.listdir("./")
files.sort()

cmd = input("1: 生成编号\n2: 清除编号\n")

if(cmd is "1"):
    idx = 0
    for file in files:
        if(os.path.splitext(file)[1] in fileType and ". " not in file):
            idx = idx+1
            newName = str(idx)+". "+file
            print(file+" => "+newName)
            os.rename(file, newName)

    print(str(idx)+" files renamed!")

if (cmd is "2"):
    idx = 0
    for file in files:
        if(os.path.splitext(file)[1] in fileType and ". " in file):
            idx = idx+1
            newName = file[file.index(". ")+2:]
            print(file+" => "+newName)
            os.rename(file, newName)

    print(str(idx)+" files renamed!")

