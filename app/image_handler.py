from account_handler import account

class ImageHandler:
    def __init__(self):
        self.account = account
        self.images = []
    
    def get_image_content(self,rel_image_path):
        return self.account.get_file_content(rel_image_path)
    
    def list_images(self):
        file_list = self.account.list_files()
        for file in file_list:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".bmp"):
                self.images.append(file)

    def compress_image(self,rel_image_path):
        image = self.get_image_content(rel_image_path)
        image = image.resize((512,512))
        return image