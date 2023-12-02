import boto3

def get_csv_to_s3(bucket_name,s3_key,file_name):
    s3 = boto3.client('s3')
    try:
	s3.download_file(bucket_name,s3_key,file_name)
	print("file download sucessfully to s3")
    except Exception as e:
	print(f"an error occured:{str(e)}")

bucketname = 'data5-s3rev'
file_name = 'india.pdf'
s3_key = 'india-flag.pdf'

get_csv_to_s3(bucket_name,s3_key,file_name)
		 
	
	