import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')
table.delete()