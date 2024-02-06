import torch
import torchvision.transforms as T
import numpy as np
import os
import time

from utils import Logger, relative_path, variables, set_variable, run_mode
from utils.image_utils import compress_image, transform_image
from account_handler import account

logger = Logger(log_dir=relative_path("/logs"))

class ImageTrainer:
    def __init__(self,seeds,account,device,model,preprocess,db):
        self.account = account
        self.images = []
        self.device = device
        self.seeds = seeds
        self.torch = torch
        self.model = model
        self.preprocess = preprocess
        self.init_seeds()
        self.data = None
        self.db = db

    def init_seeds(self):
        np.random.seed(self.seeds)
        torch.manual_seed(self.seeds)
        torch.cuda.manual_seed(self.seeds)
        torch.cuda.manual_seed_all(self.seeds)
        os.environ['PYTHONHASHSEED'] = str(self.seeds)
        os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_mb:224'

    def get_database_info(self):
        print(self.db)
