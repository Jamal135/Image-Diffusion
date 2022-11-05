import pip
import os


def import_or_install(package):
    ''' Purpose: Installs package if it does not exist. '''
    try:
        __import__(package)
        print(f'{package} package already installed')
    except ImportError:
        pip.main(['install', package])  


def create_env():
    ''' Purpose: Creates .env file with provided Hugging Face token. '''
    print('Please enter READ Hugging Face token https://huggingface.co/settings/tokens \nToken:')
    TOKEN = input()
    with open('.env', 'w') as file:
        file.write(f'TOKEN={TOKEN}')


if __name__ == '__main__':
    try:
        import_or_install('virtualenv') # https://pypi.org/project/virtualenv/
        import_or_install('conda') # https://pypi.org/project/conda/
        if not os.path.exists('.env'):
            create_env()
        print('Installing packages, this will take a while...')
        os.system('virtualenv .venv')
        os.system('conda activate .venv')
        os.system('pip install -r requirements.txt')
        os.system('pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116')
        print('Note: On Windows enable developer mode or run elevated, get latest NVIDIA drivers.')
    except Exception as e:
        print(f"Automatic setup failed:\n{e}")
