import pathlib
import os
import shutil
import sys

import configs


def main():
    specified_config = configs.get_config(sys.argv)

    to_swap = [
        'Presets',
        'Clickset Presets.xml',
        'Key Commands.xml',
        'Profile Manager.xml',
        'UserPreferences.xml',
    ]    

    default_items = []
    for d in pathlib.Path.iterdir(configs.default_config):
        default_items.append(d.name)

    user_items = []
    for u in pathlib.Path.iterdir(specified_config['path']):
        user_items.append(u.name)

    for item in to_swap:
        if item in user_items:
            user_item = pathlib.Path(pathlib.PurePath.joinpath(specified_config['path'], item)).resolve()

            if item in default_items:
                default_item = pathlib.Path(pathlib.PurePath.joinpath(configs.default_config, item))
                # if default_item.exists():
                #     print(f'{default_item} exists!')

                if default_item.is_symlink():
                    print(f'{default_item} is a symlink')
                    if default_item.is_dir():
                        # print(f'{default_item} is a dir')

                        # Using `os` instead of `pathlib` here because pathlib's rmdir() doesn't 
                        # work as expected. The documentation states that rmdir() can delete links 
                        # to directories, but it just...doesn't work. Seems that it always expects 
                        # a directory, period.
                        # On the other hand, os.unlink() works just fine.
                        os.unlink(default_item)
                        # default_item.symlink_to(user_item, target_is_directory=True)
                    if default_item.is_file():
                        # print(f'{default_item} is a file')
                        default_item.unlink(missing_ok=True)
                    #     default_item.symlink_to(user_item, target_is_directory=False)
                else:
                    print('placeholder')
                    # if default_item.is_dir():
                    #     print(f'{default_item} is a dir')
                    #     default_item.rmdir
                    #     default_item.symlink_to(user_item, target_is_directory=True)

                    # elif default_item.is_file():
                    #     print(f'{default_item} is a file')
                    #     default_item.symlink_to(user_item, target_is_directory=False)

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
