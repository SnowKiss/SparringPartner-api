import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')

    body = json.loads(event['body'])
    username = body['username']
    profile_info = body['profile_info']  # e.g., skill level, weight, etc.

    response = table.update_item(
        Key={'UserId': username},
        UpdateExpression='SET profile_info = :val1',
        ExpressionAttributeValues={':val1': profile_info}
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Profile updated successfully!')
    }
