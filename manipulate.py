from PIL import Image
import os

class Manipulate:

    def __init__(self, filename):
        self.filename = filename

    def resize_to_square(self):

        img = Image.open(f'images/{self.filename}')
        img_w, img_h = img.size

        if img_w > img_h:
            size = img_w
            offset = (0, (size - img_h) // 2)
        else:
            size = img_h
            offset = ((size - img_w) // 2, 0)

        # fn, fext = os.path.splitext(self.filename)
        bg = Image.new('RGB', (size, size), 'white')

        bg.paste(img, offset)
        bg.save(f'resized/{self.filename}')

    def create_thumbnail(self, size):

        file_path = f'resized/{self.filename}'
        new_size = size, size

        if os.path.exists(file_path):
            img = Image.open(file_path)
            img.thumbnail(new_size)
            img.save(f'thumbnails/{self.filename}')
        else:
            self.resize_to_square()
            self.create_thumbnail(size)
