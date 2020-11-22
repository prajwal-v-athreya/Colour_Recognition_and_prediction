import cv2 as cv
import argparse
import numpy as np
import time
import numpy.ma as ma

parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)

def main():

    while True:

        ret, frame = cap.read()
        if ret == False:
            break

        height = frame.shape[0]
        width = frame.shape[1]
        total_pixles = height * width


        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        retval, frame_threshold = cv.threshold(frame,55,255, cv.THRESH_BINARY)
        #gaus = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
        hsv = cv.cvtColor(frame_threshold,cv.COLOR_BGR2HSV)
        low_rangeb = np.array([110,50,50])
        up_rangeb = np.array([130,255,255])
        maskb = cv.inRange(hsv, low_rangeb , up_rangeb)
        '''
        BLUE_MIN = np.array([200, 0, 0], np.uint8)
        BLUE_MAX = np.array([255, 50, 50], np.uint8)
        dst = cv.inRange(frame, BLUE_MIN, BLUE_MAX)
        '''
        no_blue = cv.countNonZero(maskb)

        #call functions to find the particular colour

        cv.imshow('original',frame)
        cv.imshow('mask', maskb)

        key = cv.waitKey(30)
        if( key == ord('q') or key == 27):
            break
main()
cv.destroyAllWindows()
