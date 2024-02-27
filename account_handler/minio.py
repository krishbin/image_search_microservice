import boto3
from utils import relative_path
from PIL import Image
import io

class Minio:

    def __init__(self, bucket_name: str, endpoint: str, access_key: str, secret_key: str):
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        try:
            self.s3_resource = self.connect()
        except Exception as e:
            print(f"Error: {e}")
            print("Failed to connect to S3")

    def connect(self):
        return boto3.resource(
            "s3",
            endpoint_url=self.endpoint,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )

    def upload_local(self, file_path: str):
        # Upload file to S3
        pass

    def upload_url(self, file_url: str):
        # Upload file from URL to S3
        pass
   
    def get_file_content(self, file_path: str):
        try:
            obj = self.s3_resource.Object(self.bucket_name, file_path)
            image_bytes = obj.get()['Body'].read()
            image = Image.open(io.BytesIO(image_bytes))
            return image
        except Exception as e:
            print(f"Error: {e}")
            return None

    def list_files(self):
        files =[]
        try:
            bucket = self.s3_resource.Bucket(self.bucket_name)
            for obj in bucket.objects.all():
                # print(obj.key, obj.last_modified)
                files.append(obj.key)
            return files
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_file_url(self, file_path: str):
        url = f"{self.endpoint}/{self.bucket_name}/{file_path}"
        #check if file exists
        try:
            self.s3_resource.Object(self.bucket_name, file_path).load()
            return url
        except Exception as e:
            print(f"Error: {e}")
            return None
