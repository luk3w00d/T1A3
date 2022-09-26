import sys
import os.path
from exif import Image
from colorama import Fore, Back, Style, init
from termcolor import colored

def get_file():
    img_filename = None

    while img_filename is None:
        img_filename = input(colored('Type the exact path and name of the image including the file type  .jpg, .png: ', 'green'))

        if os.path.exists(img_filename):
            break
        init(autoreset=True)
        print(colored('File not found! Please make sure you have entered the info correctly', 'white', 'on_red'))
        print(colored('Like this example. /Users/ComputerName/Photos/Image_Name.jpg', 'white', 'on_red'))
        print(colored('Including any Uppercase letters Or to Quit Press Ctrl+C', 'red')) 
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