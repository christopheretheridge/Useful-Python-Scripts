from boto3.session import Session
import boto3
import botocore
import os

# Store your keys in environment variables for security
ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# High Level Method
s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY , aws_secret_access_key=SECRET_KEY)
bucket = s3.Bucket('YourBucketName')
obj = s3.Object('YourBucketName', 'TheFileYouWantFromYourBucket')

# Reads the contents of your file if it is something like a
# text file or a PEM Key
print(obj.get()['Body'].read().decode('utf-8'))
