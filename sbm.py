import boto3

def upload_csv_to_s3(bucket_name, file_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, s3_key)
        print("File uploaded successfully from S3")
    except FileNotFoundError:
        print("the file was not found")
    except Exception as e:
	print(f"An error occured: {str(e)}")
	

bucket_name = 'data5-s3rev'
file_name = 'abcd.pdf'
s3_key = 'abcd.pdf'
get_file_from_s3(bucket_name, file_name, s3_key)