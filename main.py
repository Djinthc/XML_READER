from statement_class import Statement


if __name__ == '__main__':

    Statement.menu()
    command = Statement.pick_command()
    
    while command != 0:

        if command == 1:
            Statement().load()
            Statement.menu()
            command = Statement.pick_command()

        elif command == 2:
            Statement().print()
            Statement.menu()
            command = Statement.pick_command()

        elif command == 3:
            Statement().save()
            Statement.menu()
            command = Statement.pick_command()
        
        else:
            print('Wrong number. Try again.')
            Statement.pick_command()
