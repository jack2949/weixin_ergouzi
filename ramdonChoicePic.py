#!/usr/bin/python
#coding:gbk

from bs4 import BeautifulSoup
import time,sys,os,json
import pynotify,urllib2,random

def saveImg(imgUrl, imgName):
    #_checkPath(imgName)
    true_path = imgName + imgUrl[imgUrl.rfind('.'):]

    command = "wget " + imgUrl + " -q -O " + true_path
    os.system(command)

    return true_path

def getRanPic(imgName):
    f = open("pic.config", 'r')
    config = json.loads(f.read())
    f.close()
    item = random.choice(config["data"])
    #print json.dumps(item, indent = 4)
    filname = saveImg(item["path"], imgName)

    return filname,item["name"]


if __name__ == '__main__':
    file,name = getRanPic("aa")
    print file
    print name
    #getRandomPic(targat_sub_url)
