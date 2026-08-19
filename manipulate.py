"""Square-crop images and generate thumbnails from them."""
import os

from PIL import Image


class Manipulate:
    """Resizes a single image to a square canvas and thumbnails it."""

    def __init__(self, filename):
        self.filename = filename

    def resize_to_square(self):
        """Pad the image onto a white square canvas and save it to resized/."""

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
        """Save a size x size thumbnail to thumbnails/, resizing first if needed."""
        file_path = f'resized/{self.filename}'
        new_size = size, size

        if os.path.exists(file_path):
            img = Image.open(file_path)
            img.thumbnail(new_size)
            img.save(f'thumbnails/{self.filename}')
        else:
            self.resize_to_square()
            self.create_thumbnail(size)
