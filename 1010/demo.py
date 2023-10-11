import boto3

resource = boto3.resource("dynamodb", region_name='ap-northeast-2',
               aws_access_key_id='',
               aws_secret_access_key='')

client = boto3.client('dynamodb')
#print(client.list_tables())
#print(resource)
# table = client.describe_table(
#     TableName = 'lab-movie'
# )
# print(table)
table = resource.Table('lab-movie')
item = {
    'Code' : '19780080',
    'Name' : 'Star Wars',
    'Genre' : 'SF',
    'Date' : '1978-04-12',
    'Director' : 'George Lucas',
    'Actor' : '마크 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
}
table.put_item(Item=item)
