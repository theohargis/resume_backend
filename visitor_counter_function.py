import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    
    # connect to DynamoDB resource
    client = boto3.resource('dynamodb')
    
    # create dynamodb client to visitor_count table
    table = client.Table('visitor_count')
    
    # increment visitor_count for index.html
    response = table.update_item(
        Key = { 'path': 'index.html'
        }, 
        AttributeUpdates = {
            'visitor_count': {
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    
    # get visitor_count from visitor_count table for index.html
    response = table.get_item(
        Key = {
            'path': 'index.html'
        }
    )
    visitor_count = response['Item']['visitor_count']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
