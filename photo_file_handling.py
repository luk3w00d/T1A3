from simple_term_menu import TerminalMenu 
from exif import Image


print('Hi, Welcome to the Photo Organising Application !')

def main():
    print('What would you like to do ?')
    options = ['Edit new image file', 'Continue editing file', 'exit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    while menu_entry_index != 2:
        if menu_entry_index == 0:
            print('Perfect lets start editing!')
        elif menu_entry_index == 1: 
            print('Perfect lets continue editing!')
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
