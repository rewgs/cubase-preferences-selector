import pathlib
import sys


version = '12'

# Cubase default location; this must remain hard-coded and unchangeable
# TODO: once I make this app cross-platform, automatically define this based on OS
default_config = pathlib.Path(pathlib.PurePath.joinpath(pathlib.Path.home(), 'Library', 'Preferences', f'Cubase {version}')).absolute()

# hard-coding these to my machine for now, but once a GUI is added, allow users to browse to them, save presets containing one or more locations to their machine, etc
user_configs = [
    {
        'user': 'Alex Ruger',
        'nickname': 'rewgs',
        'path': pathlib.Path(pathlib.PurePath().joinpath(pathlib.Path.home(), '.config', 'cubase-preferences', f'Cubase {version}')).absolute()
    },
    {
        'user': 'Sparks and Shadows',
        'nickname': 'sns',
        'path': pathlib.Path(pathlib.PurePath().joinpath(pathlib.Path.home(), 'work', 'sns', 'development', 'cubase-preferences', f'Cubase {version}')).absolute()
    },
]


def get_config(args):

    if len(args) > 2:
        print('Too many arguments. Only one argument allowed.')
    elif len(args) < 2:
        print('Please enter the name or nickname of a Cubase config.')
    else:
        for config in user_configs:
            if config['user'] == args[1] or config['nickname'] == args[1]:
                return args[1]
            else:
                print('Cubase config not found. Please try again.')
                get_config(args, user_configs)