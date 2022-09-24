from simple_term_menu import TerminalMenu 
from functions import view_metadata, edit_metadata, Image, remove_metadata

print('Hi, Welcome to the Photo Organising Application !')

def main():
    print('What would you like to do ?')
    menu_entry_index = -1
    while menu_entry_index != 2:
        options = [
            'View photo metadata',
            'Edit photo metadata', 
            'Exit']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if menu_entry_index == 0:
            print("Perfect lets check the photo's metadata")
            img_filename = input('Type the exact name of the image including the file type  .jpg, .png ') # input from user
            img_path = f'Image/{img_filename}'
            print('What would you like to view ?')
            with open(img_path, 'rb') as img_file:
                img = Image(img_file)
                view = ['Copywrite Info', 
                'Date and time Info', 
                'What device model used', 
                'Artist', 
                'Device make', 
                'Back to main menu'
                ]
                terminal_menu = TerminalMenu(view)
                view_index = terminal_menu.show()
                if view_index == 0:
                    view_metadata(img, img_path, 'copyright')
                elif view_index == 1:
                    view_metadata(img, img_path, 'datetime')
                elif view_index == 2:
                    view_metadata(img, img_path, 'model')  
                elif view_index == 3:
                    view_metadata(img, img_path, 'artist')
                else:
                        view_metadata(img, img_path, 'make')       
        
        elif menu_entry_index == 1: 
            print("Perfect lets update the photo's metadata")
            edit_index = -1
            while edit_index != 2:
                edit = [
                'Add Metadata', 
                'Remove Metadata', 
                'Back to main menu'
                ]
                terminal_menu = TerminalMenu(edit)
                edit_index = terminal_menu.show()
                if edit_index == 0:
                        print('What would you like to add ?')
                        metadata = [
                            'copyright info',
                            'Artist', 
                            'Device make', 
                            'Back to main menu'
                            ]
                        folder_path = 'Image'
                        img_filename = input('Type the exact name of the image including the file type  .jpg, .png ') 
                        img_path = f'{folder_path}/{img_filename}'        # ^ input from user ^
                        img = None
                        with open(img_path, 'rb') as img_file:
                            img = Image(img_file)
                            img_file.close()
                        terminal_menu = TerminalMenu(metadata)
                        metadata_index = terminal_menu.show()
                        if metadata_index == 0:
                            edit_metadata(img, img_path, 'copyright')
                        elif metadata_index == 1:
                            edit_metadata(img, img_path, 'artist')
                        elif metadata_index == 2:
                            edit_metadata(img, img_path, 'make')

                elif edit_index == 1:
                            print('What would you like to remove ?')
                            metadata = [
                                'copyright info',
                                'Artist',
                                'make',
                                'Back to main menu'
                                ]
                            folder_path = 'Image'
                            img_filename = input('Type the exact name of the image including the file type  .jpg, .png ') 
                            img_path = f'{folder_path}/{img_filename}'
                            img = None
                            with open(img_path, 'rb') as img_file:
                                img = Image(img_file)
                                img_file.close()
                            terminal_menu = TerminalMenu(metadata)
                            metadata_index = terminal_menu.show()
                            if metadata_index == 0:
                                remove_metadata(img, img_path, 'copyright')
                            elif metadata_index == 1:
                                remove_metadata(img, img_path, 'artist')
                            elif metadata_index == 2:
                                remove_metadata(img, img_path, 'make')
        else: 
            print('See you next time !')  # name of photo to be error handled  
if __name__ == '__main__':
    main()