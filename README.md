# Image-Diffusion

***
# About:
---
So, probably like you, I thought all this AI image generation stuff was pretty cool. What wasn't as cool was that many of the websites that provide image generation want you to pay. So I settled on Hugging Face stable diffusion and implemented some of my own code to use it nicely for free!
Link: https://huggingface.co/blog/stable_diffusion

Do note, my hardware is crap. So if you by chance have an epic PC... you will want to look at changing the revision and torch dtype arguments for the stable diffusion pipeline code. Do note though, no matter how baller your PC is you will get terrible images if you use terrible prompts. So I strongly recommend you do some research or use some of the many good image generation prompts that have been shared across the internet.

Now obviously no image generation repository would be complete without some examples! In the interest of showing you some realistic results, these aren't examples that I have slaved away for hours to make. These are examples I got very easily with some average prompts:

<p align="center">
  <img src="https://github.com/Jamal135/Image-Diffusion/blob/main/media/example1.png?raw=true"/>
</p>
<p align="center">
  <img src="https://github.com/Jamal135/Image-Diffusion/blob/main/media/example2.png?raw=true"/>
</p>
<p align="center">
  <img src="https://github.com/Jamal135/Image-Diffusion/blob/main/media/example3.png?raw=true"/>
</p>
<p align="center">
  <img src="https://github.com/Jamal135/Image-Diffusion/blob/main/media/example4.png?raw=true"/>
</p>
<p align="center">
  <img src="https://github.com/Jamal135/Image-Diffusion/blob/main/media/example5.png?raw=true"/>
</p>
<p align="center">
  <img src="https://github.com/Jamal135/Image-Diffusion/blob/main/media/example6.png?raw=true"/>
</p>

Creation Date: 06/11/2022

***
# Setup:
---
There is no two ways about it, setting this up is a right pain. If you are lucky, the setup.py script I wrote will assist in automating much of the setup for you, though it very well may break as frankly writing bullet-proof setup code is well beyond my abilities. Additionally, if your computer is terrible and does not have a compatible GPU that allows for CUDA enabled stuff (whatever that means) then I am sorry this repository won't work for you. It is a hardware requirement completely beyond my control.

You also require a Hugging Face token, so create a Hugging Face account and then create a read only token (don't worry it is free). 
Link: https://huggingface.co/settings/tokens

None the less here are the main things you need to do (in theory) to get this repository working for you:
```
0:  Virtual Environment: Create a virtual environment (virtualenv .venv).
1:  Automatic Setup: Try use setup.py then just do steps 5, 6 & 7 (fingers crossed).
2:  Install Dependencies: All in the requirements.txt, 'pip install -r requirements.txt'.
3:  CUDA Enabled Torch: Frankly, if setup.py doesn't work goodluck. Get PyTorch CUDA enabled.
4:  Environment Variable: Must create a .env 'TOKEN=' a Hugging Face read token. Setup prompts.
5:  Developer Mode: If using Windows, activate developer mode. Or always run cli.py as admin.
6:  GPU Drivers: Even if your GPU is compatible, make sure you have the latest drivers.
--- Most Importantly ---
7:  Pray: Python is always a dependency mess but this stuff is particularly bad, best of luck.
```

If you have advice on how this setup process can be improved please do share! You may also need to change what CUDA enabled Torch version you are installing based on the hardware of your computer.
***
# Acknowledgements:
---
McJeffr is always a legend helping me with these projects, what a smart cookie!
Link: https://github.com/McJeffr

A lot of StackOverflow posts certainly helped. 
Also, the official Python Discord is great.

***
# Future:
---
I make no promises regarding the future of this repository. I will probably fix issues. This having been said, I do hope to explore more AI stuff including audio and text generation, maybe text summarization as well. So new stuff very well could be integrated into this repository. I am also pretty confident that I will explore integrating more advanced models as they are created by the wider community!

***
# License:
---
MIT License.
