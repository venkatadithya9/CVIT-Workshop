import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/bike.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
plt.imshow(img)
plt.show()
rows, cols, color = img.shape
num = 0
new_img = np.copy(img)
for r in range(rows):
  for c in range(cols):
    col = img[r][c]
    tmp = [0,0,0]
    tmp[0] = 0.393*col[0] + 0.769*col[1] + 0.189*col[2]
    tmp[1] = 0.349*col[0] + 0.686*col[1] + 0.168*col[2]
    tmp[2] = 0.272*col[0] + 0.534*col[1] + 0.131*col[2]
    if tmp[0] > 255:
      tmp[0] = 255
    if tmp[2] > 255:
      tmp[2] = 255
    if tmp[1] > 255:
      tmp[1] = 255
    new_img[r][c] = tmp
plt.imshow(new_img)
plt.show()

tex = cv2.imread('texture2.jpg', cv2.IMREAD_UNCHANGED)
tex = cv2.cvtColor(tex, cv2.COLOR_BGR2RGB)
tex = cv2.resize(tex,(cols,rows))
print(tex.shape)
fin_img = np.copy(img)
tmp1=[0,0,0]
tmp2=[]
tmp3=[]
for r in range(rows):
  for c in range(cols):
    tmp2 = new_img[r][c]
    tmp3 = tex[r][c]
    #print(tmp3)
    for i in range(3):
      tmp1[i] = ((tmp3[i]/255)* tmp2[i])
      if tmp1[i]> 255:
        tmp1[i] = 255
    fin_img[r][c] = tmp1

plt.imshow(fin_img)
plt.show()
