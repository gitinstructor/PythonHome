# Full Scanning
import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')

results = table.scan()
#print(type(results))  #dict
#print(results.keys()) 'Items', 'Count', 'ScannedCount', 'ResponseMetadata'
#print(results['Count'], results['ScannedCount'])
items = results['Items']
for i in range(len(items)) :
    print(items[i])