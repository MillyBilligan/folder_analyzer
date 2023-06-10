import os
from extensions import ext



def get_path():
    # getting path

    print("path's example - C:/Users/example")
    path = input('enter path: ')
    return path


def try_open(path):
    # checking if path is valid

    try: 
        os.startfile(path)
        return True
    
    except FileNotFoundError:
        return False


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

    path = None
    files = [] # items in path's directory

    # getting valid path
    while True:
        path = get_path()

        if try_open(path):
            break
        else:
            print('path is not valid')

    # getting directory items
    files = os.listdir(path)

    # doing some magic ///\\\
    analyzed = analyze_folder(files)
    analyzed_keys = list(analyzed.keys())

    # printing result
    print(*[f'{key}: {analyzed[key]}' for key in analyzed_keys], sep='\n')


if __name__ == '__main__':
    main()