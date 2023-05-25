# TODO: this is still deleting user files!!
# TODO: looks like Generic Remotes end up in the prefs folder too once imported...will need to account for those as well
    # maybe link to them in cubase-preferences/Generic Remotes folder (for sns)...will that work?
    # also, note that Generic Remote #1 is always called Generic Remote.xml

'''
    validate-stems: Moves silent stems from a given directory to their own
    subdirectory. Also alerts the user to any clipped files.

    This source code was originally written by Jacob Moss, and then was
    refactored and expanded upon by Alex Ruger.

'''

__author__ = ['Alex Ruger']
__copyright__ = f"Copyright 2022, {__author__}"
__deprecated__ = False
# __email__      = ''
# __license__    = 'TBD'
__maintainer__ = "Alex Ruger"
__status__ = "production"
__version__ = "0.0.1"


import os
import sys
# import shutil
import pathlib
import PySimpleGUI as sg

import configs
import gui


def main():
    window = gui.make_window()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Exit":
            break

    user_config = configs.get_config(sys.argv)

    default_items = []
    for d in pathlib.Path.iterdir(configs.default_config):
        default_items.append(d.name)

    user_items = []
    for u in pathlib.Path.iterdir(user_config):
        user_items.append(u.name)

    to_swap = [
        'Presets',
        'Clickset Presets.xml',
        'Key Commands.xml',
        'Profile Manager.xml',
        'UserPreferences.xml',
    ]    

    for item in to_swap:
        if item in user_items:
            user_item = pathlib.Path(pathlib.PurePath.joinpath(user_config, item)).resolve()

            if item in default_items:
                default_item = pathlib.Path(pathlib.PurePath.joinpath(configs.default_config, item))
                # if default_item.exists():
                #     print(f'{default_item} exists!')

                if default_item.is_symlink():
                    # print(f'DEBUG: {default_item} is a symlink')
                    if default_item.is_dir():
                        # print(f'{default_item} is a dir')
                        
                        '''
                        Using `os` instead of `pathlib` here because pathlib's rmdir() doesn't 
                        work as expected. The documentation states that rmdir() can delete links 
                        to directories, but it just...doesn't work. Seems that it always expects 
                        a directory, period.
                        On the other hand, os.unlink() works just fine.
                        '''
                        os.unlink(default_item)
                        default_item.symlink_to(user_item, target_is_directory=True)
                    if default_item.is_file():
                        # print(f'{default_item} is a file')
                        default_item.unlink(missing_ok=True)
                        default_item.symlink_to(user_item, target_is_directory=False)
                else:
                    print('placeholder')
                    if default_item.is_dir():
                        # print(f'DEBUG: {default_item} is a dir')
                        default_item.rmdir
                        default_item.symlink_to(user_item, target_is_directory=True)

                    elif default_item.is_file():
                        # print(f'DEBUG: {default_item} is a file')
                        default_item.symlink_to(user_item, target_is_directory=False)

            # this branch runs if the default Cubase config is incomplete for some reason
            elif item not in default_items:
                default_item = pathlib.PurePath.joinpath(configs.default_config, item)
                if user_item.is_dir():
                    # print(f'{user_item} is a dir')
                    default_item.symlink_to(user_item, target_is_directory=True)
                elif user_item.is_file():
                    # print(f'{user_item} is a file')
                    default_item.symlink_to(user_item, target_is_directory=False)
                else:
                    print(f'{user_item} is neither a directory nor a file. Not sure what to do with this. Exiting.')
                    exit()

            else:
                print('Unexpected behavior. Exiting.')
                exit()


if __name__ == '__main__':
    main()
