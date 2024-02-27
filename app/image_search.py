# get all the columns from table as list of tensors
import clip
from services import db
import json

class ImageSearch:
    def __init__(self, model, preprocess,device,text,search_type):
        self.db = db
        self.text = text
        self.model = model
        self.device = device
        self.preprocess = preprocess
        self.search_type = search_type
    
    def get_text_embedding(self):
        text = clip.tokenize(self.text).to(self.device)
        text_features = self.model.encode_text(text)
        return text_features.cpu().tolist()
    
    def set_search_params(self):   
        return {
            "metric_type": self.search_type, 
            "params": {"nprobe": 10}
        }
    
    def get_similarity_result(self):
        results = self.db.collection.search(
            data=self.get_text_embedding(), 
            anns_field="image_embedding", 
            # the sum of `offset` in `param` and `limit` 
            # should be less than 16384.
            param=self.set_search_params(),
            limit=10,
            expr=None,
            # set the names of the fields you want to 
            # retrieve from the search result.
            output_fields=['image_id','image_url'],
            consistency_level="Strong"
        )

        return json.loads(results)
        
