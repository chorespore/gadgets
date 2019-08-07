import os

files = os.listdir("./")
files.sort()
idx = 0
for file in files:
    print(file)
    if(os.path.splitext(file)[1] == ".png" and ". " not in file):
        idx = idx+1
        newName = str(idx)+". "+file
        print(file+" => "+newName)
        os.rename(file, newName)

print(str(idx)+" files renamed!")
