import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv
load_dotenv()

# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

######### Create a client #########
s3 = boto3.client('s3', region_name='ap-south-1', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
location = {'LocationConstraint': 'ap-south-1'}

######### Create a bucket #########
# response = s3.create_bucket(Bucket='jayant-learning-2', CreateBucketConfiguration=location)

######### List all buckets #########
# list_buckets = s3.list_buckets()
# print(list_buckets)

#########Delete a bucket#########
# s3.delete_bucket(Bucket='jayant-learning')

######### Upload a file #########
# s3.upload_file('C:\\Users\\jayde\\Downloads\Screenshot 2023-08-08 203356.png', 'jayant-learning', 'Screenshot 2023-08-08 203356.png')

######### List all files/object in a bucket #########
# list_objects = s3.list_objects(Bucket='jayant-learning')
# print(list_objects)

######### Download a file/object #########
# s3.download_file('jayant-learning', 'Screenshot 2023-08-08 203356.png', 'C:\\Users\\jayde\\Downloads\Screenshot 2023-08-08 20335.png')

######### Delete a file/object #########
# s3.delete_object(Bucket='jayant-learning', Key='Screenshot 2023-08-08 203356.png')

######### Enable versioning #########
# s3.put_bucket_versioning(Bucket='jayant-learning', VersioningConfiguration={'Status': 'Enabled'})

######### Copy a file/object from one bucket to another #########
# s3.copy_object(CopySource='jayant-learning/Screenshot 2023-08-08 203356.png', Bucket='jayant-learning-2', Key='Screenshot 2023-08-08 203356.png')

######### Generate a presigned URL #########
# presigned_url = s3.generate_presigned_url('get_object', Params={'Bucket': 'jayant-learning', 'Key': 'Screenshot 2023-08-08 203356.png'}, ExpiresIn=3600)
# print(presigned_url)

######### Kill a presigned URL #########
s3.delete_object(Bucket='jayant-learning', Key='Screenshot 2023-08-08 203356.png')