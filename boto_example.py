import boto
import boto.s3.connection
import boto.s3.key
import sys
sys.path.insert(0, '../auth')
import auth

class aws_as():
	conn = None
	list_buckets = []
	def __init__(self, access_key, secret_ket):
		#connect to s3
		self.conn = boto.connect_s3(
			aws_access_key_id = access_key,
			aws_secret_access_key = secret_key
		)
        
		#get buckets
		for bucket in self.conn.get_all_buckets():
			self.list_buckets.append([bucket.name, bucket.creation_date])

	def show_list_buckets(self):
		for bucket in self.list_buckets:
			print(bucket)

	def upload_file(self, bucket_name, file_name):
		bucket = self.conn.get_bucket(bucket_name)
		key = bucket.new_key(file_name)

access_key = auth.access_key
secret_key = auth.secret_key
a = aws_as(access_key, secret_key)
a.show_list_buckets()
