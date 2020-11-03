"""
Make sure to install the automl python package

    pip install google-cloud-automl
"""
import os
from google.cloud import automl


project_id = "dscs2020"
model_id = "ICN5998708941750534144"
file_path = "../../Images/test_bananas/banana1.jpg"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp_credentials/dscs2020-b20a630b58a2.json"

os.getcwdb()

prediction_client = automl.PredictionServiceClient()


# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path(
    project_id, "us-central1", model_id
)


# Read the file.
with open(file_path, "rb") as content_file:
    content = content_file.read()


image = automl.Image(image_bytes=content)
payload = automl.ExamplePayload(image=image)


request = automl.PredictRequest(
    name=model_full_id,
    payload=payload
)
response = prediction_client.predict(request=request)

print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {}".format(result.classification.score))
