from pathlib import Path

class Statement:

    '''   IN BUILD!    '''
    xmlfile = ''

    canva = f'''
-----------------------------------------------------------------------------------------------------------------------
|                                   SPRAWOZDANIE FINANSOWE / FINANCIAL STATEMENT                                      |
-----------------------------------------------------------------------------------------------------------------------
|DATA / DATE                                                                                                          |
-----------------------------------------------------------------------------------------------------------------------
|NAZWA FIRMY / COMPANY NAME                                                                                           |
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
|                                                  BILANS / BALANCE                                                   |
-----------------------------------------------------------------------------------------------------------------------
|AKTYWA                                                                                                               |
-----------------------------------------------------------------------------------------------------------------------
| A. AKTYWA TRWAŁE                                                                                                    |
-----------------------------------------------------------------------------------------------------------------------
|    I. WARTOŚCI NIEMATERIALNE I PRAWNE                                                                               |
|       1. KOSZTY ZAKOŃCZONYCH PRAC ROZWOJOWYCH                                                                       |
|       2. WARTOŚĆ FIRMY                                                                                              |
|       3. INNE WARTOŚCI NIEMATERIALNE I PRAWNE                                                                       |
|       4. ZALICZKI NA WARTOŚCI NIEMATERIALNE I PRAWNE                                                                |
-----------------------------------------------------------------------------------------------------------------------
|   II. RZECZOWE AKTYWA TRWAŁE                                                                                        | 
|       1. ŚRODKI TRWAŁE                                                                                              |
|           a) grunty (w tym prawo użytkowania gruntów)                                                               |
|           b) budynki, lokale, prawa do lokali i obiekty inżynierii lądowej i wodnej                                 |
|           c) urządzenia techniczne i maszyny                                                                        |
|           d) środki transportu                                                                                      |
|           e) inne środki trwałe                                                                                     |
|       2. ŚRODKI TRWAŁE W BUDOWIE                                                                                    |
|       3. ZALICZKI NA ŚRODKI TRWAŁE W BUDOWIE                                                                        |
-----------------------------------------------------------------------------------------------------------------------
|   III. NALEŻNOŚCI DŁUGOTERMINOWE                                                                                    |
|       1. OD JEDNOSTEK POWIĄZANYCH                                                                                   |
|       2. OD POZOSTAŁYCH JEDNOSTEK, W KTÓRYCH JEDNOSTKA POSIADA ZAANGAŻOWANIE W KAPITALE                             |
|       3. OD POZOSTAŁYCH JEDNOSTEK                                                                                   |
-----------------------------------------------------------------------------------------------------------------------
|   IV. INWESTYCJE DŁUGOTERMINOWE
|       1. NIERUCHOMOŚCI
|       2. WARTOŚCI NIEMATERIALNE I PRAWNE
|       3. DŁUGOTERMIONWE AKTYWA FINANSOWE
|           a) w jednostkach powiązanych
|               - udziały lub akcje
|               - inne papiery wartościowe
|               - udzielone pożyczki
|               - inne długotermionowe aktywa finansowe
|           b) w pozostałych jednostkach, w których jednostka posiada zaangażowanie w kapitale
|               - udziały lub akcje
|               - inne papiery wartościowe
|               - udzielone pożyczki
|               - inne długotermionowe aktywa finansowe
|
|
'''
    

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
