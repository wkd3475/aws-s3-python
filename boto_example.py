import boto3
import sys
sys.path.insert(0, '../auth')
import auth
import os
import glob

class aws_s3():
	_client = None
	_list_buckets = []
	
	def __init__(self, access_key, secret_key):
		self._client = boto3.client(
			's3',
			aws_access_key_id = access_key,
			aws_secret_access_key = secret_key
		)

		response = self._client.list_buckets()
		self.list_buckets = [bucket['Name'] for bucket in response['Buckets']]
		
	def show_list_buckets(self):
		print(self.list_buckets)

	#To upload file, you have to know about file_path.
	def upload_file(self, bucket_name, file_):
		self._client.upload_file(file_['file_path'], bucket_name, file_['file_name'])

	#To upload files.
	def upload_files(self, bucket_name, files):
		for i in files:
			upload_file(bucket_name, files[i])

	def delete_all_files(self, bucket_name):
		response = self._client.list_objects_v2(Bucket=bucket_name)
		print('Delete all files in %s(bucket).' %(bucket_name))
		print('Are you sure? [y, n]')
		answer = input()
		if answer == 'y':
			if 'Contents' in response:
				for item in response['Contents']:
					print('deleting file', item['Key'])
					self._client.delete_object(Bucket=bucket_name, Key=item['Key'])
					while response['KeyCount'] == 1000:
						response = self._client.list_objects_v2(
							Bucket=bucket_name,
							StartAfter=response['Contents'][0]['Key'],
						)
						for item in response['Contents']:
							print('deleting file', item['Key'])
							self._client.delete_object(Bucket=bucket_name, Key=item['Key'])
		else:
			print('cancel...')
						
def get_files(path):
	files = []

	path_listdir = path
	path_glob = path + '*'
	file_list_listdir = os.listdir(path_listdir)
	file_list_glob = glob.glob(path_glob)
	
	for i in range(len(file_list_listdir)):
		files.append({'file_name': file_list_listdir[i], 'file_path': file_list_glob[i]})
	
	return files

def show_files(files):
	for i in range(len(files)):
		print("file_name : {}".format(files[i]['file_name']))
		print("file_path : {}".format(files[i]['file_path']))
	
def main():
	files = get_files('./upload/')
	show_files(files)

	access_key = auth.access_key
	secret_key = auth.secret_key
	a = aws_as(access_key, secret_key)
	a.show_list_buckets()

main()
