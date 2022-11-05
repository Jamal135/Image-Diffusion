''' Creation Date: 27/09/2022 '''

import torch
from os import getenv
from dotenv import load_dotenv
from random import randint
from pathlib import Path
from torch import autocast, Generator
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler


def get_env_variable(variable: str):
	''' Returns: Loaded .env file variable. '''
	load_dotenv() 
	return getenv(variable)


def create_pipeline():
	''' Returns: Diffusion Pipeline object. '''
	TOKEN = get_env_variable('TOKEN') # Generate token here: https://huggingface.co/
	try:
		scheduler = LMSDiscreteScheduler(
			beta_start=0.00085, 
			beta_end=0.012, 
			beta_schedule='scaled_linear', 
			num_train_timesteps=1000
		)
		return StableDiffusionPipeline.from_pretrained(
			'CompVis/stable-diffusion-v1-4',
			scheduler=scheduler,
			revision='fp16',
			torch_dtype=torch.float16,
			use_auth_token=TOKEN
		).to('cuda')
	except Exception as e:
		print(e)
		exit()


def uniquify(filename: str):
	''' Returns filepath modified if needed to ensure it doesn't already exist. '''
	counter = 1
	filepath = Path(f'Images/{filename}.png')
	while filepath.is_file():
		filepath = Path(f'Images/{filename + "-" + str(counter)}.png') 
		counter += 1
	return filepath


def generate_image(prompt: str, steps: int = 50, filename: str = None, seed: int = None):
	''' Purpose: Creates and saves image from provided prompt. '''
	if filename == None:
		filename = 'result'
	if seed == None:
		seed = randint(0, 999999999999999999)
	pipe = create_pipeline()
	pipe.enable_attention_slicing()
	generator = Generator('cuda').manual_seed(seed)
	with autocast('cuda'):
		image = pipe(
			prompt, 
			guidance_scale=7.5, 
			num_inference_steps=steps,
			generator=generator
		)['sample'][0]
	filepath = uniquify(filename)
	image.save(filepath)
	return seed
