# NaturalLanguageProcessing usingGoogleAPI and DialogFlow
Natural Language Processing and Intent Classification Using Google Cloud APIs

This project is composed of 2 parts:
1)	Natural Language Processing using Google APIs
2)	Intent Classification using Google APIs

Part 1: Natural Language Processing
The objective is to process a set of statements, and collect all the entities from calling a specific google API. The input data set looks like this (you can find the entire data set in the attached data file IntentPhrase.data):
------------------------------------------------------------------------------------------------------------------------------------------
Please email our proof of No Claims Discount on the car we have insured with you as we need proof of NCD to enable us to insure our new Motorhome with the Caravan and Motorhome club., ncd_proof
Hey I would like to request my NCD proof. I have cancelled my insurance and yet I have not received my NCD proof which I need for my new insurance. Pleas could you send it to me as soon as possible., ncd_proof
I thought my NCD was X years it appears to be Y years, is that a problem?, ncd_change_years
I put in X years NCD and it's actually Y...How can I change the quote etc please?, ncd_change_years
------------------------------------------------------------------------------------------------------------------------------------------
The last term after the comma is simply a naming convention for the categorization of the data set. It should be removed before calling the google API, but it is supposed to be used in the collected output, which should go into a file. The output is supposed to look like this (for the data set above):
------------------------------------------------------------------------------------------------------------------------------------------
, ncd_proof
proof,0.394|No Claims Discount,0.142|Motorhome,0.135|car,0.097|proof,0.088|NCD,0.054|club,0.048|Caravan,0.041
proof,0.740|NCD,0.146|insurance,0.072|insurance,0.022|Pleas,0.019
, ncd_change_years
NCD,0.880|problem,0.120
NCD,0.552|quote,0.448
------------------------------------------------------------------------------------------------------------------------------------------
Step 1) Go to google site and create a free trial account:
https://cloud.google.com/natural-language/
Step 2) Look at the documentation and create a program (use the language of your choice) to process every line from the data set file (from the attached data file IntentPhrase.data), and call the “entities” API to output the entities and their salient values for each line processed.
Step 3) The output should have a line for the naming convention term for the set that is being processed (the term after the comma, see above), followed by the entities and salient values for every line processed. When the code processes a line which has a new naming convention term, it needs to output that term first, followed by the next line with the entities and salient values. The current naming convention term is only written once in the output file.

Part 2: Intent Classification
The objective of this project is to create a google agent and train it with part of the data set in the attached data file IntentPhrase.data, and then process all statements, and capture the output for the intent, to make sure it matched correctly or not.
Step 1) Got to google DialogFlow and click on the “Sign up for Free” button and connect to the same account you used for the NLP project.
https://dialogflow.com/
Step 2) Using UI console, create an agent.
Step 3) Create a program using the APIs and the data set in the attached file IntentPhrases.data, to create intents and to add training phrases (no more than 5) for each intent. If you look at the data set, there are groupings of phrases for each intent, and each grouping is separated by a blank line. The unique term at the end of every phrase, after the comma, is the intent name to be used in the intent creation.
It might be a good idea to create at least one intent via the UI, with some training phrases, and use the GET API to retrieve so you can have an idea how the json intent object is populated. Use the first grouping in the data set, the “ncd_proof” one.
Step 4) Create another program to use the API and send all the phrases to the agent, capturing the results into a file (I’ll let you pick what you think are relevant data points to write to the file), and at the end a summary to total success and failure phrases, and also with a breakdown by intents.




