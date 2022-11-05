''' Creation Date: 06/11/2022 '''


from pathlib import Path
import time
import inquirer
from image_generation import generate_image


STEPS_MIN = 15
STEPS_MAX = 15000

# Choices
REGENERATE = 'Regenerate'
ADJUST_STEPS = 'Adjust Steps'
CHANGE_PROMPT = 'Change Prompt'
START_OVER = 'Start Over'
EXIT = 'Exit'


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
                        choices = [25, 50, 100, 250, 750, 'Custom'],
                        default = 50)
    if steps == 'Custom':
        steps = inquirer.text(
                        message = f'Enter number steps',
                        validate = check_steps
        )
    return int(steps)


def check_prompt(_, prompt: str):
    ''' Purpose: Validates prompt input text. '''
    if prompt == '':
        raise inquirer.errors.ValidationError('', reason = 'Please enter a prompt...')
    return True


def get_prompt():
    ''' Returns: String input for image generation. '''
    return inquirer.text(
                        message = 'Describe image',
                        validate = check_prompt
    )


def get_next_step():
    ''' Returns: User decision on next image generation. '''
    return inquirer.list_input(
                        message = 'What would you like to do next?',
                        choices = [REGENERATE, ADJUST_STEPS, CHANGE_PROMPT, START_OVER, EXIT],
                        default = REGENERATE
                    )


def uniquify(filename: str):
	''' Returns filepath modified if needed to ensure it doesn't already exist. '''
	counter = 1
	filepath = Path(f'Images/{filename}.png')
	while filepath.is_file():
		filepath = Path(f'Images/{filename + "-" + str(counter)}.png') 
		counter += 1
	return filepath


if __name__ == '__main__':
    filename = 'result'
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
        print('\nGenerating image...')
        seed, image = generate_image(prompt, steps, seed=seed)
        filepath = uniquify(filename)
        image.save(filepath)
        print(f'Seed used: {seed}\n')
        with open('Images/log.txt', 'a') as log:
            log.write(f'{time.time()}, ')
            log.write(f'{choice}, ')
            log.write(f'{steps}, ') 
            log.write(f'{prompt}, ')
            log.write(f'{seed}, ')
            log.write(f'{filepath}\n')
        choice = get_next_step()
        if choice == EXIT:
            exit()
