import json
import sys
import requests

def lambda_handler(event, context):
    miles = event['miles']
    km = miles / 0.62137  
    
    return {
        'statusCode': 200,
        'body': str(km)
    }
