# class : aws\_s3

### variables in aws\_s3  
```_client``` : boto3.client</br>
```_resource``` : boto3.resource</br>
```_bucket``` : bucket name</br>
```_list_buckets``` : (list) {bucket_name}</br>
```_prefix``` : default : './root', it will use as fuse's root directory</br>
  
### functions in aws\_s3
```aws_s3 : __init__(self, access_key, secret_key, bucket)```</br>
**=>**</br>
1. init aws_access_key_id and aws_secret_access_key to use boto3.client</br>
2. init aws_access_key_id and aws_secret_access_key to use boto3.resource</br>
3. init bucket
4. store bucket list ==> list\_buckets</br>
  

```aws_s3 : show_list_buckets(self)```</br>
**=>** show list_buckets</br>


```aws_s3 : show_list_objects(self)``` return : list of Contents in bucket</br>
**=>** show list_objects</br>

  
```aws_s3 : upload_file(self, file_path)```</br>
**=>** upload a file to same location</br>
  

```aws_s3 : upload_file(self, file_path, s3_path)```</br>
**=>** upload a file to "s3_path" ex) /hello.py in local file_path to /tmp/hello.py in s3_path</br>

  
```aws_s3 : upload_folder(self, folder_path)```</br>
**=>** upload folder</br>


```aws_s3 : upload_all(self)```</br>
**=>** upload all files to s3</br>


```aws_s3 : delete_file(file_path)```</br>
**=>** **not yet!!!**</br>


```aws_s3 : delete_all(self)```</br>
**=>** empty bucket</br>


```aws_s3 : download_file(self, s3_path)```</br>
**=>** download a file "s3_path"</br>


```aws_s3 : download_folder(self, s3_path)```</br>
**=>** download a folder "s3_path"</br>


```aws_s3 : download_all(self)```</br>
**=>** download all files in bucket</br>

-------------------------------------------------------

# functions
```def get_files(path)``` return : files</br>
files = (list) {['file_name'], [file_path']}</br>
**=>** to show root dictionary</br>
 

```def show_files(files)```</br>
**=>** show files contents</br>

--------------------------------------------------------

you need auth folder and auth.py file</br>=></br></br>
aws-s3cl</br>
&nbsp;&nbsp;ㄴauth</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ㄴauth.py</br>
&nbsp;&nbsp;ㄴaws-s3-python</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ㄴ...</br></br>

**auth.py**
```python
{
	access_key = 'your aws_access_key_id'
	secret_key = 'your aws_secret_access_key'
	bucket = 'your bucket_name'
}
```

