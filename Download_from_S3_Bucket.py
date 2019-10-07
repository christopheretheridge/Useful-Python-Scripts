from boto3.session import Session
import boto3
import os

# Store your keys in environment variables for security
ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

s3_bucket_name = 'YourBucketName'

# Establish a connection to S3
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY , aws_secret_access_key=SECRET_KEY)

# Download your file
s3.download_file('s3_bucket_name','some.file','/Users/some/directory/some.file')
