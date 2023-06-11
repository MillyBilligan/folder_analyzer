from texts import commands

def commands_handler(message):
    # commands processing

    if message in commands:

        match message:
            case '/start':              
                return True
            case '/help':
                print(commands['/help'])
            case '/credits':
                print(commands['/credits'])
    else:
        print('message is unrecognized')