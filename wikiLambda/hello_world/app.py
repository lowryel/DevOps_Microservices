import json
import wikipedia

# prints when function loads
print('Loading wikipedia summarizer function')


def lambda_handler(event, context):
    ''' Wikipedia page summarizer.
        :param event: a request with a wikipedia "entity" that has page information
        :return: a response that contains the first sentence of a wikipedia page,
            the response is JSON formatted.'''
    
    ## TO DO: Check that the request has some input body and save it
    if 'body' in event:
        body = json.loads(event["body"])
    
    ## TO DO: Get the wikipedia "entity" from the body of the request
    entity = event["entity"]
    try:
        res = wikipedia.summary(entity, sentences=1) # first sentence, result
        statusCode=200
    except wikipedia.exceptions.PageError:
        statusCode=400
        res="\nText does not exist\n"
    except wikipedia.exceptions.DisambiguationError:
        statusCode=400
        res="\nThere are multiple reference to this word!\n"
    except:
        res="\nNo context\n"

    # print statements
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    ## TO DO: Format the response as JSON and return the result
    response = {
        ## your code here
        "statusCode":statusCode,
        "hearders":{"Content-type": "application/json"},
        "body":json.dumps({"message":res})
    }
    
    return response
