#!/c/Users/spatil4/AppData/Local/Programs/Python/Python36-32/python


import boto3

ec2 = boto3.resource('ec2')

instance_id = 'i-0ae0ccf26364596b9'
instance = ec2.Instance(instance_id)
response= instance.terminate()
print(response)
