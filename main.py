import pathlib
import shutil
import sys

import configs


def main():
    specified_config = configs.get_config(sys.argv)
    print(specified_config)

    breakpoint()

    # backups = pathlib.PurePath.joinpath(configs.default_config, "_backups")

    to_swap = [
        # as strings
        'Presets',
        # 'Click Sound Sets',
        # 'KeyCommands',
        # 'Logical Edit',
        # 'Project Logical Editor',
        'Clickset Presets.xml',
        'Key Commands.xml',
        'Profile Manager.xml',
        'UserPreferences.xml',

        # as pathlib objects
        # pathlib.PurePath('Presets', 'Click Sound Sets'),
        # pathlib.PurePath('Presets', 'KeyCommands'),
        # pathlib.PurePath('Presets', 'Logical Edit'),
        # pathlib.PurePath('Presets', 'Project Logical Editor'),
        # pathlib.PurePath('Clickset Presets.xml'),
        # pathlib.PurePath('Key Commands.xml'),
        # pathlib.PurePath('Profile Manager.xml'),
        # pathlib.PurePath('UserPreferences.xml')
        # ['Presets', 'Click Sound Sets'],
        # ['Presets', 'KeyCommands'],
        # ['Presets', 'Logical Edit'],
        # ['Presets', 'Project Logical Editor'],
    ]    

    # if one in configs.default_config is a file or folder, back up
    # else if it's a link, delete the link
    # symlink from specified_config to configs.default_config
    # MAKE SURE that we're linking TO the user config FROM the default folder, not the other way around

    default_items = []
    for d in pathlib.Path.iterdir(configs.default_config):
        default_items.append(d.name)

    user_items = []
    for u in pathlib.Path.iterdir(specified_config['path']):
        user_items.append(u.name)

    for item in to_swap:
        if item in default_items and item in user_items:
            default_item = pathlib.Path(pathlib.PurePath.joinpath(configs.default_config, item)).resolve()
            user_item = pathlib.Path(pathlib.PurePath.joinpath(specified_config['path'], item)).resolve()

            # if not default_item.is_dir() or not default_item.is_file() or not default_item.is_symlink():
            #     print('Taking the if not')
            #     print(f'Something weird just happened. {default_item} is apparently not a directory, file, or symbolic link.')
            #     return

            if default_item.is_dir():
                print(f'{default_item} is a dir')
                backup_dst = pathlib.Path(pathlib.PurePath.joinpath(backups, item))
                if not backup_dst.exists():
                    pathlib.Path.mkdir(backups, parents=True, exist_ok=True)
                shutil.move(default_item, backup_dst)
                default_item.symlink_to(user_item, target_is_directory=True)

            elif default_item.is_file():
                print(f'{default_item} is a file')
                backup_dst = pathlib.Path(pathlib.PurePath.joinpath(backups, item))
                if not backup_dst.exists():
                    pathlib.Path.mkdir(backups, parents=True, exist_ok=True)
                shutil.move(default_item, backup_dst)
                default_item.symlink_to(user_item, target_is_directory=False)

            elif default_item.is_symlink():
                print(f'{default_item} is a symlink')
                if user_item.is_dir():
                    default_item.rmdir()
                    default_item.symlink_to(user_item, target_is_directory=True)
                elif user_item.is_file():
                    default_item.unlink(missing_ok=True)
                    default_item.symlink_to(user_item, target_is_directory=False)

            else:
                print('Taking the else')
                print(f'Something weird just happened. {default_item} is apparently not a directory, file, or symbolic link.')
                return


    # debug; can comment out
    # for config in user_configs:
    #     user = config['user']
    #     nickname = config['nickname']
    #     path = pathlib.Path(config['path'])

    #     if user == specified_config or nickname == specified_config: 
    #         if path.exists:
    #             print(f'The Cubase config for {user} is located at {path}.')
    #         else:
    #             print(f'The Cubase config for {user} cannot be found at {path}.')


if __name__ == '__main__':
    main()
