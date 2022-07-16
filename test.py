import cv2


def hu_moment(img):
    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('origina', im)
    cv2.waitKey(0)

    moments = cv2.moments(im)
    huMoments = cv2.HuMoments(moments)

    return moments, huMoments


def is_shape(original_img, expected_img):
    return cv2.matchShapes(original_img, expected_img, cv2.CONTOURS_MATCH_I1, 0)


img = cv2.imread('assets/shapes/4.png')
im2 = cv2.imread('assets/shapes/4.1.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im22 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
print(is_shape(im22, img2))
moments, huMoments = hu_moment(img)
_, humoments2 = hu_moment(im2)

[print(f'{huMoments[i]} {humoments2[i]}') for i in range(7)]
print(moments)
