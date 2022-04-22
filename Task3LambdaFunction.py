import json
import boto3

def lambda_handler(event, context):
    
    #Taking body of the SQS message from event
    body =json.dumps(event["Records"][0]["body"])
    
    # Taking Id & message from body
    b=body.replace("\"","")
    msg =b.split(" : ")
    Id= int(msg[0])
    m= msg[1]
    message={"Id": Id,"Message": m} 
    print(message)
    #INserting into table
    dynamoDB=boto3.resource('dynamodb')
    table=dynamoDB.Table('BootcampT3-DyDB-tbl')
    table.put_item(Item=message)
    return "Inserted"
