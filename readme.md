# class : aws\_s3

## variables in aws\_s3  
```client``` : boto3.client</br>
```list_buckets``` : (list) {bucket_name}</br>
  
## functions in aws\_s3
```aws_s3 : __init__(self, access_key, secret_key)```</br>
input aws_access_key_id and aws_secret_access_key to use boto3.client</br>
store bucket list ==> list\_buckets</br>
  

```aws_s3 : show_list_buckets(self)```</br>
show list\_buckets</br>

  
```aws_s3 : def upload_file(self, bucket_name, file)```</br>
upload one file</br>
  
  
```aws_s3 : upload_files(self, bucket_name, files)```</br>
upload files</br>
 
  
```aws_s3 : delete_all_files(self, bucket_name)```</br>
empty bucket</br>

-------------------------------------------------------
    
```def get_files(path)``` return : files</br>

files = (list) {['file_name'], [file_path']}</br>
 

```def show_files(files)```</br>
show files contents
