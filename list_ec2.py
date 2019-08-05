import boto3
import random
print("Welcome to TUD Chaos Monkey (tud_cm)\n")


ec2client=boto3.client('ec2', aws_access_key_id="AKIAJO53UHGYI6A7N4CQ",aws_secret_access_key="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",region_name="eu-west-1")


#ec2client = boto3.client('ec2')
response = ec2client.describe_instances()


def get_instances():
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
            #print([instance["InstanceId"]])

            #print(instance["InstanceId"])
            instList=(instance["InstanceId"])
            return(instList)
        # initializing list
        #list_instances=[instance["InstanceId"]]
        #print(list_instances)
        #list_instances.append(instance["InstanceId"])
        #print(list_instances)
    #return(instance["InstanceId"])
    list=[instList.append()]
    print(list)
    return(list)
#ask_del=input("How many do you want tud_cm to dirupt >> [2]:")

#list_instances=[instance["InstanceId"]]
#list_instances.append(list_instances)
#print("List: ", list_instances)

print("You have following instances running")
print(get_instances())
#list_of_instances=[get_instances()]
#print("List:", list_of_instances)
# initializing list
#test_list = [1, 4, 5, 2, 7]

# printing original list
#print("Original list is : " + str(list_instances))

# using random.choice() to
# get a random number
#random_instances = random.choice(list_instances)

# printing random number
#print("Random selected number is : " + str(random_instances))

#print("[ " + instance["InstanceId"] + " ]")