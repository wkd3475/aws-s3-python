# class aws\_s3

## variables in aws\_s3  
```client``` : boto3.client
```list_buckets``` : (list) {bucket_name}  
  
  
```aws_s3 : __init__(self, access_key, secret_key)```
input aws_access_key_id and aws_secret_access_key to use boto3.client  
store bucket list ==> list\_buckets  
  

```aws_s3 : show_list_buckets(self)```
show list\_buckets  

  
```aws_s3 : def upload_file(self, bucket_name, file)```
upload one file  
  
  
```aws_s3 : upload_files(self, bucket_name, files)```
upload files  
 
  
```aws_s3 : delete_all_files(self, bucket_name)```
empty bucket  


-------------------------------------------------------
    
```def get_files(path)
	return files ```

files = (list) {['file_name'], [file_path']}  
 
  
```def show_files(files)```
show files contents
