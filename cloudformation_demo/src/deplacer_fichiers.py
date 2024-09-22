import boto3
from datetime import datetime, timedelta
import json
import os


#  my_env_variable = os.getenv('MY_ENV_VARIABLE')

def lambda_handler(event, context):
    s3 = boto3.client('s3', "us-east-1")
    bucket_name = os.getenv('BUCKET_ARCHIVAGE')
    folderA = 'folderA/'
    folderB = 'folderB/'

    # List objects in folderA
    objects_in_folderA = s3.list_objects(Bucket=bucket_name, Prefix=folderA)

    for obj in objects_in_folderA.get('Contents', []):
        # Get the object's last modified time
        last_modified = obj['LastModified']
        
        # Check if the object is not named 'empty_file.txt' and has been in folderA for more than 1 minute
        if obj['Key'] != 'folderA/empty_file.txt' and datetime.now(last_modified.tzinfo) - last_modified > timedelta(minutes=1):
            # Construct the new key by replacing folderA with folderB
            new_key = obj['Key'].replace(folderA, folderB)
            
            # Copy the object to folderB
            s3.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': obj['Key']}, Key=new_key)
            
            # Delete the original object in folderA
            try:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            except Exception as e:
                print(f"Unable to delete the file {obj['Key']} due to bucket policy: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Moved objects from folderA to folderB')
    }
