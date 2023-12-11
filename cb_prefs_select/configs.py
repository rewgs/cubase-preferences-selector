from pathlib import Path
from pathlib import PurePath
from platform import system
from types import NoneType

# Cubase default location; this must remain hard-coded and unchangeable
# TODO: once I make this app cross-platform, automatically define this based on OS
# default_config = Path(PurePath.joinpath(Path.home(), "Library", "Preferences", f"Cubase {version}")).resolve(strict=True)

# hard-coding these to my machine for now, but once a GUI is added, allow users
# to browse to them, save presets containing one or more locations to their
# machine, etc
# user_configs: list = [
#     {
#         "user": "Alex Ruger",
#         "nickname": "rewgs",
#         "path": Path(PurePath().joinpath(Path.home(), ".config", "cubase-preferences",f"Cubase {version}")).absolute()
#     },
#     {
#         "user": "Sparks and Shadows",
#         "nickname": "sns",
#         "path": Path(PurePath().joinpath(Path.home(), "work", "sns", "development", "cubase-preferences", f"Cubase {version}")).absolute()
#     },
# ]


# def get_config(args):
#     checked_configs = []
#     specified_config = args[1]

#     if len(checked_configs) == len(user_configs):
#         # TODO: only recursively call this function when asking for user input; otherwise the first instance of invalid input causes it to run forever and crash

#         # print(f'{specified_config} not found. Please try again.')
#         # get_config(args)

#         print("The following configs were checked and were not found:")
#         for config in checked_configs:
#             print(f"{config}")
#         print("Please check your config paths and try again. Exiting now.")
#     else:
#         for config in user_configs:
#             if (specified_config == config["user"] or specified_config == config["nickname"]) and config["path"].exists():
#                 return config["path"]
#             else:
#                 checked_configs.append(config)


# TODO: Implement behavior for `version` != None
def get_stock_config(version: int | NoneType = None) -> Path | bool:
    """
    Checks for the stock Cubase preferences location on both macOS and Windows.
    If found, returns Path object; if not, returns False.
    If multiple Cubase versions are present, default behavior is to return only the most recent, 
    but this behavior can be overridden by passing a value to the argument `version`.
    """

    if system() == "Darwin":
        stock_prefs_location = Path(PurePath.joinpath(Path.home(), "Library", "Preferences"))
        stock_configs = [file for file in stock_prefs_location.iterdir() if file.is_dir and "Cubase" in file.name]
        if len(stock_configs) == 1: 
            return stock_configs[0]
        else:
            # This is a nested list comprehension. Gets the numbers from each config in stock_configs, 
            # and then packs those into a single list called version_nums.
            version_nums: list = [ [int(char) for char in config.name.split() if char.isdigit()] for config in stock_configs ]

            newest_version = max(version_nums)[0] # `version_nums` is a single-member list
            for config in stock_configs:
                if str(newest_version) in config.name:
                    return config.resolve(strict=True)
    elif system() == "Linux":
        ...
    elif system() == "Windows":
        ...
    else:
        return False

