import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def create_seam(img1, img2, r):
    s = []
    for i in range(r):
        if i == 0:
            min_val = min(img2[i])
            index = np.where(img2[i] == min_val)
            index = index[0][0]
            #img[i][index] = np.array([255,0,0])
        else:
            if i == 1:
                print(index)
            if index == 0:
                if img1[i][index] < img1[i][index+1]:
                    index = index
                else:
                    index += 1
            elif index < columns -1:
                min_val = min(img2[i][index-1], img2[i][index], img2[i][index+1])
                if img2[i][index - 1] == min_val:
                    index = index -1
                elif img2[i][index] == min_val:
                    index = index
                else:
                    index = index + 1
            else:
                if img1[i][index] < img1[i][index-1]:
                    index = index
                else:
                    index -= 1
            #img[i][index] = np.array([255,0,0])
        s.append((i,index))
    return s

def create_mat(img1,columns,rows):
    img2 = np.copy(img1)

    for j in range(columns):
        img2[rows - 1][j] = img1[rows - 1][j]


    for i in range(rows-2,-1,-1):
        for j in range(columns):
            if j == 0:
                img2[i][j] = img1[i][j] + min(img2[i+1][j], img2[i+1][j+1])
            elif j == columns -1:
                img2[i][j] = img1[i][j] + min(img2[i+1][j], img2[i+1][j-1])
            else:
                img2[i][j] = img1[i][j] + min(img2[i-1][j], img2[i+1][j], img2[i+1][j+1])
    return img2

filename = 'images/tower.jpg'
img = cv.imread(filename)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
rows, columns = gray.shape
print(rows, columns)

img1 = np.copy(gray)
img2 = np.copy(gray)

# Calcution of Sobelx
sobelx = cv.Sobel(gray,cv.CV_64F,1,0,ksize=5)
    
# Calculation of Sobely
sobely = cv.Sobel(gray,cv.CV_64F,0,1,ksize=5)

img1 = (sobelx)*(sobelx) + (sobely)*(sobely)
img1 = np.sqrt(img1)

plt.imshow(img1, cmap = 'gray')
plt.show()

#Calculating dp matrix in img2


seams = 10
seam = []
index = 0
c = columns
for s in range(seams):
    img2 = create_mat(img1,c,rows)
    seam = create_seam(img1,img2,rows)
    for k in range(len(seam)):
        x = seam[k][0]
        y = seam[k][1]
        img[x][y] = np.array([255,0,255])
        #print(x, k)
    #rearrange img2
        arr1 = np.array(img1[x][:y])
        arr2 = np.array(img1[x][y+1:])
        img1[x] = np.concatenate((arr1,arr2,[0]))
    img1.resize((rows,c-1), refcheck = False)
    c-=1

plt.imshow(img)
plt.show()


