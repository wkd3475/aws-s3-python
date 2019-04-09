import boto
import boto.s3.connection
import boto.s3.key
import auth as au


def connect_aws_as() :
    conn = boto.connect_s3(
        aws_access_key_id = au.access_key,
        aws_secret_access_key = au.secret_key,
    )

    return conn


def list_buckets(conn) :
    for bucket in conn.get_all_buckets():
        print(bucket.name)
        print(bucket.creation_date)

def upload_file(conn, bucket_name, file_name) :
    bucket = conn.get_bucket(bucket_name)
    key = bucket.new_key(file_name)

conn = connect_aws_as()
list_buckets(conn)
upload_file(conn, 'python-example-s3cl', 'hello.txt')
