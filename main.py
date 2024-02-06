from fastapi import BackgroundTasks,FastAPI
from pydantic import BaseModel
from utils import variables,set_variable,relative_path
from utils.logger import Logger

logger = Logger(log_dir=relative_path("/logs"))
logger.info("Imported the required modules")
logger.info("Starting the application")

class GetAccountDetail(BaseModel):
    bucket_url: str
    bucket_key: str
    bucket_secret: str
    account_type: str

imagesearch = FastAPI()

@imagesearch.get("/")
async def root():
    return {"message": "Hello World"}

#only allow admin to access this
@imagesearch.get("/refresh_embeddings")
async def refresh_embeddings():
    return {"message": "Refreshed the embeddings"}

@imagesearch.post("/set_account_details")
async def get_account_details(account: GetAccountDetail):
    if account.account_type not in variables["supported_account_types"]:
        return {"message": f"Account type not supported, supported types are {variables['supported_account_types']}"}
    set_variable("bucket_url", account.bucket_url)
    set_variable("bucket_key", account.bucket_key)
    set_variable("bucket_secret", account.bucket_secret)
    set_variable("account_type", account.account_type)
    return {"message": "Account details updated"}
    
@imagesearch.post("/search")
async def search_image(item: str):
    return {"message": "Searching for the image"}
    

