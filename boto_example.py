import boto3
import sys
sys.path.insert(0, '../auth')
import auth
import os
import glob
import botocore

class aws_s3():
	_client = None
	_resource = None
	_bucket = None
	_list_buckets = []
	_prefix = './root/' #이 값은 추후 fuse의 root directory가 될 것임
	
	#__init__
	def __init__(self, access_key, secret_key, bucket):
		self._client = boto3.client(
			's3',
			aws_access_key_id = access_key,
			aws_secret_access_key = secret_key
		)

		self._resource = boto3.resource(
			's3',
			aws_access_key_id = access_key,
			aws_secret_access_key = secret_key
		)
		
		self._bucket = bucket

		response = self._client.list_buckets()
		self.list_buckets = [bucket['Name'] for bucket in response['Buckets']]
	
	#show buckets list
	def show_list_buckets(self):
		print(self.list_buckets)

	#show objects list
	def show_list_objects(self):
		list = print(self._client.list_objects(Bucket=self._bucket)['Contents'])
		return list

	#upload a file to same location
	def upload_file(self, file_path):
		print('upload... (%s)' %(file_path))
		self._client.upload_file(file_path, self._bucket, file_path)
		print('finish')

	#upload a file to different location
	def upload_file(self, file_path, s3_path):
		print('upload... (%s)' %(file_path))
		self._client.upload_file(file_path, self._bucket, s3_path)
		print('finish')

	#upload folder
	#변경 사항이 있는 파일만 업로드하고 싶은데 해당 내용은 fuse를 통해 알아내야함
	def upload_folder(self, folder_path):
		for root, dirs, files in os.walk(folder_path):
			for file_ in files:
				local_path = os.path.join(root, file_)

				relative_path = os.path.relpath(local_path, folder_path)
				s3_path = relative_path

			print('searching %s in %s' %(s3_path, self._bucket))
			
			try:
				self._client.head_object(Bucket=self._bucket, Key=s3_path)
				#파일이 변경사항이 있으면 upload하는 내용이 추가되어야 하는 부분
				print('path found on s3! skip %s...' %(s3_path))
			except:
				print("uploading %s..." %(s3_path))
				self._client.upload_file(local_path, self._bucket, s3_path)
				print("complete")
			
	#delete a file
	def delete_file(self, file_name):
		print("delete_file")

	#delete all files
	def delete_all(self):
		response = self._client.list_objects_v2(Bucket=self._bucket)
		print('Delete all files in %s(bucket).' %(self._bucket))
		print('Are you sure? [y, n]')
		answer = input()
		if answer == 'y':
			if 'Contents' in response:
				for item in response['Contents']:
					print('deleting file', item['Key'])
					self._client.delete_object(Bucket=self._bucket, Key=item['Key'])
					while response['KeyCount'] == 1000:
						response = self._client.list_objects_v2(
							Bucket=self._bucket,
							StartAfter=response['Contents'][0]['Key'],
						)
						for item in response['Contents']:
							print('deleting file...', item['Key'])
							self._client.delete_object(Bucket=self._bucket, Key=item['Key'])
		else:
			print('cancel...')
	
	#download a file
	def download_file(self, s3_path):
		try:
			print("downloading... : %s" %(s3_path))
			self._resource.Bucket(self._bucket).download_file(s3_path, self._prefix+s3_path)
			print("complete")
		except botocore.exceptions.ClientError as e:
			if e.response['Error']['Code'] == "404":
				print("The object does no exist.")
			else:
				raise

	#download folder
	def download_folder(self, s3_path):
		bucket = self._resource.Bucket(self._bucket)
		for key in bucket.objects.filter(Prefix = s3_path):
			if not os.path.exists(os.path.dirname(self._prefix+key.key)):
				os.makedirs(os.path.dirname(self._prefix+key.key))
			print("downloading... : %s" %(key.key))
			bucket.download_file(key.key, self._prefix+key.key)
			print("complete")

	def download_all(self):
		self.download_folder("")
			
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
	files = get_files('./root/')
	show_files(files)

	#사용할 bucket 지정
	bucket = 'python-example-s3cl'

	#암호키 입력
	access_key = auth.access_key
	secret_key = auth.secret_key
	bucket = auth.bucket
	client = aws_s3(access_key, secret_key, bucket)

	#list = client.show_list_objects()
	#client.upload_folder('./root')
	client.download_all()
	#client.delete_all_files()
	

main()
