from simple_term_menu import TerminalMenu 
from exif import Image


# img.artist = 'bob the builder'
# with open(f'{folder_path}/{img_filename}', 'wb') as new_image_file:
    # new_image_file.write(img.get_file())

# print(img.has_exif)
# print(folder_path)
# print(img_filename)
# print(img_path)
# print(img.list_all())


print('Hi, Welcome to the Photo Organising Application !')

def main():
    print('What would you like to do ?')
    options = ['View photo metadata', 'Edit photo metadata', 'exit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    while menu_entry_index != 2:
        if menu_entry_index == 0:
            print("Perfect lets check the photo's metadata")
        
            folder_path = 'Image'
            img_filename = input('Type the exact name of the image including .jpg ') # input from user
            img_path = f'{folder_path}/{img_filename}'

            with open(img_path, 'rb') as img_file:
                img = Image(img_file)
                print(img.list_all())
        
        elif menu_entry_index == 1: 
            print("Perfect lets update the photo's metadata")
        
        print('What would you like to do ?')
        options = ['Add Metadata', 'Remove Metadata', 'exit']
        terminal_menu = TerminalMenu(options)
        
        menu_entry_index = terminal_menu.show()
        while menu_entry_index != 2:
            if menu_entry_index == 0:
                print('What Data would you like to add?')
            elif menu_entry_index == 1: 
                print('What would you like to Remove?')

            menu_entry_index = terminal_menu.show()
        
        


        
    

    print('See you next time !')

if __name__ == '__main__':
    main()
