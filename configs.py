import pathlib

# import sys


version = "12"

# Cubase default location; this must remain hard-coded and unchangeable
# TODO: once I make this app cross-platform, automatically define this based on OS
default_config = pathlib.Path(
    pathlib.PurePath.joinpath(
        pathlib.Path.home(), "Library", "Preferences", f"Cubase {version}"
    )
).absolute()

# hard-coding these to my machine for now, but once a GUI is added, allow users
# to browse to them, save presets containing one or more locations to their
# machine, etc
user_configs = [
    {
        "user": "Alex Ruger",
        "nickname": "rewgs",
        "path": pathlib.Path(pathlib.PurePath().joinpath(pathlib.Path.home(), ".config", "cubase-preferences",f"Cubase {version}")).absolute()
    },
    {
        "user": "Sparks and Shadows",
        "nickname": "sns",
        "path": pathlib.Path(pathlib.PurePath().joinpath(pathlib.Path.home(), "work", "sns", "development", "cubase-preferences", f"Cubase {version}")).absolute()
    },
]


def get_config(args):
    if len(args) > 2:
        print("Too many arguments. Only one argument allowed.")
        get_config(args)
    elif len(args) < 2:
        print("Not enough arguments. Please enter the name or nickname of a Cubase config.")
        get_config(args)
    else:
        checked_configs = []
        specified_config = args[1]

        if len(checked_configs) == len(user_configs):
            # TODO: only recursively call this function when asking for user input;
            # otherwise the first instance of invalid input causes it to run
            # forever and crash
            # print(f'{specified_config} not found. Please try again.')
            # get_config(args)
            print("The following configs were checked and were not found:")
            for config in checked_configs:
                print(f"{config}")
            print("Please check your config paths and try again. Exiting now.")
        else:
            for config in user_configs:
                if (specified_config == config["user"] or specified_config == config["nickname"]) and config["path"].exists():
                    return config["path"]
                else:
                    checked_configs.append(config)
