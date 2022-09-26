import sys
import os.path

from colorama import Fore, Back, Style, init
from termcolor import colored

from simple_term_menu import TerminalMenu 
import functions

import int_enum

print(colored('Hi, Welcome to the Photo Organizing Application!', 'blue', 'on_white'))

def main():
    img_filename = None

    if len(sys.argv) > 1:
        img_filename = sys.argv[1]

    else:
        img_filename = functions.get_file()

    print(colored('What would you like to do?', 'green'))
    menu_entry_index = int_enum.MenuItems.NONE

    while menu_entry_index != int_enum.MenuItems.EXIT:
        options = [
            'View photo metadata',
            'Edit photo metadata',
            'Exit'
        ]
        
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == int_enum.MenuItems.VIEW_METADATA:
            print("Perfect lets check the photo's metadata")
            print('What would you like to view?')

            with open(img_filename, 'rb') as img_file:
                img = functions.Image(img_file)
                view = [
                    'Copy-write Info',
                    'Date and time Info',
                    'What device model used',
                    'Artist',
                    'Device make',
                    'Back to main menu'
                ]

                terminal_menu = TerminalMenu(view)
                metadata_index = terminal_menu.show()
            try:
                if metadata_index == int_enum.MetadataMenuItems.COPYRIGHT:
                    functions.view_metadata(img, img_filename, 'copyright')
                elif metadata_index == int_enum.MetadataMenuItems.DATE:
                    functions.view_metadata(img, img_filename, 'datetime')
                elif metadata_index == int_enum.MetadataMenuItems.DEVICE_MODEL:
                    functions.view_metadata(img, img_filename, 'model')
                elif metadata_index == int_enum.MetadataMenuItems.ARTIST:
                    functions.view_metadata(img, img_filename, 'artist')
                elif metadata_index == int_enum.MetadataMenuItems.DEVICE_MAKE:
                    functions.view_metadata(img, img_filename, 'make')          
            except   LookupError:
                print('There is no metadata for this photo, You can add some metadata now!')       
        
        elif menu_entry_index == int_enum.MenuItems.UPDATE_METADATA:
            print("Perfect lets update the photo's metadata")
            edit_index = int_enum.EditMenuItems.NONE

            while edit_index != int_enum.EditMenuItems.EXIT:
                edit = [
                    'Add Metadata',
                    'Remove Metadata',
                    'Back to main menu'
                ]

                terminal_menu = TerminalMenu(edit)
                edit_index = terminal_menu.show()

                if edit_index == int_enum.EditMenuItems.ADD:
                    print('What would you like to add?')

                    metadata = [
                        'copyright info',
                        'Artist',
                        'Device make',
                        'Date and time',
                        'Back to main menu'
                    ]

                    img = None

                    with open(img_filename, 'rb') as img_file:
                        img = functions.Image(img_file)
                        img_file.close()

                    terminal_menu = TerminalMenu(metadata)
                    metadata_index = terminal_menu.show()

                    if metadata_index == int_enum.UpdateMetadata.UPDATE_COPYRIGHT:
                        functions.edit_metadata(img, img_filename, 'copyright')
                    elif metadata_index == int_enum.UpdateMetadata.UPDATE_ARTIST:
                        functions.edit_metadata(img, img_filename, 'artist')
                    elif metadata_index == int_enum.UpdateMetadata.UPDATE_MAKE:
                        functions.edit_metadata(img, img_filename, 'make')
                    elif metadata_index == int_enum.UpdateMetadata.UPDATE_DATETIME:
                        functions.edit_metadata(img, img_filename, 'datetime')

                elif edit_index == int_enum.EditMenuItems.REMOVE:
                    print('What would you like to remove?')

                    metadata = [
                        'copyright info',
                        'Artist',
                        'make',
                        'Back to main menu'
                    ]

                    img = None

                    with open(img_filename, 'rb') as img_file:
                        img = functions.Image(img_file)
                        img_file.close()

                    terminal_menu = TerminalMenu(metadata)
                    metadata_index = terminal_menu.show()

                    if metadata_index == int_enum.RemoveMenuItems.REMOVE_COPYRIGHT:
                        functions.remove_metadata(img, img_filename, 'copyright')
                    elif metadata_index == int_enum.RemoveMenuItems.REMOVE_ARTIST:
                        functions.remove_metadata(img, img_filename, 'artist')
                    elif metadata_index == int_enum.RemoveMenuItems.REMOVE_MAKE:
                        functions.remove_metadata(img, img_filename, 'make')
                    elif metadata_index == int_enum.RemoveMenuItems.REMOVE_DATETIME:
                        functions.remove_metadata(img, img_filename, 'datetime')
        else:
            print(colored('See you next time!', 'grey', 'on_yellow'))  
if __name__ == '__main__':
    main()