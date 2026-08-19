"""Generate square-cropped thumbnails for every image in images/."""
import os

from manipulate import Manipulate

for file in os.listdir('images'):
    files = Manipulate(file)
    files.create_thumbnail(300)
