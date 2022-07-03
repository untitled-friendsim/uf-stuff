#!/usr/bin/env python3

import os
import shutil
import sys
import wget
import zipfile

renpy_ver = "8.0.0"

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
    
    os.chdir("fansim-engine")
    os.system("git reset --hard HEAD")
    os.chdir(path)
    
    vol_path = "./fansim-engine/custom_volumes/"
    art_path = "./fansim-engine/skins/"
    
    for vol in os.listdir(vol_path):
        shutil.copytree(vol, vol_path)
    
    for art in os.listdir(art_path):
        shutil.copytree(art, art_path)    


def build():
    path = os.getcwd()
    
    os.chdir("./fansim-engine/src")
    os.system("python3 run_wizard.py --clean")
    os.chdir(path)



def run():
    renpy_path = "renpy-{}-sdk".format(renpy_ver)
    os.system("python3 ./{}/renpy.sh fansim-engine/projects/work")


def main():
    arg = sys.argv[1]
    
    match arg:
        case 'init':
            init()
            update()
            get_sdk()
        case 'update':
            update()
        case 'copy':
            copy()
        case 'build':
            build()
        case 'run':
            run()


if __name__ == '__main__':
    main()