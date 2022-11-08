''' Creation Date: 09/11/2022 '''

# NOTE: Setup is intended for Windows only

import os
import sys
import pip


def import_or_install(package):
    ''' Purpose: Installs package if it does not exist. '''
    try:
        __import__(package)
        print(f'{package} package already installed')
    except ImportError:
        pip.main(['install', package])


def is_venv():
    ''' Purpose: Checks if inside virtual environment. '''
    return hasattr(sys, 'real_prefix') or sys.base_prefix != sys.prefix


def create_env():
    ''' Purpose: Creates .env file with provided Hugging Face token. '''
    print(Formats.status('Get read token at https://huggingface.co/settings/tokens'))
    TOKEN = input(Formats.question('Enter Hugging Face token'))
    with open('.env', 'w') as file:
        file.write(f'TOKEN={TOKEN}')


if __name__ == '__main__':
    try:
        import_or_install('colorama')
        from functions.library import Formats
        if is_venv():
            print(Formats.status('Setting up prerequisites'))
            if not os.path.exists('.env'):
                create_env()
            else:
                print(Formats.info('.env already exists'))
            print(Formats.status('Installing requirements'))
            pip.main(['install', '-r', 'requirements.txt'])
            print(Formats.status('Finishing setup'))
            print(Formats.info('Enable developer mode and get latest GPU drivers'))
        else:
            print(Formats.alert('No virtual environment, aborting'))
    except Exception as e:
        print(Formats.alert(f"Automatic setup failed:\n{e}"))
