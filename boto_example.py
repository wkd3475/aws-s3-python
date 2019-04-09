import boto3
import sys
sys.path.insert(0, '../auth')
import auth
import os
import glob

#하나의 파일 시스템은 하나의 aws-s3 버킷에만 연결된다고 가정하고 코드 수정할 필요가 있음
class aws_s3():
	_client = None
	_list_buckets = []
	
	#__init__
	def __init__(self, access_key, secret_key):
		self._client = boto3.client(
			's3',
			aws_access_key_id = access_key,
			aws_secret_access_key = secret_key
		)

		response = self._client.list_buckets()
		self.list_buckets = [bucket['Name'] for bucket in response['Buckets']]
	
	#show buckets list
	def show_list_buckets(self):
		print(self.list_buckets)

	#upload file same location
	def upload_file(self, bucket_name, file_path):
		print('upload... (%s)' %(file_path))
		self._client.upload_file(file_path, bucket_name, file_path)
		print('finish')

	#upload file different location
	def upload_file(self, bucket_name, file_path, s3_path):
		print('upload... (%s)' %(file_path))
		self._client.upload_file(file_path, bucket_name, s3_path)
		print('finish')

	#upload folder
	#변경 사항이 있는 파일만 업로드하고 싶은데 해당 내용은 fuse를 통해 알아내야함
	def upload_folder(self, bucket, folder_path):
		for root, dirs, files in os.walk(folder_path):
			for file_ in files:
				local_path = os.path.join(root, file_)

				relative_path = os.path.relpath(local_path, folder_path)
				s3_path = relative_path

			print('searching %s in %s' %(s3_path, bucket))
			
			try:
				self._client.head_object(Bucket=bucket, Key=s3_path)
				#파일이 변경사항이 있으면 upload하는 내용이 추가되어야 하는 부분
				print('path found on s3! skip %s...' %(s3_path))
			except:
				print("uploading %s..." %(s3_path))
				self._client.upload_file(local_path, bucket, s3_path)
			

	def delete_file(self, bucket_name, file_name):
		print("delete_file")

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
							print('deleting file...', item['Key'])
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
		#print("file_name : {}".format(files[i]['file_name']))
		print("file_path : {}".format(files[i]['file_path']))


def main():
	#upload폴더가 fuse의 root directory라고 가정
	files = get_files('./upload/')
	show_files(files)
	bucket = 'python-example-s3cl'

	access_key = auth.access_key
	secret_key = auth.secret_key
	a = aws_s3(access_key, secret_key)
	a.show_list_buckets()
	#a.delete_all_files(bucket)

main()
