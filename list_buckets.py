#!/c/Users/spatil4/AppData/Local/Programs/Python/Python36-32/python
import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]

print("bucket list : %s " % buckets)


