# coding: utf-8



from google.cloud import language  # Imported to use the google nlp api
import os
from google.cloud.language import enums
from google.cloud.language import types
import fileinput
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= r"Path of your key"
#Sets the path of the json key to the GOOGLE_APPLICATION_CREDENTIALS

client = language.LanguageServiceClient() # Creates client
temp = ''

with open(r'Path to your data') as fp:
    #remove the blank lines to avoid list out of index error
    lines= [line for line in fp.read().split("\n") if line]
    for line in lines:
        sep = ', n'
        rem = "n"+line.split(sep,1)[1]
        line = line.split(sep, 1)[0]
        #Print the intent name
        if(temp!=rem):
            print('='*20+'\n'+rem+'\n')
        document = types.Document(
            content=line,
            type=enums.Document.Type.PLAIN_TEXT)
        entities = client.analyze_entities(document).entities

        for entity in entities:
        #Print the entity name and salience
            print(entity.name,",",entity.salience,"|")

        temp = rem

