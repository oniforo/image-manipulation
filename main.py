from manipulate import Manipulate
import os

for file in os.listdir('images'):
    files = Manipulate(file)
    files.create_thumbnail(300)