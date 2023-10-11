import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')
table.delete_item(
    Key={
        'Code' : '20050112',
        'Name' : 'Batman Begins'
    }
)