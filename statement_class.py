from pathlib import Path

class Statement:

    '''   IN BUILD!    '''
    xmlfile = ''

    def __init__(self):
        pass

        


    def menu():
        print('''
              
    What would You like to do:
              
        1. Load Statement
        2. Print Statement
        3. Save Statement to file
        0. Exit
              ''')


    def pick_command():
        '''Taking command and checking if it is a number'''
        try:
            command = int(input('Select :   '))
            return command
        except ValueError:
            print('Wrong choice! Pick a number corresponding with menu.')
            Statement.pick_command()


    def load(self):
        print('''
    Make sure statement You are looking for is correctly placed in folder "files".
    Please enter the file name.
    
              ''')
        try:
            Statement.xmlfile = ''
            current_folder = Path(__file__).parents[0]
            filename = input('Filename: ')
            file_path = current_folder/f'files/{filename}'
            with open(file_path, "r") as file:
                Statement.xmlfile = file.read()
            print('File has been successfully loaded.')
            return 
        except:
            print('Loading went wrong. Make sure statement file name is correct. Try again')
            Statement.load(self)
        

    def print(self):
        print(self.xmlfile)
        return
        

    def save(self):
        file = str(input('Enter file name: '))
        with open(file, 'w') as doc:
            doc.write(Statement.xmlfile)
        print('File has been saved')
        return
