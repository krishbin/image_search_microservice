import boto3
from utils import relative_path


class AmazonS3:

    def __init__(self, bucket_name: str, region: str, access_key: str, secret_key: str):
        self.type = "aws"
        self.bucket_name = bucket_name
        self.region = region
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
            region_name=self.region,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )

    def upload_local(self, file_path: str):
        # Upload file to S3
        pass

    def upload_url(self, file_url: str):
        # Upload file from URL to S3
        pass

    def download(self, file_path: str):
        try:
            local_file_path = relative_path(f"/downloads/{file_path}")
            self.s3_resource.Bucket(self.bucket_name).download_file(file_path, local_file_path)
            return file_path
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def get_file_content(self, file_path: str):
        try:
            obj = self.s3_resource.Object(self.bucket_name, file_path)
            return obj.get()['Body'].read().decode('utf-8')
        except Exception as e:
            print(f"Error: {e}")
            return None

    def list_files(self):
        file = []
        try:
            for obj in self.s3_resource.Bucket(self.bucket_name).objects.all():
                file.append(obj.file_path)
            return file
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_file_url(self, file_path: str):
        url = f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{file_path}"
        #check if file exists
        try:
            self.s3_resource.Object(self.bucket_name, file_path).load()
            return url
        except Exception as e:
            print(f"Error: {e}")
            return None