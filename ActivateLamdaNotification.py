import boto3
import json



client = boto3.client(
    service_name='ses',
    aws_access_key_id='AKIAJO53UHGYI6A7N4CQ',
    aws_secret_access_key='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',
    region_name='eu-west-1'
)

response = client.send_email(
    Destination={
        #'ToAddresses': ['recipient1@domain.com', 'recipient2@domain.com],
        'ToAddresses': ['shahid.iqbal.khan@ericsson.com', 'omer9992001@gmail.com'],
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
    Source='omer9992001@gmail.com',
)
