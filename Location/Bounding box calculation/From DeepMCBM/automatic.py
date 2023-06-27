import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import sys

def update_figure(i):
    # setting values to rows and column variables
    rows = 3
    columns = 3

    # reading images
    Image1 = cv2.imread(dataset_path + '/' + images[i])
    Image2 = cv2.imread(background_path + '/' + backgrounds[i])
    Image3 = cv2.imread(output_path + '/' + results[i])

    # only shows previous image if it exists
    if i > 0:
        previous_image = cv2.imread(dataset_path + '/' + images[i-1])
    else: #show black
        previous_image = np.zeros_like(Image1)
    # only shows next image if it exists 
    if i < images_size - 1:
        next_image = cv2.imread(dataset_path + '/' + images[i+1])
    else: #show black
        next_image = np.zeros_like(Image1)

    # calculate cumulative sum of masks
    global cumulative_sum
    if i == 0:
        #initialize as completely black
        cumulative_sum = np.zeros_like(Image3)
    else:
        
        #the areas in the mask that are white gets copied to a new image but instead of being white (255) they are 1

        #select the white parts of the mask
        mask_indices = np.where(Image3 > 0)

        #create an empty image with the same size and shape as the input image
        mask = np.zeros_like(Image3)

        #set the white parts of the mask to 1
        mask[mask_indices[0], mask_indices[1], 0] = 2
        mask[mask_indices[0], mask_indices[1], 1] = 2
        mask[mask_indices[0], mask_indices[1], 2] = 2

        #add the mask to the cumulative sum
        #but if an area is already white (255) in the cumulative sum, it will not be added again
        cumulative_sum = cv2.add(cumulative_sum, mask)

        #if an area in the cumulative sum is > 255, it will be set to 255
        cumulative_sum = np.where(cumulative_sum > 255, 255, cumulative_sum)

        #print the max vallue achieved in the cumulative sum
        #np.max(cumulative_sum)
        
        #cumulative_sum += Image3

    # save cumulative sum to file
    cv2.imwrite('cumulative_sum.png', cumulative_sum)

    # clear figure
    fig.clear()

    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, 5)

    # create an empty image with the same size and shape as the input image
    masked_image = np.zeros_like(Image1)

    # select the white parts of the mask
    mask_indices = np.where(Image3 > 0)

    # set the blue channel of the masked image to 255 at the white mask indices
    masked_image[mask_indices[0], mask_indices[1], 0] = 255

    # set the green and red channels of the masked image to the corresponding values from the input image
    masked_image[:,:,1] = Image1[:,:,1]
    masked_image[:,:,2] = Image1[:,:,2]


    # display the masked image
    plt.imshow(masked_image)
    plt.axis('off')
    plt.title("Masked Image")

    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, 2)

    # showing image
    plt.imshow(Image2)
    plt.axis('off')
    plt.title("Background")

    # Adds a subplot at the 4th position
    fig.add_subplot(rows, columns, 8)

    # showing image
    plt.imshow(cumulative_sum)
    plt.axis('off')
    plt.title("Cumulative Sum - Max val: " + str(np.max(cumulative_sum)))

    fig.add_subplot(rows, columns, 4)

    # showing image
    plt.imshow(previous_image)
    plt.axis('off')
    plt.title("Previous image")

    fig.add_subplot(rows, columns, 6)

    # showing image
    plt.imshow(next_image)
    plt.axis('off')
    plt.title("Next image")

# main that receives the path to the dataset, the path to the background images and the path to the output images
if __name__ == "__main__":
    print("Running automatic.py")
    
    dataset_path = sys.argv[1] #dataset_path = 'mdsn_no_p/input'
    background_path = sys.argv[2] #background_path = 'backgrounds'
    output_path = sys.argv[3] #output_path = 'results'

    #list of all images
    images = os.listdir(dataset_path)
    backgrounds = os.listdir(background_path)
    results = os.listdir(output_path)

    #sort images
    images.sort()
    backgrounds.sort()
    results.sort()

    images_size = len(images)
    backgrounds_size = len(backgrounds)
    results_size = len(results)

    # create figure
    fig = plt.figure(figsize=(10, 7))

    # initialize cumulative sum variable
    cumulative_sum = None

    # create animation
    anim = animation.FuncAnimation(fig, update_figure, frames=images_size, repeat=False)

    # show animation
    plt.show()