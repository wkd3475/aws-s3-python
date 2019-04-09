import boto3
import sys
sys.path.insert(0, '../auth')
import auth

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

access_key = auth.access_key
secret_key = auth.secret_key
a = aws_as(access_key, secret_key)
a.show_list_buckets()
