#dynamodbinfo.py

import boto3
dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-2',
            aws_access_key_id= '',
            aws_secret_access_key='')