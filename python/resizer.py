#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by Chao

# 本模块的功能:<更改图片尺寸>

import json
from PIL import Image

'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''


def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height), Image.ANTIALIAS)
    out.save(fileout, type)


def loadJson(filename):
    with open(filename) as file_obj:
        data = json.load(file_obj)
        return data


def getIcons(imgInfo):
    for info in imgInfo:
        if info['size'] == 'icon':
            continue
        size = int(int(info['scale'][0])*float(info['size'].split('x')[0]))
        ResizeImage('./icon.png', './{}'.format(info['filename']), size, size, 'png')


def getLaunchImages(imgInfo):
    file_path = './LaunchImage@3x.png'
    img = Image.open(file_path)
    for info in imgInfo:
        if info['scale'] == '3x':
            continue
        w = int(img.width/3*int(info['scale'][0]))
        h = int(img.height/3*int(info['scale'][0]))
        ResizeImage(file_path, './{}'.format(info['filename']), w, h, 'png')


if __name__ == "__main__":
    imgInfo = loadJson('./Contents.json')['images']
    if(imgInfo[0]['idiom'] == 'universal'):
        getLaunchImages(imgInfo)
    else:
        getIcons(imgInfo)

    print(list(map(lambda x: x['filename'], imgInfo)))
