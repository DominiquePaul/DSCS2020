"""
This code is based on a tutorial by GCP:
https://www.youtube.com/watch?v=kgxfdTh9lz0

The specific code can be found here:
https://gist.github.com/yufengg/984ed8c02d95ce7e95e1c39da906ee04
"""

import os
import pandas as pd

path1 = "../Images/yellow"
path2 = "../Images/green"

data_folders = [path1, path2]
label_names = ["yellow", "green"]

filenames = [os.listdir(f) for f in data_folders]
[print(f[1]) for f in filenames]
[len(f) for f in filenames]

files_dict = dict(zip(label_names, filenames))
files_dict

data_array = []
base_gcs_path = "gs://example_bananas_dscs/"

for label, list in files_dict.items():
    for filename in list:
        file_path_gcs = base_gcs_path + label + "/" + filename
        data_array.append((file_path_gcs, label))


dataframe = pd.DataFrame(data_array)
dataframe.to_csv('../Images/image_mapping.csv', index=False, header=False)
