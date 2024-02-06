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
        self.client = connections.connect(
            alias=variables["milvus_alias"], 
            host=variables["database_host"], 
            port=variables["database_port"]
        )

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
            self.client.insert(collection_name=self.default_collection_name, records=data)
        except Exception as e:
            print(f"Error: {e}")
            print("Failed to insert data")

    def search(self, data: list):
        # Search data
        pass

    def truncate(self):
        # Truncate collection
        self.client.collection.drop(self.default_collection_name)