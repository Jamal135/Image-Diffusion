# Image-Diffusion

***
# About:
---
So, like you (probably), I thought all this AI image generation stuff was pretty cool. I also didn't find it as cool that many of the websites and platforms that provide image generation want me to pay. So I settled on Hugging Face stable diffusion and implemented some of my own code to use it nicely.
Link: https://huggingface.co/blog/stable_diffusion

Do note, my hardware is crap. So if you are by chance using my code and have an over-powered PC... you will want to look at changing the revision and torch dtype arguments for the stable diffusion pipeline code (you get better results). Pretty big pretense though, no matter how baller your PC is you will get terrible images if you use terrible prompts. So I strongly recommend you do some research or use some of the many good image generation prompts that exist across the internet.

Now obviously no image generation repository would be complete without some examples! In the interest of showing you some realistic results, these aren't examples that I have slaved away for hours to make. These are examples I got very easily with somewhat well constructed prompts:

![alt text]()

![alt text]()

![alt text]()

![alt text]()

Creation Date: 06/11/2022

***
# Setup:
---
There is no two ways about it, setting this up is a right pain. If you are lucky, the setup.py script I wrote will assist in automating much of the setup for you, though it very well may break or otherwise not work for you as frankly writing bullet-proof setup code is well beyond my abilities. I tried. Some notes as well, if your computer is particularly terrible and does not have a compatible GPU that allows for CUDA enabled stuff (whatever that is) then I am sorry this repository will not work for you. It is a hardware requirement completely beyond my control.

You also require a Hugging Face token, so create a Hugging Face account and then create a read only token (don't worry it is free). 
Link: https://huggingface.co/settings/tokens

None the less here are the main things you need to do (in theory) to get this repository working for you:
```
1:  Virtual Environment: Don't risk not having one, trust me. The setup.py will use virtualenv, you can use whatever.
2:  Install Dependencies: They are all in the requirements.txt, get them all installed. pip install -r requirements.txt
3:  CUDA Enabled Torch: Frankly this is a mess, if setup.py doesn't work goodluck. Make sure PyTorch is CUDA enabled.
4:  Environment Variable: Through setup.py or manually, you must create a .env 'TOKEN=' a Hugging Face read token.
5:  Developer Mode: If using Windows, activate developer mode. Or (if you prefer) always execute cli.py as admin.
6:  GPU Drivers: Even if your GPU is compatible, make sure you have the latest/suitable drivers installed.
--- Most Importantly ---
7:  Pray: Honestly Python is always a dependency mess but this stuff is particularly bad, best of luck.
```

***
# Acknowledgements:
---
McJeffr is always a legend helping me with these projects, what a smart cookie!
Link: https://github.com/McJeffr

A lot of StackOverflow posts certainly helped as well as always. Official Python Discord is great as well.

***
# Future:
---
I make no promises regarding the future of this repository beyond that I will probably fix issues. This having been said, I do hope to explore more AI generation technology including audio and text generation as well as text summarization. So they very well may be integrated into the CLI/scope of this repository. I am also pretty confident that I will explore integrating more advanced models as they develop across the community!

***
# License:
---
MIT License.
