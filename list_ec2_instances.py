import boto3
import pprint
import random
import time


initial = time.time()
# Following credentials can be covered up in a another hidden function or use encryption or .. Folowing is for new to understand.
session=boto3.Session(aws_access_key_id="XXXXXXXXXXXXXXXXXX",aws_secret_access_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",region_name="eu-west-1")

ec2_re_ob=session.resource(service_name='ec2')
ec2_cli=session.client(service_name="ec2")



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
   # print("Time in listing Instances", time.time() - initial, "Seconds")

    return(RunningInstances)
    # for each_in in ec2_re_ob.instances.all():
    #     print("[ "+ each_in.id + " ]")


"""
# not needed 
def get_ec2_List():
    inst_List=[]
    for each_in in ec2_re_ob.instances.all():
        inst_List.append(each_in.id)
    return(inst_List)
    #print(inst_List)
    #print(each_in.id)

#def stop_ec2():
"""
def terminate_ec2(ec2_1, ec2_2):

    #instance_2_id = ec2_re_ob.Instance(random_ec2_2).id
    #print(instance_2_id)
    ec2_re_ob.Instance(ec2_1).terminate()
    ec2_re_ob.Instance(ec2_2).terminate()
    # ec2_re_ob.instances.filter(InstanceIds=ec2_1).terminate()
    # ec2_re_ob.instances.filter(InstanceIds=ec2_2).terminate()


def state_ec2(ec2_1, ec2_2):

    instance_1_state = ec2_re_ob.Instance(ec2_1).state['Name']
    instance_2_state = ec2_re_ob.Instance(ec2_2).state['Name']
    print(instance_1_state, " ", instance_2_state)
    print("outside while")

    while ec2_re_ob.Instance(ec2_1).state['Name'] and ec2_re_ob.Instance(ec2_2).state['Name'] not in ('running', 'stopped'):
        print("waiting termination ...")
        time.sleep(10)


def wait_ec2():
    RunningInstances = []
    # check_inst1 = 0
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
        # check_inst = len(RunningInstances)
        for instance in instances:
            # for each instance, append to array

            RunningInstances.append(instance.id)
            check_inst = len(RunningInstances)
            #print("check_inst:", check_inst)
            #print("check_id:", RunningInstances)
        check_inst = len(RunningInstances)
        if int(check_inst) != 6:
            RunningInstances = []
            check_inst1 = len(RunningInstances)
        else:
            #print("A")
            break
            # print("[ " + instance.id + " ]")

    print("Time in listing Instances2", time.time() - initial, "Seconds")

    # for each_in in ec2_re_ob.instances.all():
    #     print("[ "+ each_in.id + " ]")


#### MAIN CODE ####

print("Welcome to TUD Chaos Monkey (tud_cm)\n")

print("You have 6 instances running")
ec2_list=(get_ec2_instances())

#end_time1=time.time()
#print(time.time() - end_time1, " seconds")
while True:
    ask_del=int(input("How many do you want tud_cm to dirupt >> [2]: "))
    if ask_del != int(2):
        print("Please type ""2"" to delete any 2 instances")
    else:
        print("\nThe following 2 instance IDs will be disrupted: ")
        break




# using random.choice() to
# get a random number
random_ec2_1 = random.choice(ec2_list)
random_ec2_2 = random.choice(ec2_list)

# printing random number
#print("\nRandom selected number is : " + str(random_ec2_1) +" "+ str(random_ec2_2) )
print("[ " + random_ec2_1 + " ]")
print("[ " + random_ec2_2 + " ]")

print("\nPlease wait while these instances are disrupted ...")

# instance_1_id = ec2_re_ob.Instance(random_ec2_2).id
# instance_2_id = ec2_re_ob.Instance(random_ec2_2).id

terminate_ec2(random_ec2_1, random_ec2_2)


"""
# state the status of random instances

instance_1_state = ec2_re_ob.Instance(random_ec2_1).state['Name']
print(instance_1_state)

instance_2_state = ec2_re_ob.Instance(random_ec2_1).state['Name']
print(instance_2_state)
"""


#
"""
while instance_1.state['Name'] not in ('running', 'stopped'):
                #while instance_1.state['Name'] not in ('stopped'):
    time.sleep(2)
    print("state: ", instance_1.state)
    instance_1.load()

"""
#


print("\tYou now have 4 instances running: ")

get_ec2_instances()

print("\nNow timing reinstatement... ")
print("\nPlease wait while these AWS HA reinstates the instances ... ")
initial = time.time()
#state_ec2(random_ec2_1, random_ec2_2)
wait_ec2()

print("\nYou now have 6 instances running: ")
get_ec2_instances()

print("\n====tud_cm Test Result====")
print("\n 2 instances stopped, 2 instances reinstated in ", time.time() - initial," seconds...test pass!")

#TEXT& EMAIL
sns = boto3.client('sns')
phone_number = '+353999999999'
# SENDER = "Shahid@dummy.com>"
# RECIPIENT = "shahidkhan@dublin.com"
# CONFIGURATION_SET = "ConfigSet"
# AWS_REGION = "eu-west-1"
# SUBJECT = "Amazon SES Test (SDK for Python)"
# BODY_TEXT = ("Amazon SES Test (Python)\r\n"
#              "This email was sent with Amazon SES using the "
#              "AWS SDK for Python (Boto)."
#             )
# CHARSET = "UTF-8"
sns.publish(Message='Hello Shahid 2 instances stopped, 2 instances reinstated ',PhoneNumber=phone_number)
