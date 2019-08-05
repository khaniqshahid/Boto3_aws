import boto3
import time
import random



initial = time.time()
session=boto3.Session(aws_access_key_id="XXXXXXXXXXXXXXXX",aws_secret_access_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",region_name="eu-west-1")

ec2_re_ob=session.resource(service_name='ec2')
ec2_cli=session.client(service_name="ec2")


def wait_ec2():

    RunningInstances = []
    #check_inst1 = 0
    while True:
        time.sleep(2)
        filters = [
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]

        # filter the instances based on filters() above
        instances = ec2_re_ob.instances.filter(Filters=filters)

        # instantiate empty array
        #check_inst = len(RunningInstances)
        for instance in instances:

            # for each instance, append to array

            RunningInstances.append(instance.id)
            check_inst = len(RunningInstances)
            print("check_inst:", check_inst)
            print("check_id:", RunningInstances)
        check_inst = len(RunningInstances)
        if int(check_inst) != 6:
            RunningInstances = []
            check_inst1 = len(RunningInstances)
        else:
            print("A")
            break
               # print("[ " + instance.id + " ]")

    print("Time in listing Instances2", time.time() - initial, "Seconds")

    # for each_in in ec2_re_ob.instances.all():
    #     print("[ "+ each_in.id + " ]")



def get_ec2_instances():
    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # filter the instances based on filters() above
    instances = ec2_re_ob.instances.filter(Filters=filters)

    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print("[ " + instance.id + " ]")
    print("Time in listing Instances", time.time() - initial, "Seconds")

    return(RunningInstances)
    # for each_in in ec2_re_ob.instances.all():
    #     print("[ "+ each_in.id + " ]")


get_ec2_instances()
wait_ec2()
