import boto3
from datetime import datetime, timedelta
import os

def lambda_handler(event, context):
    # Specify the S3 bucket name and directory (prefix) containing the files
    bucket_name = os.getenv('BUCKET_ARCHIVAGE')
    directory = 'folderB/'
    
    # Create a connection to the S3 service
    s3 = boto3.client('s3')
    
    # Retrieve the list of objects in the specified directory
    objects_in_directory = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory)
    
    # Iterate through each object in the directory
    for obj in objects_in_directory.get('Contents', []):
        # Get the object's last modified time
        last_modified = obj['LastModified']
        
        # Check if the object's key is not 'empty_file.txt'
        if obj['Key'] != 'folderB/empty_file.txt':
            # Calculate the date ten minutes ago
            one_month_ago = datetime.now() - timedelta(minutes=10)
            
            # Check if the object was created one month ago or earlier
            if last_modified < one_month_ago:
                # Delete the object
                try:
                    s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                except Exception as e:
                    print(f"Deleted object '{obj['Key']}' from the directory '{directory}'")
    
    return {
        'statusCode': 200,
        'body': 'Deleted old files successfully'
    }                  
