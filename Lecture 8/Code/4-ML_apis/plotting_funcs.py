"""
Source:
https://stackoverflow.com/questions/37435369/matplotlib-how-to-draw-a-rectangle-on-image
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np


def plot_box(img_path, x, y, x_diff, y_diff):
    im = np.array(Image.open(img_path), dtype=np.uint8)

    # Create figure and axes
    fig, ax = plt.subplots(1)

    # Display the image
    ax.imshow(im)

    # Create a Rectangle patch
    rect = patches.Rectangle((x, y), x_diff, y_diff,
                             linewidth=3,
                             edgecolor='r',
                             facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    plt.show()
