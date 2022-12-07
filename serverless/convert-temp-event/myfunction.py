import json
import sys
import requests

def lambda_handler(event, context):
    temp = event['temp']
    fahrenheit = (temp * 1.8) + 32
    
    return {
        'statusCode': 200,
        'body': str(fahrenheit)
    }
