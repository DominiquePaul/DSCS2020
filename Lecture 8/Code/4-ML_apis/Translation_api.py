"""
Make sure the google cloud and google cloud translate packages are installed:

pip install google-cloud
pip install google-cloud-translate

"""
import os
from google.cloud import translate_v2 as translate

# Replace this with your credentials path. The translate client will look
# for credentials in the environment
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp_credentials/dscs2020-b20a630b58a2.json"


translate_client = translate.Client()

# the text we want to translate
text = "How many screwdrivers of this kind can you deliver in the next two months?"

# the target language, must be an ISO 639-1 language code.
# See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

# examples:
target = "zh"

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
result = translate_client.translate(text, target_language=target)

print(f"Text: {result['input']}")
print(f"Translation: {result['translatedText']}")
print(f"Detected source language: {result['detectedSourceLanguage']}")



languages = ["fr", "de", "es"]

for language in languages:
    result = translate_client.translate(text, target_language=language)
    print(f"Translation: {result['translatedText']}")
