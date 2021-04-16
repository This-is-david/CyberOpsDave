#AWS-LAMBDA_Notification_with_Filename.py

import json
import boto3
sns_cli = boto3.client("sns")


def lambda_handler(event, context):
    #Send_Update()
    #Loops through every file uploaded
    for record in event['Records']:
        #pull the body out & json load it
        jsonmaybe=(record["body"])
        jsonmaybe=json.loads(jsonmaybe)
        
        #now the normal stuff works
        bucket_name = jsonmaybe["Records"][0]["s3"]["bucket"]["name"]
        print(bucket_name)
        key=jsonmaybe["Records"][0]["s3"]["object"]["key"]
        print(key)
        Send_Update(bucket_name,key)
        
def Send_Update(sub,msg):
    #tarn = EnvMeta['topicarn']
    #msg = 'Hello From Lambda'
    #sub = 'Subject From Lambda'
    response = sns_cli.publish(
        TopicArn='arn:aws:sns:us-east-1:333896066730:ur-project-sns',
        Message=json.dumps(msg),
        Subject=sub,
        MessageStructure='string',
        MessageAttributes={
            'summary': {
                'StringValue': 'just a summary',
                'DataType': 'String'
            }
          }
    )
    return
