#!/usr/bin/env python


import os
import shutil

def main():
    folderPath = "../data"
    dataSavePath = "../dataNew"
    folderNameList = os.listdir(folderPath)
    count = 1
    for folder in folderNameList:
        imgFolderPath = os.path.join(folderPath,folder)
        dryimgNameList = os.listdir(os.path.join(imgFolderPath,"dry"))
        #wetimgNameList = os.listdir(os.path.join(imgFolderPath, "wet"))
        for dryimgName in dryimgNameList:
            srcdryimg = os.path.join(imgFolderPath,"dry",dryimgName)
            srcwetimg = os.path.join(imgFolderPath,"wet",dryimgName.split("_")[0]+"_wet.png")
            dstdryimg = os.path.join(dataSavePath,"dry",str(count)+".png")
            dstwetimg = os.path.join(dataSavePath, "wet", str(count) + ".png")
            shutil.copy(srcdryimg,dstdryimg)
            shutil.copy(srcwetimg, dstwetimg)
            count = count + 1






if __name__ == "__main__":
    main()