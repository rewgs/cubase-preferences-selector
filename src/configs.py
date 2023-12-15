from pathlib import Path
from pathlib import PurePath
from platform import system
from types import NoneType
from dataclasses import dataclass

# class CubasePreferences:
#     """
#     Contains all default and custom Cubase preferences.
#     """

#     def __init__(self, default_main_prefs_location, default_user_presets_location, default_preferences, custom_preferences, current):
#         @dataclass
#         class CubasePref:
#             """
#             A single instance of Cubase preferences.
#             """
#             name: str
#             description: str
#             main_prefs_path: Path
#             user_preset_path: Path
#             version: int # which Cubase version this is intended to work with

#         self.default_main_prefs_location: Path = default_main_prefs_location
#         self.default_user_presets_location: Path = default_user_presets_location
#         self.default_preferences: list = default_preferences    # TODO: this should just be the return value of __get_all_default()
#         self.custom_preferences: list = custom_preferences
#         self.current: CubasePref = current

#     def __get_all_default(self):
#         """
#         Checks for the default Cubase preferences location on both macOS and Windows.
#         If found, returns list of Path objects.
#         If not found, checks if Cubase application is present.
#         If Cubase application is found, raises error that .
#         If multiple Cubase versions are present, returns the most recent.
#         """

#         try:
#             system() == "Darwin" or system() == "Windows"
#         except Exception as error:
#             raise error
#         else:
#             if system() == "Darwin":
#                 self.default_main_prefs_location = Path(PurePath.joinpath(Path.home(), "Library", "Preferences"))
#                 try:
#                     self.default_main_prefs_location.resolve(strict=True)
#                 except FileNotFoundError as error:
#                     raise error
#                 else:
#                     default_configs = [file for file in self.default_main_prefs_location.iterdir() if file.is_dir and "Cubase" in file.name]
#                     return default_configs

#             # if system() == "Windows":


@dataclass
class CubaseApp:
    """A specific instance of the application Cubase"""

    location: Path
    version: int


class Cubase:
    """Deals with the application of Cubase itself"""

    def __init__(self):
        self.default_location: Path = self.__get_default_location()
        self.installations: list[CubaseApp] = self.__get_installations()

    def __get_default_location(self):
        try:
            system() == "Darwin" or system() == "Windows"
        except Exception as error:
            raise error
        else:
            if system() == "Darwin":
                default_location: Path = Path(
                    PurePath(Path.home().root).joinpath("Applications")
                )
                return default_location
            # TODO:
            if system() == "Windows":
                pass

    def __get_installations(self):
        installations: list[CubaseApp] = []

        app_paths = [file for file in self.default_location.iterdir() if file.is_dir and "Cubase" in file.name]
        for p in app_paths:
            extracted_number: list = [char for char in p.stem.split() if char.isdigit()]
            version_number = int(extracted_number[0])
            installation = CubaseApp(p, version_number)
            installations.append(installation)

        return installations


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
