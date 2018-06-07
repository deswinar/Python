import numpy as np
from PIL import ImageGrab
from directkeys import PressKey, ReleaseKey, KEY_D, KEY_F, KEY_SPACE, KEY_J, KEY_K
import time
from threading import Thread

foundD, foundF, foundJ, foundK = 0,0,0,0


def pressKey(key):
    time.sleep(0.54)
    PressKey(key)
def releaseKey(key):
    time.sleep(0.54)
    ReleaseKey(key)

while True:
    screenD =  ImageGrab.grab(bbox=(219, 0, 265, 15))
    zerosD = np.array(screenD)
    indicesD = np.where(zerosD==[0,0,0])
    coordinatesD = zip(indicesD[0], indicesD[1])

    screenF =  ImageGrab.grab(bbox=(267, 0, 313, 15))
    zerosF = np.array(screenF)
    indicesF = np.where(zerosF==[0,0,0])
    coordinatesF = zip(indicesF[0], indicesF[1])

    screenJ =  ImageGrab.grab(bbox=(315, 0, 361, 15))
    zerosJ = np.array(screenJ)
    indicesJ = np.where(zerosJ==[0,0,0])
    coordinatesJ = zip(indicesJ[0], indicesJ[1])

    screenK =  ImageGrab.grab(bbox=(363, 0, 409, 15))
    zerosK = np.array(screenK)
    indicesK = np.where(zerosK==[0,0,0])
    coordinatesK = zip(indicesK[0], indicesK[1])

    if(len(coordinatesD) <= 1900):
        if(foundD == 0):
            startThreadD = Thread(target=pressKey, args=(KEY_D,)).start()
        foundD = 1

    if(len(coordinatesD) >= 1900):
        if(foundD == 1):
            endThreadD = Thread(target=releaseKey, args=(KEY_D,)).start()
        foundD = 0

    if(len(coordinatesF) <= 1900):
        if(foundF == 0):
            startThreadF = Thread(target=pressKey, args=(KEY_F,)).start()
        foundF = 1

    if(len(coordinatesF) >= 1900):
        if(foundF == 1):
            endThreadF = Thread(target=releaseKey, args=(KEY_F,)).start()
        foundF = 0

    if(len(coordinatesJ) <= 1900):
        if(foundJ == 0):
            startThreadJ = Thread(target=pressKey, args=(KEY_J,)).start()
        foundJ = 1

    if(len(coordinatesJ) >= 1900):
        if(foundJ == 1):
            endThreadJ = Thread(target=releaseKey, args=(KEY_J,)).start()
        foundJ = 0

    if(len(coordinatesK) <= 1900):
        if(foundK == 0):
            startThreadK = Thread(target=pressKey, args=(KEY_K,)).start()
        foundK = 1

    if(len(coordinatesK) >= 1900):
        if(foundK == 1):
            endThreadK = Thread(target=releaseKey, args=(KEY_K,)).start()
        foundK = 0
