
from simple_term_menu import TerminalMenu 
from functions import view_metadata, edit_metadata, Image, remove_metadata
import int_enum

print('Hi, Welcome to the Photo Organizing Application!')

def main():
    img_filename = input('Type the exact name of the image including the file type  .jpg, .png: ')
    img_path = f'Image/{img_filename}'

    print('What would you like to do?')
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

            with open(img_path, 'rb') as img_file:
                img = Image(img_file)
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

                if metadata_index == int_enum.MetadataMenuItems.COPYRIGHT:
                    view_metadata(img, img_path, 'copyright')
                elif metadata_index == int_enum.MetadataMenuItems.DATE:
                    view_metadata(img, img_path, 'datetime')
                elif metadata_index == int_enum.MetadataMenuItems.DEVICE_MODEL:
                    view_metadata(img, img_path, 'model')
                elif metadata_index == int_enum.MetadataMenuItems.ARTIST:
                    view_metadata(img, img_path, 'artist')
                elif metadata_index == int_enum.MetadataMenuItems.DEVICE_MAKE:
                    view_metadata(img, img_path, 'make')             

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
                        'Back to main menu'
                    ]

                    img = None

                    with open(img_path, 'rb') as img_file:
                        img = Image(img_file)
                        img_file.close()

                    terminal_menu = TerminalMenu(metadata)
                    metadata_index = terminal_menu.show()

                    if metadata_index == int_enum.UpdateMetadata.UPDATE_COPYRIGHT:
                        edit_metadata(img, img_path, 'copyright')
                    elif metadata_index == int_enum.UpdateMetadata.UPDATE_ARTIST:
                        edit_metadata(img, img_path, 'artist')
                    elif metadata_index == int_enum.UpdateMetadata.UPDATE_MAKE:
                        edit_metadata(img, img_path, 'make')

                elif edit_index == int_enum.EditMenuItems.REMOVE:
                    print('What would you like to remove?')

                    metadata = [
                        'copyright info',
                        'Artist',
                        'make',
                        'Back to main menu'
                    ]

                    img = None

                    with open(img_path, 'rb') as img_file:
                        img = Image(img_file)
                        img_file.close()

                    terminal_menu = TerminalMenu(metadata)
                    metadata_index = terminal_menu.show()

                    if metadata_index == int_enum.RemoveMenuItems.REMOVE_COPYRIGHT:
                        remove_metadata(img, img_path, 'copyright')
                    elif metadata_index == int_enum.RemoveMenuItems.REMOVE_ARTIST:
                        remove_metadata(img, img_path, 'artist')
                    elif metadata_index == int_enum.RemoveMenuItems.REMOVE_MAKE:
                        remove_metadata(img, img_path, 'make')
        else:
            print('See you next time!')  # name of photo to be error handled
if __name__ == '__main__':
    main()