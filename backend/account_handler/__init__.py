from .amazons3bucket import AmazonS3
from utils import variables
from .minio import Minio

account = None

# def amazon_s3_bucket():
#     return AmazonS3(
#         variables["bucket_url"],
#         variables["bucket_key"],
#         variables["bucket_secret"],
#         variables["account_type"]
#     )

 

# if variables["account_type"] == "aws":
#     account = amazon_s3_bucket()

def minio_s3_bucket():
    return Minio(
        "image-search-bucket",
        variables["bucket_url"],
        variables["bucket_key"],
        variables["bucket_secret"]
    )

# account = minio_s3_bucket()

