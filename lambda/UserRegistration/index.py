import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Parse the input data
    try:
        body = json.loads(event['body'])
        username = body['username']
        password = body['password']  # Hash this password in a real application

        # Insert into DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Users')
        table.put_item(Item={'UserId': username, 'Password': password})
        return {
            'statusCode': 200,
            'body': json.dumps('User registered successfully!')
        }
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': json.dumps("Error writing to DynamoDB")
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps("Internal server error")
        }
