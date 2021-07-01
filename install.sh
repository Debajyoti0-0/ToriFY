#!/bin/bash
#git clone https://github.com/Und3rf10w/kali-anonsurf
sudo apt-get install macchanger;sudo dnf install macchanger;sudo pacman -S macchanger
sudo apt-get install tor;sudo dnf install tor;sudo pacman -S tor
cd kali-anonsurf && chmod +x * && sudo ./installer.sh
