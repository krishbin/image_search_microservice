from .image_trainer import ImageTrainer

#inheriting the ImageTrainer class
class AWSImageTrainer(ImageTrainer):
    def __init__(self,seeds,account):
        super().__init__(seeds,account)
 
