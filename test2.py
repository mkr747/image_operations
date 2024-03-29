from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse
import random as rng
rng.seed(12345)


def thresh_callback(val):
    threshold = val

    canny_output = cv.Canny(src_gray, threshold, threshold * 2)

    contours, _ = cv.findContours(
        canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Get the moments
    mu = [None]*len(contours)
    for i in range(len(contours)):
        mu[i] = cv.moments(contours[i])
    # Get the mass centers
    mc = [None]*len(contours)
    for i in range(len(contours)):
        # add 1e-5 to avoid division by zero
        mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5),
                 mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
    # Draw contours

    drawing = np.zeros(
        (canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv.drawContours(drawing, contours, i, color, 2)
        cv.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)

    cv.imshow('Contours', drawing)

    # Calculate the area with the moments 00 and compare with the result of the OpenCV function
    for i in range(len(contours)):
        print(' * Contour[%d] - Area (M_00) = %.2f - Area OpenCV: %.2f - Length: %.2f' %
              (i, mu[i]['m00'], cv.contourArea(contours[i]), cv.arcLength(contours[i], True)))


for a in ('assets/shapes/1.1.png', 'assets/shapes/2.1.png', 'assets/shapes/4.1.png', 'assets/shapes/5.1.png', 'assets/shapes/6.1.png', 'assets/shapes/7.1.png', 'assets/shapes/8.png'):
    print(a)
    parser = argparse.ArgumentParser(
        description='Code for Image Moments tutorial.')
    parser.add_argument('--input', help='Path to input image.',
                        default='stuff.jpg')
    args = parser.parse_args()
    src = cv.imread(a)
    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)
    # Convert image to gray and blur it
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    src_gray = cv.blur(src_gray, (3, 3))
    source_window = 'Source'
    cv.namedWindow(source_window)
    cv.imshow(source_window, src)
    max_thresh = 255
    thresh = 100  # initial threshold
    cv.createTrackbar('Canny Thresh:', source_window,
                      thresh, max_thresh, thresh_callback)
    thresh_callback(thresh)
    cv.waitKey()
