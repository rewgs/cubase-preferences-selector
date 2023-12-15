from pathlib import Path
from pathlib import PurePath
from platform import system
from types import NoneType
from dataclasses import dataclass


@dataclass
class CubasePref:
    """
    Defines a single instance of Cubase preferences, whether they be default or custom.
    """
    name: str
    description: str
    kind: str # default or custom
    main_prefs_path: Path
    user_preset_path: Path
    # version: CubaseApp # which Cubase version this is intended to work with


# TODO: merge most if not all of this with class Cubase
class Preferences:
    """
    Contains all default and custom Cubase preferences.
    """

    def __init__(self):
        self.default_location: Path = self.__get_default_location()
        self.default_preferences: list[CubasePref] = self.__get_default_preferences()
        # self.custom_preferences: list[CubasePref] = custom_preferences
        # self.current: CubasePref = current
        
    def __get_default_location(self) -> Path:
        default_location: Path = Path(PurePath(Path.home().root))

        if system() == "Darwin":
            default_location = default_location.joinpath("Library", "Preferences")
        # TODO:
        elif system() == "Windows":
            pass

        try:
            default_location.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return default_location.resolve(strict=True)

    def __get_default_preferences(self, installations: list[CubaseApp]) -> list[CubasePref]:
        default_prefs: list[CubasePref] = []

        prefs_paths = [file for file in self.default_location.iterdir() if file.is_dir() and "Cubase" in file.name]

    def add_custom(self):
        pass


# TODO: Implement behavior for `version` != None

# def get_default_cubase_prefs(version: int | NoneType = None) -> list | bool:
#     """
#     Checks for the default Cubase preferences location on both macOS and Windows.
#     If found, returns list of Path objects; if not, returns False.
#     If multiple Cubase versions are present, returns the most recent.
#     """

#     if system() == "Darwin":
#         default_prefs_location = Path(PurePath.joinpath(Path.home(), "Library", "Preferences"))
#         default_configs = [file for file in default_prefs_location.iterdir() if file.is_dir and "Cubase" in file.name]
#         return default_configs
#         # if len(default_configs) == 1:
#         #     return default_configs[0]
#         # else:
#     elif system() == "Linux":
#         ...
#     elif system() == "Windows":
#         ...
#     else:
#         return False


# def get_cubase_version_num(default_configs: list):
#     # This is a nested list comprehension. Gets the numbers from each config in default_configs,
#     # and then packs those into a single list called version_nums.
#     version_nums: list = [ [int(char) for char in config.name.split() if char.isdigit()] for config in default_configs ]

#     path_and_nums = []
#     for config in default_configs:
#         path_and_nums.append(dict(
#             path: Path = config,
#             version: int =
#         ))

#     # newest_version = max(version_nums)[0] # `version_nums` is a single-member list
#     # for config in default_configs:
#     #     if str(newest_version) in config.name:
#     #         return config.resolve(strict=True)
