import boto3

def promail(start):
    topic_arn = 'arn:aws:sns:us-east-1:204897189983:SnsTopic'
    message = 'A new user registered with the username'
    subject = 'mail by SNS Library'
    AWS_REGION = 'us-east-1'
    sns_client = boto3.client('sns', region_name=AWS_REGION)
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject,
        )['MessageId']