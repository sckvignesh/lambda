import boto3

client = boto3.client('sns')


def lambda_handler(event, context):
    topic_arn = 'arn:aws:sns:ap-south-1:456642401593:Production-alerts'
    message = 'Hey!!! Your production server id={} is down, Please look into it'
    client.publish(TopicArn=topic_arn, Message=message, Subject='P1:CRITICAL-EC2 SERVER STOPPED')

'''
- send an email with message and subject
- Need to send the email with instance id.
'''