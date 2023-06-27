#opens the costruction_bk/input folder
#shuffles the images b changing their names
#this script will run on linux

import os
import random

#path to the folder with images
path = 'mds/input'

#list of all images
images = os.listdir(path)

#shuffle images
random.shuffle(images)

#rename images
for i, image in enumerate(images):
    os.rename(os.path.join(path, image), os.path.join(path, str(i) + '.jpg'))