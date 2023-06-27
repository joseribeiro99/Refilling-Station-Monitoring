#this code iterates in the mdsn/input folder.
#checks if each image has a person in it.
#if it has a person, it removes the image from the folder.
#to check if an image has a person, it uses a pre-trained model from yolov5.

# Note that the model can detect more classes than person, but we only care about person

import torch
import torch
from IPython.display import clear_output
import os

# Load the model from torch.hub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def check_image(image):
    # Inference, run the model on the 2 foreground images
    results = model(image, size=640)
    clear_output()

    # Print out a summary of the inference job, we ran it on 2 images, at what speed and what detections were made
    results.print()

    # Convert the above to a string
    results_print = str(results)

    #This returns -1 if theres no person in the image
    print(results_print.find('person'))

    if results_print.find('person') == -1:
        print("no person in image")
    else:
        print("person in image")
        os.remove(image)

path = "mdsn/input"

#iterate in the folder
for filename in os.listdir(path):
    check_image(path + "/" + filename)