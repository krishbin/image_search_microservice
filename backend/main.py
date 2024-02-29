from fastapi import BackgroundTasks,FastAPI
from pydantic import BaseModel
from utils import variables,set_variable,relative_path
from utils.logger import Logger
from app.image_search import ImageSearch

from fastapi.middleware.cors import CORSMiddleware
from services import db 
from trainer import create_image_trainer
from account_handler import miniO_s3_bucket
from app.image_handler import ImageHandler
import clip
import json

logger = Logger(log_dir=relative_path("/logs"))
logger.info("Imported the required modules")
logger.info("Starting the application")


model, preprocess = clip.load("ViT-B/32", device=variables["device"])
search_type = "L2"



class GetAccountDetail(BaseModel):
    bucket_url: str
    bucket_key: str
    bucket_secret: str
    bucket_name: str

imagesearch = FastAPI()

# Configure CORS settings
origins = [
    "http://127.0.0.1:5173",
]

imagesearch.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@imagesearch.get("/")
async def root():
    return {"message": "Hello Worl"}

#only allow admin to access this
@imagesearch.get("/refresh_embeddings")
def refresh_embeddings():
    account = miniO_s3_bucket()
    image_handler = ImageHandler(account)
    imgtrainer = create_image_trainer(9222,"aws",image_handler,variables["device"],model,preprocess,db)
    imgtrainer.train()
    return {"message": "Refreshed the embeddings"}

@imagesearch.post("/set_account_details")
async def get_account_details(account: GetAccountDetail):
    set_variable("bucket_url", account.bucket_url)
    set_variable("bucket_key", account.bucket_key)
    set_variable("bucket_secret", account.bucket_secret)
    set_variable("bucket_name", account.bucket_name)
    return {"message": "Account details updated"}
    
@imagesearch.get("/search")
def search_image(item: str):
    image_search = ImageSearch(model,preprocess,variables["device"],item,search_type)
    image_result = image_search.get_similarity_result()
    return {"message":"Search successful","result":image_result}

