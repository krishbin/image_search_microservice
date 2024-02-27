import clip
from .image_search import ImageSearch
from .image_handler import ImageHandler
from account_handler import account
from account_handler.minio import Minio
from utils import Logger, relative_path, variables, set_variable, run_mode

model, preprocess = clip.load("ViT-B/32", device=variables["device"])


text = "fish"
search_type = "L2"

image_search = ImageSearch(model,preprocess,variables["device"],text,search_type)

def miniO_s3_bucket():
    return Minio(
        "image-search-bucket",
        variables["bucket_url"],
        variables["bucket_key"],
        variables["bucket_secret"]
    )
account = miniO_s3_bucket()
image_handler = ImageHandler(account)
