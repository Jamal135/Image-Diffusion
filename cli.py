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
LOOP = 'Loop'
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
                        choices = [25, 50, 75, 100, 250, 750, 'Custom'],
                        default = 50)
    if steps == 'Custom':
        steps = inquirer.text(
                        message = f'Enter number steps',
                        validate = check_steps
        )
    return int(steps)


def check_prompt(prompt: str):
    ''' Purpose: Validates prompt input text. '''
    if prompt == '':
        print('Please enter a prompt...')
    return True


def get_prompt():
    ''' Returns: String input for image generation. '''
    while True:
        prompt = input('Describe image: ')
        if check_prompt:
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
            print(f'\nGenerating image {count + 1}/{iterations}...')
            create_image(None, choice)
        return get_next_step()
    return choice


def uniquify(filename: str):
	''' Returns filepath modified if needed to ensure it doesn't already exist. '''
	counter = 1
	filepath = Path(f'Images/{filename}.png')
	while filepath.is_file():
		filepath = Path(f'Images/{filename + "-" + str(counter)}.png') 
		counter += 1
	return filepath


def create_image(seed: int, choice: str):
    ''' Purpose: Updates log file and called image generation. '''
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
    return seed


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
        print(f'\nGenerating image...')
        seed = create_image(seed, choice)
        choice = get_next_step()
        if choice == EXIT:
            exit()

