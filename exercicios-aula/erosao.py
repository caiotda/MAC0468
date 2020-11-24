import cv2 as cv
import numpy as np


def main():
    img = [[0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1]]

    kernel = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    
    kernel = np.array(kernel, dtype = np.uint8)
    img = np.array(img, dtype = np.uint8)

    erosion = cv.erode(img, kernel, iterations=1)
    dilation = cv.dilate(img,kernel,iterations = 1)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    print(erosion, '\n')
    print(dilation, '\n')
    print(opening, '\n')
    print(closing, '\n')
main()