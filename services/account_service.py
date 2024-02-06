class ImageTrainerTriggerService:
    def __init__(self, image_trainer_service: ImageTrainerService):
        self.image_trainer_service = image_trainer_service

    def trigger_image_trainer(self, image_trainer_trigger: ImageTrainerTrigger):
        self.image_trainer_service.train_image(image_trainer_trigger.image_id)