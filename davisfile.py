import boto3

import random

import time



TIME2TRY = 1200


# the list of EC2

def listofEC2(instances):

    EC2LIST = []

    for instance in instances:

        EC2LIST.append(instance.id)

    return EC2LIST




# the list of EC2 running instances

def Ec2insts():

    ec2client = boto3.resource('ec2')

    instances = ec2client.instances.filter(

    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])   # this filter ensures we only get running EC2s

    return instances



# EC2 instances counts

def EC2COUNTS(instances)
    NoOfInstances = 0

    for instance in instances:

        NoOfInstances = NoOfInstances+1

    return NoOfInstances



# prints a list of the EC2 instances running in the account to the console

def printEc2instances(instances):

    for instance in instances:

        print(instance.id, instance.state["Name"])



# kills an EC2 instance based on ID

def killAnInstance(target):

    evilMonkeyClient = boto3.client('ec2')

    response = evilMonkeyClient.terminate_instances(

        InstanceIds=[target]

    )



# timing the reestablishment of VMs back to original numbers

def timingRebuild(total):

    machines = 0

    timeForFunction = time.time()       # Grab current time

    while machines < total:             # continue checking the machines until it matches the original number

        testing = Ec2insts()

        machines = EC2COUNTS(testing)

        if time.time() - timeForFunction > TIME2TRY:  # Implement time limit for revival checks

            return "Failed"

    return "Passed"



# Picks X number of instances to kill

def breakingStuff(amount):

    currentInstances = Ec2insts()

    currentInstancesAsList = convertEC2iterToList(currentInstances)

    while int(amount) > 0:

        nextTarget = random.choice(currentInstancesAsList)

        currentInstancesAsList.remove(nextTarget)

        instancesImpactedStr = "The following instance ID {} will be disrupted:".format(nextTarget)

        print(instancesImpactedStr)

        killAnInstance(nextTarget)

        amount = amount - 1





##########################################

# The actual code that runs ChaosMonkey  #

##########################################





print("Welcome to the TUD Chaos Monkey!")

print("Checking AWS ...")






# initial infrastructure assessment

runningMachines = Ec2insts()

printEc2instances(runningMachines)

instanceCount = EC2COUNTS(runningMachines)



instanceCountStr = "You current have {} instances running".format(instanceCount)

print(instanceCountStr)



# Get the number of instances to kill with some validation

inputofEC2 = input("How many instances would you like to disrupt? ")



if int(inputofEC2) == 0:

    inputofEC2 = input("This is going to be pretty dull if we don't disrupt SOME of these instances...Try again ")

    if int(inputofEC2) == 0:

        print("Well if you're not going to take this seriously...")

        raise SystemExit



while int(inputofEC2) > instanceCount:

    inputofEC2 = input("...You just saw how many is there, you know you asked for two many, try again ")



print("Please wait while we unleash the chaos monkey...")



# chaos begins here

breakingStuff(int(inputofEC2))



# tracking time after killing instances to track revival time

startTime = time.time()



# confirm updated EC2 instances

updatedRunningMachines = Ec2insts()

printEc2instances(updatedRunningMachines)

updatedInstanceCount = EC2COUNTS(updatedRunningMachines)

updatedInstanceCountStr = "You now have {} instances running".format(updatedInstanceCount)

print(updatedInstanceCountStr)



# start checking repeatedly for the machines to have recovered

print("Now timing reinstatement")

print("Please wait while we test our recoverability")

result = timingRebuild(instanceCount)



# grab end time to calculate recovery time

endTime = time.time()

resultForNotification = ""



print("====CHAOS MONKEY TEST RESULT====")



# time to recover obtained

testTime = endTime - startTime



# build test results output

if result == "Passed":

    testResultStr = "It took {} seconds to get back to {} instances".format(testTime, instanceCount)

    print(testResultStr)

    resultForNotification = "Dave Hill's TUD_CM test PASSED. "+testResultStr

elif result == "Failed":

    testResultStr = "Chaos Monkey has won. We have not gotten back to the original number of instances. Goodbye"

    print(testResultStr)

    resultForNotification = "Dave Hill's TUD_CM test FAILED. " + testResultStr

else:

    print("Something has gone wrong in the test, Dave should debug further")

    resultForNotification = "While the test goofed, you got a notification still from Dave Hill, yay!"



# Activate the reporting lambda

ActivateLambdaNotifcation(resultForNotification)