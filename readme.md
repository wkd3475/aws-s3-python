class aws\_s3
============
## class aws\_s3

variables in aws\_s3
**client : boto3.client**
**list__buckets : (list) {bucket__name}**


#input aws\_access\_key\_id and aws\_secret\_access\_key to use boto3.client
#store bucket list ==> list\_buckets
def \_\_init\_\_(self, access\_key, secret\_key)


#show list\_buckets
	def **show\_list\_buckets**(self)


#upload one file
	def **upload\_file**(self, bucket\_name, file)


#upload files
	def **upload\_files**(self, bucket\_name, files)


#empty bucket
	def **delete\_all\_files**(self, bucket\_name)


-------------------------------------------------------

#files structure
#files = (list) {['file\_name'], [file\_path']}
def **get\_files**(path)
	return **files**


#show files' contents
def **show\_files**(files)
