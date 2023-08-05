# FadeoutToSleep

### About

A program to fade out volume linearly and put the computer to standby mode (sleep). It's similar to "Final Countdown" program on Windows (with less features).
I made this for my own use, but I hope it helps other people to fall asleep easier also.

### Installation

**Use command:** ```sudo python3 -m pip install FadeoutToSleep```

*Or if you downloaded the source code yourself, extracted it and changed to its directory*: ```sudo python3 -m pip install .```

Not using "sudo" may install the program to a place where it can't be found automatically and you have to add path to there manually.

**You may need to install pip before that:**
For examble on Linux Mint or Ubuntu: ```sudo apt install pip```
And on EndeavourOS: ```sudo pacman -S python-pip```


### Usage

Run using command **FadeoutToSleep** as a normal user.

Add a shortcut to your desktop environment if you like. The way it's done varies so much that I won't give instructions here.

### Depencies

- Python >=3.4 with PIP (I'm not actually sure what specific version is the lower limit)
- PyGObject
- pulsectl (python-pulse-control)

And:
+ Linux with PulseAudio
+ Sound output on your computer

### Notes

Tested with only Linux Mint 20-21 Cinnamon, Ubuntu 22 and EndeavourOS 22.9. Should work on anything Gtk capable and using PulseAudio.
