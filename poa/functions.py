import os.path
from exif import Image

def get_file():
    img_filename = None

    while img_filename is None:
        img_filename = input('Type the exact path and name of the image including the file type  .jpg, .png: ')

        if os.path.exists(img_filename):
            break

        print("File not found!")
        img_filename = None

    return img_filename

def view_metadata(img, img_path, name):
    with open(img_path, 'rb') as img_file:
        img = Image(img_file)
    print(f'{name}: {img.get(name)}')

def edit_metadata(img, img_path, name):
    img.set(name, input(f'Enter new {name} info - '))
    with open (img_path, 'wb') as img_file:
        img_file.write(img.get_file())
    print(f'{name} - After: {img.get(name)}')

def remove_metadata(img, img_path, name):
    with open(img_path, 'wb') as img_file:
        img.delete(name)
        img_file.write(img.get_file())
        img_file.close()
    print(f'{name} - After: {img.get(name)}')       