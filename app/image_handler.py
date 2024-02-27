

class ImageHandler:
    def __init__(self,account):
        self.account = account
        self.images = []
    
    def get_image_content(self,rel_image_path):
        return self.account.get_file_content(rel_image_path)
    
    def list_images(self):
        return self.account.list_files()
       
    def compress_image(self,rel_image_path):
        image = self.get_image_content(rel_image_path)
        image = image.resize((512,512))
        return image
    
    def get_image_url(self,rel_image_path):
        return self.account.get_file_url(rel_image_path)
    