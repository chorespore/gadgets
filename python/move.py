from os import *
import shutil

src = 'E:/Movies/91'

files = listdir(src)

for item in files:
    # print(item)
    p = path.join(src, item)
    if path.isdir(p):
        # print(listdir(p))
        for f in listdir(p):
            if path.splitext(f)[-1] == '.mp4':
                print(f)
                shutil.move(path.join(p, f), 'E:/Movies/guodong')
