from PIL import Image
from torchvision import transforms

def compress_image(image_content, size=None):
    image = Image.open(image_content)
    if size:
        image = image.resize(512, 512)
    return image

def transform_image(image):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    ])
    return transform(image).unsqueeze(0)