import cv2 as cv
import argparse
import numpy as np
import time
import numpy.ma as ma

parser = argparse.ArgumentParser(description='For Thresholding Operations using inRange.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)

def find_blue():
    while True:

        ret, frame = cap.read()
        if ret == False:
            break

        height = frame.shape[0]
        width = frame.shape[1]
        total_pixles = height * width

        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        retval, frame_threshold = cv.threshold(frame,55,255, cv.THRESH_BINARY)

        hsv = cv.cvtColor(frame_threshold,cv.COLOR_BGR2HSV)
        low_rangeb = np.array([110,50,50])
        up_rangeb = np.array([130,255,255])
        maskb = cv.inRange(hsv, low_rangeb , up_rangeb)

        no_blue = cv.countNonZero(maskb)
        cv.imshow('original',frame)
        cv.imshow('mask', maskb)
        key = cv.waitKey(30)
        if( key == ord('q') or key == 27):
            break

def find_red():
    while True:

        ret, frame = cap.read()
        if ret == False:
            break

        height = frame.shape[0]
        width = frame.shape[1]
        total_pixles = height * width
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        retval, frame_threshold = cv.threshold(frame,55,255, cv.THRESH_BINARY)

        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        low_ranger = np.array([169,100,100])
        up_ranger = np.array([189,255,255])
        maskr = cv.inRange(hsv , low_ranger , up_ranger)

        no_red = cv.countNonZero(maskr)
        cv.imshow('original',frame)
        cv.imshow('mask', maskr)
        key = cv.waitKey(30)
        if( key == ord('q') or key == 27):
            break


def main():
        #gaus = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
        #call functions to find the particular colour
        print("Select Colour \n 1.Blue \n 2.Red \n 3.Green")

        Option= int(input())

        if(Option == 1):

            find_blue()

        elif(Option == 2):

            find_red()

        else:
            print(Option)
            print("Wrong Option")
            exit(0)

main()
cv.destroyAllWindows()
