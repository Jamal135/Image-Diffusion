''' Creation Date: 06/11/2022 '''

from image_generation import generate_image


STEPS_MIN = 20
STEPS_MAX = 15000
DEFAULT_STEPS = 50


OPTIONS = {
    '1': [False, False], 
    '2': [True, False],
    '3': [False, True],
    '4': [True, True],
}

def option_input(options = list, default: str = None):
    ''' Returns: User choice from list of options. '''
    while True:
        choice = input('Action: ')
        if choice == '' and default != None:
            print(f'Using default: {default}')
            choice = default
            break
        if choice in options or choice == default:
            break
        print(f'Options are: {options}...')
    return choice


def number_input(mininum: int = 0, maxinum: int = float('inf'), default: int = None):
    ''' Returns: Integer user input within range. '''
    while True:
        number = input('Integer: ')
        try:
            if number == '' and default != None:
                print(f'Using default: {default}')
                number = default
                break
            number = int(number)
            if number >= mininum and number <= maxinum:
                break
        except:
            pass
        print(f'Enter number between {mininum} and {maxinum}...')
    return number


def get_steps():
    ''' Returns: Integer input for number inference steps. '''
    print(f'Enter number inference steps, {STEPS_MIN}-{STEPS_MAX}...')
    return number_input(STEPS_MIN, STEPS_MAX, DEFAULT_STEPS)


def get_prompt():
    ''' Returns: String input for image generation. '''
    print('Enter text describing image you are after...')
    return input('Prompt: ')


def get_next_step():
    ''' Returns: User decision on next image generation. '''
    print('Options (1 is default):\n1: New seed\n2: Adjust steps\n3: Change prompt\n4: Restart')
    return option_input(['1', '2', '3', '4'], '1')


if __name__ == '__main__':
    choice = '4'
    while True:
        print('\n')
        if OPTIONS[choice][0]:
            steps = get_steps()
            print('\n')
        if OPTIONS[choice][1]:
            prompt = get_prompt()
            print('\n')
        if choice in ['2', '3']:
            seed = seed
        else:
            seed = None
        print('Generating image...')
        seed = generate_image(prompt, steps, seed=seed)
        print(f'Seed used: {seed}')
        print('\n')
        choice = get_next_step()


