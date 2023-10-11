import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')
# item = {
#     'Code' : '19780080', 'Name' : 'Star Wars',
#     'Genre' : 'SF', 'Date': '1978-04-12', 'Director' : 'George Lucas', 
#     'Actor' : '마크 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
# }
# table.put_item(Item=item)
item = {
     'Code' : '20050112', 'Name' : 'Batman Begins', 
     'Time' : 134, 'Genre' : '범죄, 액션, 판타지', 
     'Date' : '2005-06-24', 'Director' : '크리스토퍼 놀란',
     'Actor' : '리암 니슨, 크리스찬 베일, 마이클 케인'
 }
table.put_item(Item=item)