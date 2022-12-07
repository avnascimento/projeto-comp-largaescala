import json
import sys
import requests

def lambda_handler(event, context):
    pounds = event['data']
    kilo_grams = pounds * 0.453592

    return {
        'statusCode': 200,
        'body': str(kilo_grams)
    }
