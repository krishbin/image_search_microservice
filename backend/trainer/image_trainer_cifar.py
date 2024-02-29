from .image_trainer import ImageTrainer
from torchvision.datasets import CIFAR100
import torchvision.transforms as T


preprocess_toPIL = T.ToPILImage()

class CiFarImageTrainer(ImageTrainer):
    def __init__(self,seeds,account,device,model,preprocess,db):
        super().__init__(seeds,account,device,model,preprocess,db)
        self.data_length = 100
        self.data = self.load_data()
        self.embeddings = []

    def load_data(self):
        dataset = CIFAR100(
          root = "data",
          download = True,
          transform = T.ToTensor()
          )
        images = []
        for i in range(self.data_length):
            images.append(preprocess_toPIL(dataset[i][0]))
        return images
    
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
                        "image_url": "cifar"+str(i)+".jpg",
                        "image_embedding": image_features.cpu().numpy().tolist()[0]
                    }
                ]
                # print(data)
                # print(dir(self.db))
                self.db.insert(data=data)
    

