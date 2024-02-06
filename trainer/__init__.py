import clip
from .image_trainer_cifar import CiFarImageTrainer
from .image_trainer_aws import AWSImageTrainer
from utils import Logger, relative_path, variables, set_variable, run_mode
from services import db
import celery

model, preprocess = clip.load("ViT-B/32", device=variables["device"])

def create_image_trainer(seeds,account,device,model,preprocess,db):
    if account == "cifar":
        return CiFarImageTrainer(seeds,account,device,model,preprocess,db)
    elif account == "aws":
        return AWSImageTrainer(seeds,account)

imtrainer = create_image_trainer(9222,"cifar",variables["device"],model,preprocess,db)