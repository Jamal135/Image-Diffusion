''' Creation Date: 27/09/2022 '''

import torch
from os import getenv
from dotenv import load_dotenv
from torch import autocast
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
			beta_schedule="scaled_linear", 
			num_train_timesteps=1000
		)
		return StableDiffusionPipeline.from_pretrained(
			"CompVis/stable-diffusion-v1-4",
			scheduler=scheduler,
			revision="fp16",
			torch_dtype=torch.float16,
			use_auth_token=TOKEN
		).to("cuda")
	except Exception as e:
		print(e)
		exit()


def generate_image(prompt: str):
	''' Purpose: Creates and saves image from provided prompt. '''
	pipe = create_pipeline()
	pipe.enable_attention_slicing()
	with autocast("cuda"):
		image = pipe(prompt, guidance_scale=7.5, num_inference_steps=50)["sample"][0]  
	image.save("Images/senrio.png")


prompt = "Doomed environment, digital technology, pollution, climate disaster, concept art style"
generate_image(prompt)