import os
import requests

ACCESS_KEY = os.environ["UNSPLASH_API_KEY"]


def get_city_img_link(query_name):
    endpoint = "https://api.unsplash.com/search/photos"
    parameters = {"client_id": ACCESS_KEY,
                  "query": query_name}

    r = requests.get(endpoint, params=parameters)
    data = r.json()
    image_url = data["results"][0]["urls"]["full"]

    return image_url


def write_img_to_disk(img_url, folder_prefix, filename):

    img = requests.get(img_url)

    file_path = os.path.join(folder_prefix, filename)

    with open(file_path, "wb") as file:
        file.write(img.content)

    return file_path
