import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB,0)

# plt.subplot(1,2,1)
# plt.imshow(img)
# plt.title('Images BGR')
# # plt.xticks([])
# # plt.yticks([])

# plt.subplot(1,2,2)
# plt.imshow(img2)
# plt.title('Images RGB')
# # plt.xticks([])
# # plt.yticks([])

# plt.show()

title = ['Image BGR','Image RGB']
images = [img,img2]

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(title[i])

plt.show()



