from .image_trainer import ImageTrainer

#inheriting the ImageTrainer class
class AWSImageTrainer(ImageTrainer):
    def __init__(self,seeds,account,image_handler,device,model,preprocess,db):
        super().__init__(seeds,account,device,model,preprocess,db)
        self.image_handler = image_handler
        self.data,self.data_url = self.load_data(image_handler)
        self.data_length = self.get_data_length()
        # self.data_length = self.get_data_length()
        self.embeddings = []

    def load_data(self,image_handler):
        images = []
        images_url = []
        for i in image_handler.list_images():
            images.append(image_handler.compress_image(i))
            images_url.append(image_handler.get_image_url(i))
        return images,images_url
    
    def get_data_length(self):
        return len(self.data)
    
    def get_data(self):
        return self.data
    
    def train(self):
        for i in range(self.data_length):
            image = self.data[i]
            image = self.preprocess(image)
            with self.torch.no_grad():
                image = image.unsqueeze(0).to(self.device)
                image_features = self.model.encode_image(image.to(self.device))
                self.embeddings.append(image_features.cpu())
                data = [
                    {
                        "image_id": i,
                        "image_url": self.data_url[i],
                        "image_embedding": image_features.cpu().numpy().tolist()[0]
                    }
                ]
                # print(data)
                # print(dir(self.db))
                self.db.insert(data=data)
 
