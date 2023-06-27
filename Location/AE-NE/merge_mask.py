# this program loads all masks in the results folder and then merges them into one mask

import cv2
import numpy as np
import os

# load all masks
masks = []
for file in os.listdir('results'):
    if file.endswith('.png'):
        masks.append(cv2.imread('results/' + file, 0))

# merge masks
mask = np.zeros(masks[0].shape)
for m in masks:
    mask = np.maximum(mask, m)

# save merged mask
cv2.imwrite('merged_mask.png', mask)