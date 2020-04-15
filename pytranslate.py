# Author: Karan Goda

# A txt file translator into the desired language
# The user specifies the file paths and target language in the CLI

import sys
import os

from google.cloud import translate_v2
from google.cloud import translate_v2 as translate

# Resources used
# https://www.youtube.com/watch?v=YapTts_An9A
# https://cloud.google.com/translate/docs/
# https://cloud.google.com/translate/docs/basic/setup-basic
# https://cloud.google.com/translate/automl/pricing
# https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv
# https://cloud.google.com/natural-language/docs/quickstart-client-libraries

"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""

# You need to specify file path of the JSON Google Credentials in Command line
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = input("Type in file path of JSON key: \n")

translate_client = translate.Client()

print('\nSupported languages: https://cloud.google.com/translate/docs/languages' + '\n')

# User inputs target language otherwise default english
target = input("Type in the ISO-639-1 Code of target translation language: \n")
print('\n')

# You need to specify file path of the Files to read and write in Command line
# File to read from
fileToRead = input("Type in file path of source text file eg '~/Desktop/srcFileName.txt':\n")
print('\n')
f1 = open(fileToRead, "r")

# File to write in
filePathToWriteIn = input("Type in file path for translation result eg: '~/Desktop/targetFileName.txt':\n")
print('\n')
f2 = open(filePathToWriteIn,"w+")

for line in f1:
    output = translate_client.translate(
        line,
        target_language = target
    )

    # Get the translated line without the dict part
    translatedText = output.get('translatedText')

    # Stores translated line in another txt file
    f2.write(translatedText + '\n')

f1.close()
f2.close()