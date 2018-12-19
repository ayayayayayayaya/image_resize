# -*- coding: utf-8 -*-

import cv2
import glob

images = glob.glob("/source/azur/splitted/*.png")
for img in images:
    dat = cv2.imread(img)
    dat = cv2.resize(dat,(150, 150))
    cv2.imwrite(img, dat)
