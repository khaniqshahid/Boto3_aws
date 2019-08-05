import boto3

# s3_ob=boto3.resource('s3', aws_access_key_id="AKIAJO53UHGYI6A7N4CQ",aws_secret_access_key="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")
# for each_b in s3_ob.buckets.all():
#     print(each_b.name)
#     #print(each_b)
#
#



#ec2=boto3.resource('ec2', aws_access_key_id="AKIAJO53UHGYI6A7N4CQ",aws_secret_access_key="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",region_name="eu-west-1")

ec2=boto3.resource('ec2', aws_access_key_id="AKIAJO53UHGYI6A7N4CQ",aws_secret_access_key="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",region_name="eu-west-1")

"""

#ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])

"""

def lambda_handler():
    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)

    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print(instance.id)


lambda_handler()
