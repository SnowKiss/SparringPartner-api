import json
import boto3

def lambda_handler(event, context):
    body = json.loads(event['body'])
    username = body['username']
    password = body['password']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    response = table.get_item(Key={'UserId': username})

    # Ajoutez des logs pour le débogage
    print("Response from DynamoDB:", response)

    stored_password = response['Item'].get('Password') if 'Item' in response else None

    if stored_password and password == stored_password:
        return {
            'statusCode': 200,
            'body': json.dumps('Authentification réussie.')
        }
    else:
        # Log pour comprendre l'échec
        print("Échec de l'authentification. Utilisateur trouvé:", 'Item' in response, "Mot de passe correspond:", password == stored_password)
        return {
            'statusCode': 401,
            'body': json.dumps('Échec de l\'authentification.')
        }

