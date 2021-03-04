import os

password = input('password (leave blank if none): ')
os.system('sudo snap install --classic code') #for distros with snap store
os.system('sudo apt install gdebi-core')
os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo apt install ./google-chrome-stable_current_amd64.deb')
os.system('wget ~/minecraft.deb https://launcher.mojang.com/download/Minecraft.deb')
os.system('sudo gdebi ~/minecraft.deb')
