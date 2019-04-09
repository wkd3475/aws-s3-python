python-aws-s3\_s3
============
# class aws\_s3

## variables in aws\_s3  
`client : boto3.client  
`list_buckets : (list) {bucket_name}  
  
  
## input aws\_access\_key\_id and aws\_secret\_access\_key to use boto3.client  
## store bucket list ==> list\_buckets  
`def __init__(self, access_key, secret_key)  
  
  
## show list\_buckets  
`def show_list_buckets(self)  
  
  
## upload one file  
`def upload_file(self, bucket_name, file)  
  
  
## upload files  
`def upload_files(self, bucket_name, files)  
  
  
## empty bucket  
`def delete_all_files(self, bucket_name)


-------------------------------------------------------
  
# files structure  
## files = (list) {['file_name'], [file_path']}  
`def get_files(path)  
`	return files  
  
  
## show files' contents  
`def show_files(files)  
