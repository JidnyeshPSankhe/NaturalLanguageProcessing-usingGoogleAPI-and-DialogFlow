
# coding: utf-8

import dialogflow
import os
#Replace the path with you json key path
os.environ["Path to your json key"
#Replace with you project id
project_id = 'project-id'

#Created to append 5 lines of each intent as its training phrase
def five_lines():
    temp=''
    fp= open(r'PAth to your data file')
    #remove the blank lines to avoid list out of index error
    lines= [line for line in fp.read().split("\n") if line]
    sep = ', n'
    temp=''
    for i in range(len(lines)):
        display_name = "n"+lines[i].split(sep,1)[1]
        if(temp!=display_name):
            head = [lines[i],lines[i+1],lines[i+2],lines[i+3],lines[i+4]]
            for line in head:
                training_phrases_parts.append(line.split(sep, 1)[0])
            create_intent(project_id, display_name, training_phrases_parts)
            del training_phrases_parts[:]
        temp = display_name
        
def create_intent(project_id, display_name, training_phrases_parts):
        intents_client = dialogflow.IntentsClient()
        message_texts=''
        parent = intents_client.project_agent_path(project_id)
        training_phrases = []
        for training_phrases_part in training_phrases_parts:
            part = dialogflow.types.Intent.TrainingPhrase.Part(
                text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
            training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)

        text = dialogflow.types.Intent.Message.Text(text=message_texts)
        message = dialogflow.types.Intent.Message(text=text)

        intent = dialogflow.types.Intent(
            display_name=display_name,
            training_phrases=training_phrases)

        response = intents_client.create_intent(parent, intent)

        print('Intent created: {}'.format(response))

five_lines()
    

