import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img1 = cv.imread('images/img2_2.png')
img2 = cv.imread('images/img2_1.png')

gray= cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
gray1 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(gray,None)
kp2, des2 = orb.detectAndCompute(gray1,None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

matches = sorted(matches, key = lambda x:x.distance)

img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3)
plt.show()

img1_pts = []
img2_pts = []
for mat in matches[:4]:
    img1_idx = mat.queryIdx
    img2_idx = mat.trainIdx
    (x1, y1) = kp1[img1_idx].pt
    (x2, y2) = kp2[img2_idx].pt

    # Append to each list
    img1_pts.append([x1, y1])
    img2_pts.append([x2, y2])
#print(img1_pts)
h, status = cv.findHomography(np.float32(img1_pts), np.float32(img2_pts))

img4 = cv.warpPerspective(img1,h,(img1.shape[1]+ img2.shape[1], img1.shape[0] +2))
img4[0:img2.shape[0], 0:img2.shape[1]] = img2
img4= cv.cvtColor(img4,cv.COLOR_BGR2RGB)
plt.imshow(img4)
plt.show()

