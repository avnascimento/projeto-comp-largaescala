import json
import sys
import requests

def lambda_handler(event, context):
    data = event['data']

    #original string
    print ("The original string is : " + data)
    # using split() function
    res = len(data.split())
    
    return {
        'statusCode': 200,
        'body': str(res)
    }
