# image-manipulation

A small Python script that batch-processes images: crops each one to a
square (padding with white where needed) and generates a thumbnail.

## How it works

`main.py` loops over every file in `images/` and, for each one, calls
`Manipulate.create_thumbnail()`. That method:

1. Looks for the image in `resized/`. If it's not there yet, calls
   `resize_to_square()`, which pads the image to a square canvas (white
   background) and saves it into `resized/`.
2. Downscales the squared image to the requested thumbnail size and saves
   it into `thumbnails/`.

## Requirements

- Python 3.10+
- [Pillow](https://python-pillow.org/) 9.1.0

## Setup

```bash
python -m venv venv
venv\Scripts\activate   # on Windows
pip install Pillow
```

## Usage

Drop your source images into `images/`, then run:

```bash
python main.py
```

Squared versions land in `resized/`; 300x300 thumbnails land in
`thumbnails/`.

## Project structure

```
images/       # source images
resized/      # images padded to a square canvas
thumbnails/   # 300x300 thumbnails generated from resized/
main.py       # entry point
manipulate.py # Manipulate class: resize_to_square, create_thumbnail
```
