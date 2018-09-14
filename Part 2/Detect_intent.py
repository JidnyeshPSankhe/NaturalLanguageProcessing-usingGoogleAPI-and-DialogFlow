
# coding: utf-8

# In[ ]:


import dialogflow
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"Path to your json key"
project_id = 'project id'
language_code= 'en-US'
session_id='session-id'
def create_texts():
    fp= open(r'Path to your data file')
    #remove the blank lines to avoid list out of index error
    lines= [line for line in fp.read().split("\n") if line]
    sep = ', n'  
    texts=[]
    input_phrases=[]
    for line in lines:
        input_phrases.append(line.split(sep, 1)[0])
        rem = "n"+line.split(sep,1)[1]
        for l in input_phrases:
            texts.append(l[0:254])
            detect_intent_texts(project_id, session_id, texts, language_code,rem)
        del input_phrases[:]
        del texts[:]
    

def detect_intent_texts(project_id, session_id, texts, language_code,rem):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    
    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Expected Intent: '+rem)
        if(response.query_result.intent.display_name!=rem):
            print('!!!!!!!!!!!!!!Wrong detection!!!!!!!!!!!!!!!!!!!!!')
create_texts()
        

