''' Creation Date: 06/11/2022 '''


from pathlib import Path
import time
import inquirer
from colorama import Fore, Style

from functions.image_generation import generate_image


STEPS_MIN = 15
STEPS_MAX = 15000

# Choices
REGENERATE = 'Regenerate'
ADJUST_STEPS = 'Adjust Steps'
CHANGE_PROMPT = 'Change Prompt'
LOOP = 'Loop'
START_OVER = 'Start Over'
EXIT = 'Exit'

LOG_PATH = 'logs/image_generation_log.csv'
LOG_HEADING = 'time, choice, steps, seed, path, prompt\n'

class Formats:
    ''' Purpose: Correctly format print messages given purpose. '''
    def status(message: str):
        ''' Format: [-] message...'''
        indicator = '\n[' + Fore.GREEN + '-' + Style.RESET_ALL + ']'
        return f'{indicator} {message}...'
    def question(message: str):
        ''' Format: [?] message: '''
        indicator = '\n[' + Fore.YELLOW + '?' + Style.RESET_ALL + ']'
        return f'{indicator} {message}: '
    def alert(message: str):
        ''' Format: [!] message...'''
        indicator = '\n[' + Fore.RED + '!' + Style.RESET_ALL + ']'
        return f'{indicator} {message}...'


def create_log():
    ''' Purpose: Creates log file if it does not exist. '''
    path = Path(LOG_PATH)
    if not path.is_file():
        with open(LOG_PATH, 'a') as log:
            log.write(LOG_HEADING)


def check_steps(_, number: str):
    ''' Purpose: Validates custom inference steps input. '''
    if not number.isdigit():
        raise inquirer.errors.ValidationError('', reason = f'{number} is not a valid number...')
    number = int(number)
    if number < STEPS_MIN:
        raise inquirer.errors.ValidationError('', reason = f'{number} is less than {STEPS_MIN}...')
    if number > STEPS_MAX:
        raise inquirer.errors.ValidationError('', reason = f'{number} is greater than {STEPS_MAX}...')
    return True


def get_steps():
    ''' Returns: Integer input for number inference steps. '''
    steps = inquirer.list_input(
                        message = f'Number of steps',
                        choices = [25, 50, 75, 100, 250, 750, 'Custom'],
                        default = 50)
    if steps == 'Custom':
        steps = inquirer.text(
                        message = f'Enter number steps',
                        validate = check_steps
        )
    return int(steps)


def get_prompt():
    ''' Returns: String input for image generation. '''
    while True:
        prompt = input(Formats.question('Describe image'))
        if prompt == '':
            print(Formats.alert('Please enter a prompt'))
        elif '"' in prompt:
            print(Formats.alert('Do not use ""s in prompt'))
        else:
            break
    return prompt


def check_loop(_, number: str):
    ''' Purpose: Validates custom inference steps input. '''
    if not number.isdigit():
        raise inquirer.errors.ValidationError('', reason = f'{number} is not a valid number...')
    return True


def get_next_step():
    ''' Returns: User decision on next image generation. '''
    choice = inquirer.list_input(
                        message = 'What would you like to do next',
                        choices = [REGENERATE, ADJUST_STEPS, CHANGE_PROMPT, LOOP, START_OVER, EXIT],
                        default = REGENERATE
                    )
    if choice == 'Loop':
        iterations = int(inquirer.text(
                        message = 'Howmany times do you want to loop',
                        validate = check_loop
        ))
        for count in range(iterations):
            print(Formats.status(f'Generating image {count + 1}/{iterations}'))
            create_image(None, choice)
        return get_next_step()
    return choice


def uniquify(filename: str):
	''' Returns filepath modified if needed to ensure it doesn't already exist. '''
	counter = 1
	path = Path(f'images/{filename}.png')
	while path.is_file():
		path = Path(f'images/{filename + "-" + str(counter)}.png') 
		counter += 1
	return path


def create_image(seed: int, choice: str):
    ''' Purpose: Updates log file and called image generation. '''
    seed, image = generate_image(prompt, steps, seed=seed)
    path = uniquify(filename)
    image.save(path)
    print(f'Seed used: {seed}\n')
    when = str(time.time())
    line = ','.join([when, choice, str(steps), str(seed), str(path), f'"{prompt}"'])
    with open(LOG_PATH, 'a') as log:
        log.write(f'{line}\n')
    return seed


if __name__ == '__main__':
    filename = 'result'
    create_log()
    choice = START_OVER
    while True:
        if choice in [START_OVER, ADJUST_STEPS]:
            steps = get_steps()
        if choice in [START_OVER, CHANGE_PROMPT]:
            prompt = get_prompt()
        if choice in [ADJUST_STEPS, CHANGE_PROMPT]:
            seed = seed
        else:
            seed = None
        print(Formats.status('Generating image'))
        seed = create_image(seed, choice)
        choice = get_next_step()
        if choice == EXIT:
            exit()

# Migrate to Questionary: https://questionary.readthedocs.io/en/stable/pages/types.html#text
