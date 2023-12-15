from pathlib import Path
from pathlib import PurePath
from platform import system
from types import NoneType
from dataclasses import dataclass
import psutil


@dataclass
class Installation:
    """A specific instance of an installation of Cubase"""

    path: Path
    version: int


@dataclass
class CubasePref:
    """
    A single instance of Cubase preferences, either default or custom.
    """

    name: str
    version: int
    description: str
    default: bool # False for custom
    main_prefs_path: Path
    user_preset_path: Path
    associated_installation: Installation


class App:
    def __init__(self):
        self.default_path: Path = self.__get_default_main_prefs()
        self.installations: list[Installation] = self.__get_installations()
        self.is_open: bool = self.__check_if_open()

    def __get_default_main_prefs(self) -> Path:
        default_path: Path = Path(PurePath(Path.home().root))

        if system() == "Darwin":
            default_path = default_path.joinpath("Applications")
        # TODO:
        elif system() == "Windows":
            pass

        try:
            default_path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return default_path.resolve(strict=True)

    def __get_installations(self) -> list[Installation]:
        installations: list[Installation] = []

        app_paths = [
            file
            for file in self.default_path.iterdir()
            if file.is_dir() and "Cubase" in file.name
        ]
        for p in app_paths:
            extracted_number: list = [char for char in p.stem.split() if char.isdigit()]
            version_number = int(extracted_number[0])
            installation = Installation(p, version_number)
            installations.append(installation)

        return installations

    def __check_if_open(self) -> bool:
        for proc in psutil.process_iter(["pid", "name", "username"]):
            if "Cubase" in proc.name() and proc.is_running():
                return True
        return False


class Preferences:
    def __init__(self):
        self.default_main_path: Path = self.__get_default_main_path()
        self.default_user_path: Path = self.__get_default_user_path()
        self.default: list[CubasePref] = self.__get_default_preferences(App().installations)
        # self.custom_preferences: list[CubasePref] = custom_preferences
        # self.current: CubasePref = current

    def __get_default_main_path(self) -> Path:
        default_main_path: Path = Path(PurePath(Path.home()))

        if system() == "Darwin":
            default_main_path = default_main_path.joinpath("Library", "Preferences")
        # TODO:
        elif system() == "Windows":
            pass

        try:
            default_main_path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return default_main_path.resolve(strict=True)

    def __get_default_user_path(self) -> Path:
        default_user_path: Path = Path(PurePath(Path.home()).joinpath("Documents"))

        if system() == "Darwin":
            default_user_path = default_user_path.joinpath(
                "Steinberg", "Cubase", "User Presets"
            )
        # TODO:
        elif system() == "Windows":
            pass

        try:
            default_user_path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return default_user_path.resolve(strict=True)

    def __get_default_preferences(self, installations: list[Installation]) -> list[CubasePref] | None:
        default_prefs: list[CubasePref] = []

        for file in self.default_main_path.iterdir():
            if file.is_dir():
                for i in installations:
                    if file.name == i.path.stem:
                        try:
                            file.resolve(strict=True)
                        except FileNotFoundError as error:
                            raise error
                        else:
                            pref = CubasePref(
                                file.name,
                                i.version,
                                "",
                                True,
                                file.resolve(strict=True),
                                self.default_user_path,
                                i,
                            )
                            default_prefs.append(pref)
        return default_prefs


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
