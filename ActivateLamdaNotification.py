import boto3
import json



client = boto3.client(
    service_name='ses',
    aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
    aws_secret_access_key='xxxxxxxxxxxxxxxxLZ5Sxxxxxxxxxxxx',
    region_name='eu-west-1'
)

response = client.send_email(
    Destination={
        #'ToAddresses': ['recipient1@domain.com', 'recipient2@domain.com],
        'ToAddresses': ['shahidkhan@dublin.com'],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'MESSAGE FROM BOTO3 LINUX',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'BOTO3 subject string',
        },
    },
    Source='shahidkhan@dublin.com',
)
