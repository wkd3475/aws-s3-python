import boto3
import sys
sys.path.insert(0, '../auth')
import auth
import os
import glob

class aws_as():
	client = None
	list_buckets = []
	
	def __init__(self, access_key, secret_key):
		self.client = boto3.client(
			's3',
			aws_access_key_id = access_key,
			aws_secret_access_key = secret_key
		)

		response = self.client.list_buckets()
		self.list_buckets = [bucket['Name'] for bucket in response['Buckets']]
		
	def show_list_buckets(self):
		print(self.list_buckets)

	#To upload file, you have to know about file_path.
	def upload_file(self, bucket_name, file_name, file_path):
		self.client.upload_file(file_path, bucket_name, file_name)

		

	def delete_all_files(self, bucket_name):
		response = self.client.list_objects_v2(Bucket=bucket_name)
		print('Delete all files in %s(bucket).' %(bucket_name))
		print('Are you sure? [y, n]')
		answer = input()
		if answer == 'y':
			if 'Contents' in response:
				for item in response['Contents']:
					print('deleting file', item['Key'])
					self.client.delete_object(Bucket=bucket_name, Key=item['Key'])
					while response['KeyCount'] == 1000:
						response = client.list_objects_v2(
							Bucket=bucket_name,
							StartAfter=response['Contents'][0]['Key'],
						)
						for item in response['Contents']:
							print('deleting file', item['Key'])
							self.client.delete_object(Bucket=bucket_name, Key=item['Key'])
		else:
			print('cancel...')
						
		


path_listdir = "./upload/"
path_glob = "./upload/*"
file_list_listdir = os.listdir(path_listdir)
file_list_glob = glob.glob(path_glob)

print("file_list_listdir : {}".format(file_list_listdir))
print("file_list_glob : {}".format(file_list_glob))

access_key = auth.access_key
secret_key = auth.secret_key
a = aws_as(access_key, secret_key)
a.show_list_buckets()

a.delete_all_files('python-example-s3cl')
