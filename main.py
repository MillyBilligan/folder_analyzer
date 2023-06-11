import os
from texts import ext, commands
from admin import commands_handler



def get_path():

    print("path's example 'C:/Users/user'")
    
    while True:
        path = input('enter path: ')
        try: 
            os.startfile(path)
            return path
    
        except FileNotFoundError:
             pass
            



def analyze_folder(items):

    result = {'folders': 0,'text': 0, 'images': 0, 'video': 0, 'audio': 0, 'apps': 0, 'python': 0, 'unrecognized': 0, 'total': 0}
    extensions = [item.split('.')[1].lower() for item in items if len(item.split('.')) == 2]


    for i in extensions:
        if i in ext['text']:
            result['text'] += 1

        elif i in ext['images']:
            result['images'] += 1

        elif i in ext['video']:
            result['video'] += 1

        elif i in ext['audio']:
            result['audio'] += 1

        elif i in ext['apps']:
            result['apps'] += 1

        elif i in ext['python']:
            result['python'] += 1

        else:
            result['unrecognized'] += 1

    
    result['folders'] = len(items) - len(extensions)
    result['total'] = len(items) 
    return result



def main():

    print(commands['start_message'])

    while True:
        inp = input()
        command = commands_handler(inp)

        if command:
            path = get_path()
            files = os.listdir(path)

            analyzed = analyze_folder(files)

            print(analyzed)

                


if __name__ == '__main__':
    main()