#!/c/Users/spatil4/AppData/Local/Programs/Python/Python36-32/python

import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
        ImageId = 'ami-082b5a644766e0e6f',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro')

print(instance[0].id)
