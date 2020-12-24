#!/usr/bin/env python

import os
import random
import cv2 as cv

oriDataPath = "../dataNew"
datasavePath = "../dataNew_aug"
datatype = ["dry","wet"]

def ProcessNoisedAug(dryimg,wetimg):
    '''
    process the Noises Aug
    '''
    randomInt = random.sample(range(-20, 20), 1) # get the randnom noise
    noiseddryImg = dryimg + randomInt
    noisedwetimg = wetimg + randomInt
    return noiseddryImg,noisedwetimg

def main():
    #folderList = os.listdir(oriDataPath)
    if not os.path.exists(os.path.join(datasavePath,datatype[0])):
        os.mkdir(os.path.join(datasavePath,datatype[0]))
    if not os.path.exists(os.path.join(datasavePath,datatype[1])):
        os.mkdir(os.path.join(datasavePath,datatype[1]))

    dryPath = os.path.join(oriDataPath,datatype[0])
    wetPath = os.path.join(oriDataPath,datatype[1])
    dryimgNameList = os.listdir(dryPath)

    for dryimgName in dryimgNameList:
        # get the dry and wet img pairs
        dryimgPath = os.path.join(dryPath,dryimgName)
        wetimgPath = os.path.join(wetPath,dryimgName)
        print("the pairs is: %s and %s" % (dryimgPath,wetimgPath))
        dryimg = cv.imread(dryimgPath)
        print("the dry img shape is: ",dryimg.shape) # [height,width,channel]
        wetimg = cv.imread(wetimgPath)
        print("the wet img shape is: ", wetimg.shape)
        # save the oriimg
        cv.imwrite(os.path.join(datasavePath, datatype[0], dryimgName),dryimg)
        cv.imwrite(os.path.join(datasavePath, datatype[1], dryimgName), wetimg)
        # do the noise aug and save
        noiseddryImg, noisedwetimg = ProcessNoisedAug(dryimg,wetimg)
        noiseddryImgSavePath = os.path.join(datasavePath,datatype[0],dryimgName.split(".")[0]+"_noised.png")
        cv.imwrite(noiseddryImgSavePath,noiseddryImg)
        noisedwetimgSavePath = os.path.join(datasavePath,datatype[1],dryimgName.split(".")[0]+"_noised.png")
        cv.imwrite(noisedwetimgSavePath, noisedwetimg)
        # do the flip aug and save
        flipdryimg = cv.flip(dryimg, 1)
        flipwetimg = cv.flip(wetimg, 1)
        flipdryimgSavePath = os.path.join(datasavePath, datatype[0], dryimgName.split(".")[0] + "_flip.png")
        cv.imwrite(flipdryimgSavePath, flipdryimg)
        flipwetimgSavePath = os.path.join(datasavePath, datatype[1], dryimgName.split(".")[0] + "_flip.png")
        cv.imwrite(flipwetimgSavePath, flipwetimg)
        # do the Gussian blur aug and save
        blurdryimg = cv.GaussianBlur(dryimg,(3,3),0)
        blurwetimg = cv.GaussianBlur(wetimg, (3, 3), 0)
        blurdryImgSavePath = os.path.join(datasavePath, datatype[0], dryimgName.split(".")[0] + "_blur.png")
        cv.imwrite(blurdryImgSavePath, blurdryimg)
        noisedwetimgSavePath = os.path.join(datasavePath, datatype[1], dryimgName.split(".")[0] + "_blur.png")
        cv.imwrite(noisedwetimgSavePath, blurwetimg)


if __name__ == "__main__":
    main()