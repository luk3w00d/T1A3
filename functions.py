from exif import Image

def view_metadata(img, img_path, name):
    with open(img_path, 'rb') as img_file:
        img = Image(img_file)
    print(f'{name}: {img.get(name)}')

def edit_metadata(img, img_path, name):
    img.set(name, input(f'Enter new {name} info - '))
    with open (img_path, 'wb') as img_file:
        img_file.write(img.get_file())
    print(f'{name} - After: {img.get(name)}')
        