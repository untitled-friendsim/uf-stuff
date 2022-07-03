#!/usr/bin/env python3

import os
import shutil

def init():
    os.system('git submodule init')

def update():
    os.system('git submodule update')

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
        case 'update':
            update()
        case 'copy':
            copy()
        case 'run':
            run()

if __name__ == '__main__':
    main()