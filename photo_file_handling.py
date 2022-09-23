from simple_term_menu import TerminalMenu 
from exif import Image



# img.artist = 'bob the builder'
# with open(f'{folder_path}/{img_filename}', 'wb') as new_image_file:
#     new_image_file.write(img.get_file())

# print(img.has_exif)
# print(folder_path)
# print(img_filename)
# print(img_path)
# print(img.list_all())
 


print('Hi, Welcome to the Photo Organising Application !')

def main():
    print('What would you like to do ?')
    menu_entry_index = -1
    while menu_entry_index != 2:
        options = ['View photo metadata', 'Edit photo metadata', 'exit']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            print("Perfect lets check the photo's metadata")
            folder_path = 'Image'
            img_filename = "image1.JPG"
            # img_filename = input('Type the exact name of the image including the file type  .jpg, .png ') # input from user
            img_path = f'{folder_path}/{img_filename}'
            print('What would you like to view ?')
            with open(img_path, 'rb') as img_file:
                img = Image(img_file)
                view = ['Copywrite Info', 'Date and time Info', 'What device used']
                terminal_menu = TerminalMenu(view)
                view_index = terminal_menu.show()
                if view_index == 0:
                    print(f'Copyright: {img.get("copyright")}')
                    
                elif view_index == 1:
                    print(f'Date and time: {img.get("datetime")}')
                
                else:
                    print(f'Device Used: {img.get("model")}')    
                # ask user what they want to view
                # Get the input
                # use input to get the key
                # then print value
        elif menu_entry_index == 1: 
            print("Perfect lets update the photo's metadata")
            edit = ['Add Metadata', 'Remove Metadata', 'exit']
            terminal_menu = TerminalMenu(edit)
            edit_index = terminal_menu.show()
            if edit_index == 0:
                    print('What would you like to add ?')

                    metadata = ['copyright info','Artist', 'If a flash was used' ]
                    folder_path = 'Image'
                    img_filename = "image1.JPG"
                    # img_filename = input('Type the exact name of the image including the file type  .jpg, .png ') # input from user
                    img_path = f'{folder_path}/{img_filename}'
                    with open(img_path, 'rb') as img_file:
                        img = Image(img_file)
                        terminal_menu = TerminalMenu(metadata)
                        metadata_index = terminal_menu.show()
                        if metadata_index == 0:
                            img.copyright = input('Enter new copyright info - ')
                            print(f'copyright - After: {img.get("copyright")}')
                        

           
                        # ask glen ^

                   
                        
                        
                    
                            
                         
                
           
             
        else: 
            print('See you next time !')





if __name__ == '__main__':
    main()
