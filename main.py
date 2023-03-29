import pathlib
import sys


def main():
    args = sys.argv
    # for count, arg in enumerate(args):
    #     print(f'Arg {count}: {arg}')
    if len(args) > 2:
        print('Too many arguments. Only one argument allowed.')

    specified_config = args[1]

    version = '12'

    # Cubase default location; this must remain hard-coded and unchangeable
    # TODO: once I make this app cross-platform, automatically define this based on OS
    default_config = pathlib.PurePath.joinpath(pathlib.Path.home(), 'Library', 'Preferences', f'Cubase {version}')

    # hard-coding these to my machine for now, but once a GUI is added, allow users to browse to them, save presets containing one or more locations to their machine, etc
    user_configs = [
        {
            'user': 'Alex Ruger',
            'nickname': 'rewgs',
            'location': pathlib.PurePath().joinpath(pathlib.Path.home(), 'Cubase-preferences', f'Cubase {version}')
        },
        {
            'user': 'Sparks and Shadows',
            'nickname': 'sns',
            'location': pathlib.PurePath().joinpath(pathlib.Path.home(), 'work', 'sns', 'development', 'cubase-preferences', f'Cubase {version}')
        },
    ]

    # debug; can comment out
    for config in user_configs:
        user = config['user']
        nickname = config['nickname']
        location = pathlib.Path(config['location'])

        if user == specified_config or nickname == specified_config: 
            if location.exists:
                print(f'The Cubase config for {user} is located at {location}.')
            else:
                print(f'The Cubase config for {user} cannot be found at {location}.')

    # to_swap = [
    #     ['Presets', 'Click Sound Sets'],
    #     ['Presets', 'KeyCommands'],
    #     ['Presets', 'Logical Edit'],
    #     ['Presets', 'Project Logical Editor'],
    #     'Clickset Presets.xml',
    #     'Key Commands.xml',
    #     'Profile Manager.xml',
    #     'UserPreferences.xml',
    # ]    



if __name__ == '__main__':
    main()
