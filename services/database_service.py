from pymilvus import Collection,connections,CollectionSchema, FieldSchema, DataType
from utils import variables

image_id = FieldSchema(
  name="image_id", 
  dtype=DataType.INT64, 
  is_primary=True, 
)
image_url = FieldSchema(
  name="image_url", 
  dtype=DataType.VARCHAR,  
  max_length=65535,
)
image_embedding = FieldSchema(
  name="image_embedding", 
  dtype=DataType.FLOAT_VECTOR, 
  dim=512
)

schema = CollectionSchema(
  fields=[image_id, image_url, image_embedding], 
  description="ImageSearchCollection"
)

class MilvusDatabase:
    def __init__(self):
        self.default_collection_name = variables["milvus_collection_name"]
        self.collection = None
        try:
            connections.connect(
                alias=variables["milvus_alias"], 
                host=variables["database_host"], 
                port=variables["database_port"]
            )
            self.collection = Collection(self.default_collection_name)
        except Exception as e:
            print(f"Error: {e}")
            print("Failed to connect to Milvus")

    def setupDatabase(self):
        try:
            self.create_collection(self.default_collection_name)
        except Exception as e:
            print(f"Error: {e}")
            print("Failed to create collection")

    def create_collection(self, dimension: int):
        return Collection(
            name=self.default_collection_name,
            schema=schema,
            using=variables["milvus_alias"],
            shard_num=2,
            consistency_level="Strong",
        )

    def insert(self, data: list):
        try:
            self.collection.insert(data=data)
        except Exception as e:
            print(f"Error: {e}")
            print("Failed to insert data")

    def search(self, search_params: dict):
        try:
            self.collection.load()
            self.collection.search(
                data=search_params["query_records"],
                top_k=search_params["top_k"],
                anns_field="image_embedding",
                limit=search_params["limit"],
                param=search_params["params"],
            )
        except Exception as e:
            print(f"Error: {e}")
            print("Failed to search data")
        

    def truncate(self):
        # Truncate collection
        self.collection.drop(self.default_collection_name)

    def get_all_embeddings(self):
        num_vectors = self.collection.num_entities
        all_ids = list(range(num_vectors))
        search_params = {
            "query_records": [],
            "top_k": num_vectors, 
            "params": {"nprobe": 16},
            "limit": num_vectors,
            "anns_field": "image_embedding"
            }
        all_embeddings = self.search(search_params)
        print(all_embeddings)
        # return (all_ids, all_embeddings)

    def load(self):
        # Load data
        self.collection.load()