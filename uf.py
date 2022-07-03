#!/usr/bin/env python3

import os
import shutil
import wget

def init():
    os.system('git submodule init')


def update():
    os.system('git submodule update')


def get_sdk():
    renpy_url = "https://www.renpy.org/dl/%ver%/renpy-%ver%-sdk.zip"
    renpy_ver = "8.0.0"

    renpy_dl  = renpy_url.replace("%ver%", renpy_ver)
    renpy_f   = renpy_dl.split('/').pop()
    
    wget.download(
        renpy_dl,
        renpy_f
    )

    renpy_f.extractall("renpy/")

    shutil.rmtree(renpy_f)
    

def copy():
    vol_path = "fansim-engine/custom_volumes"
    art_path = "fansim-engine/skins"

    shutil.rmtree(vol_path)
    shutil.rmtree(art_path)
    
    shutil.copy("custom_volumes", vol_path)
    shutil.copy("skins", art_path)    


def run():
    os.system('python3 renpy/renpy.py')


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
        case 'run':
            run()


if __name__ == '__main__':
    main()