#opens the costruction_bk/input folder
#randomly delete 25% of the images

import os
import random
import shutil

#path to the folder with images
path = 'construction_bk/input'

#list of all images
images = os.listdir(path)

#number of images to delete
num_images = int(len(images) * 0.25)

#randomly select images to delete
images_to_delete = random.sample(images, num_images)

#delete images
for image in images_to_delete:
    os.remove(os.path.join(path, image))