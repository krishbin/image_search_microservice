import clip
from .image_trainer_cifar import CiFarImageTrainer
from .image_trainer_aws import AWSImageTrainer
from utils import Logger, relative_path, variables, set_variable, run_mode
from services import db
import celery
from app.image_handler import ImageHandler
from account_handler.minio import Minio

model, preprocess = clip.load("ViT-B/32", device=variables["device"])

def create_image_trainer(seeds,account,image_handler,device,model,preprocess,db):
    if account == "cifar":
        return CiFarImageTrainer(seeds,account,device,model,preprocess,db)
    elif account == "aws":
        return AWSImageTrainer(seeds,account,image_handler,device,model,preprocess,db)

# imtrainer = create_image_trainer(9222,"cifar",variables["device"],model,preprocess,db)
def miniO_s3_bucket():
    return Minio(
        "image-search-bucket",
        variables["bucket_url"],
        variables["bucket_key"],
        variables["bucket_secret"]
    )

account = miniO_s3_bucket()
image_handler = ImageHandler(account)
imgtrainer = create_image_trainer(9222,"aws",image_handler,variables["device"],model,preprocess,db)