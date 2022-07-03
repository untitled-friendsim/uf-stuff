#!/usr/bin/env python3

import os
import shutil
import sys
import wget
import zipfile

renpy_ver = "7.5.0"

def init():
    os.system('git submodule update --init --recursive --progress')


def update():
    os.system('git submodule update --recursive --progress')


def get_sdk():
    renpy_url = "https://www.renpy.org/dl/%ver%/renpy-%ver%-sdk.zip"

    renpy_dl  = renpy_url.replace("%ver%", renpy_ver)
    renpy_f   = renpy_dl.split('/').pop()

    print(renpy_dl + "\n" + renpy_f)
        
    wget.download(
        renpy_dl,
        renpy_f
    )

    with zipfile.ZipFile(renpy_f) as zip:
        zip.extractall()

    os.remove(renpy_f)
    

def copy():
    path = os.getcwd()
    
    print(path)
    
    os.chdir("fansim-engine")
    os.system("git reset --hard HEAD")
    os.system("git clean -dfx")
    os.chdir(path)
    
    vol_path = "./fansim-engine/custom_volumes/"
    art_path = "./fansim-engine/skins/"
    
    for vol in os.scandir("{}/custom_volumes".format(path)):
        shutil.copytree(vol, vol_path + vol.name)
    
    for art in os.scandir("{}/skins".format(path)):
        shutil.copytree(art, art_path + art.name)


def build():
    path = os.getcwd()
    
    os.chdir("./fansim-engine/src")
    os.system("python run_wizard.py --clean --skins untitled-friendsim")
    os.chdir(path)



def run():
    renpy_path = "renpy-{}-sdk".format(renpy_ver)
    os.system("{}/renpy.sh fansim-engine/projects/work".format(renpy_path))


def main():
    arg = sys.argv[1]
    
    if arg == 'init':
        init()
        update()
        get_sdk()
    elif arg == 'update':
        update()
    elif arg == 'copy':
        copy()
    elif arg == 'build':
        build()
    elif arg == 'run':
        run()
    else:
        pass


if __name__ == '__main__':
    main()