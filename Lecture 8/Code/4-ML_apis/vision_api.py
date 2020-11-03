"""
Make sure the google cloud and google cloud vision packages are installed:

pip install google-cloud
pip install google-cloud-vision
"""

import os
import io
from google.cloud import vision

from plotting_funcs import plot_box

# Replace this with your credentials path. The vision client will look
# for credentials in the environment
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp_credentials/dscs2020-b20a630b58a2.json"




###############################################################################
# Detecting text
###############################################################################


# the image we want to analyse
file_path = "./example_images/swiss_highway.png"

# open the image annotator client
client = vision.ImageAnnotatorClient()

# open the image as a bytes file
with io.open(file_path, 'rb') as image_file:
    content = image_file.read()

# load the image as a google vision object
image = vision.Image(content=content)

# search for text
response = client.text_detection(image=image)

# plot some of the texts found
texts = response.text_annotations
for text in texts:
    x = text.bounding_poly.vertices[0].x
    y = text.bounding_poly.vertices[0].y
    x_diff = text.bounding_poly.vertices[2].x  - text.bounding_poly.vertices[0].x
    y_diff = text.bounding_poly.vertices[2].y  - text.bounding_poly.vertices[0].y
    desc = text.description
    print(desc)

    plot_box(file_path, x, y, x_diff, y_diff)


###############################################################################
# Detecting landmarks
###############################################################################

def detect_landmarks(file_path):
    """Detects landmarks in the file."""

    client = vision.ImageAnnotatorClient()

    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print('Landmarks:')

    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print('Latitude {}'.format(lat_lng.latitude))
            print('Longitude {}'.format(lat_lng.longitude))


# example use case: automatically tag images by location on a travel blog website
detect_landmarks("./example_images/geneva.png")


###############################################################################
# Detecting landmarks
###############################################################################


def detect_labels(file_path):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(f"Found {label.description} with {round(label.score, 3)*100}% confidence")


detect_labels("./example_images/bmensa.jpg")
