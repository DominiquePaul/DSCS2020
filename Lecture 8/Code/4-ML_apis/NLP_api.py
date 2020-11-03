"""
Make sure the google cloud and google cloud language pip packages are installed:

pip install google-cloud
pip install google-cloud-language



Parts of this code are from the Google API github repository:
https://github.com/googleapis/python-language/blob/master/samples/snippets/sentiment/sentiment_analysis.py
https://cloud.google.com/natural-language/docs/basics

You can read up on how to interpret the responses here:
https://cloud.google.com/natural-language/docs/basics
"""

import os
from google.cloud import language_v1

# Replace this with your credentials path. The LanguageServiceClient will look
# for credentials in the environment
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp_credentials/dscs2020-b20a630b58a2.json"


### Data

# Today is the US election day so lets use some tweets from the candidates for analsis

# Trump
# Source: https://twitter.com/realDonaldTrump/status/1323381654451376133
trump1 = "For years you had a President who apologized for America – now you have a President who is standing up for America, and standing up for PENNSYLVANIA. Tomorrow, you have the power, with your vote, to save AMERICA! GET OUT AND VOTE!!"
trump2 = "¡Mi AmericanDreamPlan es una promesa para los hispanoamericanos de impulsar una economía próspera, proveer oportunidades de educación para todos, preservar la libertad y apoyar la fe, la familia y la comunidad!"

# Biden
# Source: https://twitter.com/JoeBiden/status/1323354189876125696
biden = "I have always believed you can define America in one word: possibilities. And I refuse to postpone those possibilities any longer. There is so much we can achieve as a nation with Donald Trump out of the White House."

# source: https://www.galaxus.ch/de/s1/product/apple-iphone-11-128gb-black-610-sim-esim-12mpx-4g-mobiltelefon-11872363
galaxus = 'Unbrauchbarer Extender da die MAC-Adressen vom EX6120 dynamisch vergeben werden und damit eine DDNS routing verunmöglicht, weil beim nächsten Neustart wieder andere MACs vergeben werden. Ich bin ziemlich verärgert; hätte so einen Schrott von Netgear nicht erwartet!'

# source: https://fr.tripadvisor.ch/Attraction_Review-g187147-d189284-Reviews-Montmartre-Paris_Ile_de_France.html
tripadvisor = "Très sympathique avec une vue magnifique sur tout Paris. L’intérieur est magnifique avec des vitraux époustouflants. Un lieu incontournable si on vient visiter Paris."


### Sentiment

client = language_v1.LanguageServiceClient()

# this creates an object that the language client requires as an input
document = language_v1.Document(content=biden, type_=language_v1.Document.Type.PLAIN_TEXT)

sentiment = client.analyze_sentiment(request={'document': document})

print(sentiment)

# as a function

def analyse_sentiment(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    result = client.analyze_sentiment(request={'document': document})

    text_sentiment = round(result.document_sentiment.score, 2)
    sentiment_magnitude = round(result.document_sentiment.magnitude, 2)
    language = result.language

    return text_sentiment, sentiment_magnitude, language


for text in [trump1, trump2, biden, galaxus, tripadvisor]:
    sent, mag, lang = analyse_sentiment(text)
    print(f"The text has a overall sentiment of {sent} with a magnitude of {mag}. Language: {lang}")


### Entities

client = language_v1.LanguageServiceClient()

document = language_v1.Document(content=biden, type_=language_v1.Document.Type.PLAIN_TEXT)

annotations = client.analyze_entities(request={'document': document})

print(annotations)




# Syntax

client = language_v1.LanguageServiceClient()

document = language_v1.Document(content=tripadvisor, type_=language_v1.Document.Type.PLAIN_TEXT)

response = client.analyze_syntax(request = {'document': document})

# Loop through tokens returned from the API
for token in response.tokens:
    # Get the text content of this token. Usually a word or punctuation.
    text = token.text
    print(u"Token text: {}".format(text.content))
    # Get the part of speech information for this token.
    # Parts of spech are as defined in:
    # http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf
    part_of_speech = token.part_of_speech
    # Get the tag, e.g. NOUN, ADJ for Adjective, et al.
    print(
        u"Part of Speech tag: {}".format(
            language_v1.PartOfSpeech.Tag(part_of_speech.tag).name
        )
    )
    # Get the voice, e.g. ACTIVE or PASSIVE
    print(u"Voice: {}".format(language_v1.PartOfSpeech.Voice(part_of_speech.voice).name))
    # Get the tense, e.g. PAST, FUTURE, PRESENT, et al.
    print(u"Tense: {}".format(language_v1.PartOfSpeech.Tense(part_of_speech.tense).name))
    # See API reference for additional Part of Speech information available
    # Get the lemma of the token. Wikipedia lemma description
    # https://en.wikipedia.org/wiki/Lemma_(morphology)
    print(u"Lemma: {}".format(token.lemma))
    # Get the dependency tree parse information for this token.
    # For more information on dependency labels:
    # http://www.aclweb.org/anthology/P13-2017
    dependency_edge = token.dependency_edge
    print(u"Head token index: {}".format(dependency_edge.head_token_index))
    print(
        u"Label: {}".format(language_v1.DependencyEdge.Label(dependency_edge.label).name)
    )

    print("")
