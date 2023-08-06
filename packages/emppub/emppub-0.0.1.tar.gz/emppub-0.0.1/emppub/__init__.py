import boto3

def publish(topic_arn):
    message = 'Employee has been created successfully.'
    subject = 'CRUD update.'
    AWS_REGION = 'us-east-1'
    sns_client = boto3.client('sns', region_name=AWS_REGION)
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject,
        )['MessageId']