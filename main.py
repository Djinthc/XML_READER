class Statement:

    '''   IN BUILD!    '''

    def __init__(self) -> None:
        textfile = ''

    def menu():
        print('''Hi! Pick what would You like to do:
              
                1. Load Statement
                2. Print Statement
                3. Save Statement to file
                0. Exit''')

    def pick_command():
        '''Taking command and checking if it is a number'''
        try:
            command = int(input('Select :   '))
        except:
            print('Wrong choice! Pick a number corresponding with menu.')
            Statement.pick_command()


if __name__ == '__main__':

    Statement.menu()
    command = Statement.pick_command()
    
    while command != 0:

        if command == 1:
            Statement.load()

        elif command == 2:
            Statement.print()

        elif command == 3:
            Statement.save()
        
        else:
            print('wohooho')
            Statement.pick_command()
