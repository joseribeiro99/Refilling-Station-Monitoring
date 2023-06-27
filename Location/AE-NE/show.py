import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

dataset_path = 'mdsn_no_p/input'
background_path = 'backgrounds'
output_path = 'results'

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

# define update_figure function
# define update_figure function
# define update_figure function
def update_figure(i):
    # setting values to rows and column variables
    rows = 2
    columns = 2

    # reading images
    Image1 = cv2.imread(dataset_path + '/' + images[i])
    Image2 = cv2.imread(background_path + '/' + backgrounds[i])
    Image3 = cv2.imread(output_path + '/' + results[i])

    # calculate cumulative sum of masks
    global cumulative_sum
    if i == 0:
        cumulative_sum = Image3
    else:
        cumulative_sum += Image3

    # save cumulative sum to file
    cv2.imwrite('cumulative_sum.png', cumulative_sum)

    # clear figure
    fig.clear()

    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, 1)

    # showing image
    plt.imshow(Image1)
    plt.axis('off')
    plt.title("First")

    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, 2)

    # showing image
    plt.imshow(Image2)
    plt.axis('off')
    plt.title("Second")

    # Adds a subplot at the 3rd position
    fig.add_subplot(rows, columns, 3)

    # showing image
    plt.imshow(Image3)
    plt.axis('off')
    plt.title("Third")

    # Adds a subplot at the 4th position
    fig.add_subplot(rows, columns, 4)

    # showing image
    plt.imshow(cumulative_sum)
    plt.axis('off')
    plt.title("Cumulative Sum")


# create animation
anim = animation.FuncAnimation(fig, update_figure, frames=images_size, repeat=False)

# show animation
plt.show()
