#use knn to separate image in 3 regions
#use 3 different colors to represent 3 regions

import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
import cv2

image = plt.imread('image.jpg')
plt.imshow(image)

#reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

#define stopping criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

#number of clusters (K)
k = 3
compactness,labels,centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

#convert data into 8-bit values
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]

#reshape data into the original image dimensions
segmented_image = segmented_data.reshape((image.shape))
labels_reshape = labels.reshape(image.shape[0], image.shape[1])

#show the image
plt.imshow(segmented_image)

#show the image with segmented colors
plt.imshow(labels_reshape, cmap='gray')

#save the image
#plt.imsave('segmented_image.jpg', segmented_image)