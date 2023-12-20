from pathlib import Path
from pathlib import PurePath
from platform import system
from types import NoneType
from dataclasses import dataclass
import psutil


@dataclass
class App:
    """
    A specific instance of an App of Cubase.
    """

    path: Path
    version: int


@dataclass
class Pref:
    """
    A single instance of Cubase preferences, either default or custom.
    """

    name: str
    version: int
    description: str
    default: bool  # False for custom
    main_prefs_path: Path
    user_preset_path: Path
    associated_installation: App


class CubaseApp:
    def __init__(self):
        self.default_path: Path = self.__get_default_main_prefs()
        self.apps: list[App] = self.__get_installed_apps()
        self.is_open: bool = self.__check_if_open()
        self.newest: App = self.__get_newest_version()

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

    def __get_installed_apps(self) -> list[App]:
        installations: list[App] = []

        app_paths = [
            file
            for file in self.default_path.iterdir()
            if file.is_dir() and "Cubase" in file.name
        ]
        for p in app_paths:
            extracted_number: list = [char for char in p.stem.split() if char.isdigit()]
            version_number = int(extracted_number[0])
            app = App(p, version_number)
            installations.append(App)

        return installations

    def __check_if_open(self) -> bool:
        for proc in psutil.process_iter(["pid", "name", "username"]):
            if "Cubase" in proc.name() and proc.is_running():
                return True
        return False

    def __get_newest_version(self) -> App:
        version_nums = [i.version for i in self.apps]
        newest_version_num = max(version_nums)
        newest = [i for i in self.apps if str(newest_version_num) in i.path.stem]
        # print(newest)
        try:
            len(newest) == 1
        except Exception as error:
            raise error
        else:
            return newest[0]


class CubasePreferences:
    def __init__(self):
        self.default_main_path: Path = self.__get_default_main_path()
        self.default_user_path: Path = self.__get_default_user_path()
        # FIX: the use of CubaseApp() here smells...wrong. Perhaps this is a usecase for composition/inheritance?
        self.default: list[Pref] = self.__get_default_preferences(CubaseApp().apps)
        # self.custom_preferences: list[Pref] = custom_preferences
        # self.current: Pref = current

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

    def __get_default_preferences(self, installed_apps: list[App]) -> list[Pref] | None:
        default_prefs: list[Pref] = []

        for file in self.default_main_path.iterdir():
            if file.is_dir():
                for i in installed_apps:
                    if file.name == i.path.stem:
                        try:
                            file.resolve(strict=True)
                        except FileNotFoundError as error:
                            raise error
                        else:
                            pref = Pref(
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

    # read: https://realpython.com/python-json/
    def store_custom():
        pass

        
    # read: https://realpython.com/python-json/
    def read_custom():
        pass


    # TODO: version needs to be the most recent Cubase version instead of None...how to do?
    def add_custom(self, name: str, path: Path, version: int | NoneType = None, description: str | NoneType = None) -> Pref:
        try:
            path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            def resolve_associated_installation(version) -> App | NoneType:
                if version == None:
                    return None
                # else:
                    # return most recent App

            custom_pref_path = path.resolve(strict=True)

            # remaining attr declarations
            custom_pref_associated_installation = resolve_associated_installation(version)

            # FIX: the use of CubasePreferences() here smells...wrong. Perhaps this is a usecase for composition/inheritance?
            custom_pref_user_preset_path: Path = CubasePreferences().default_user_path

            custom_pref = Pref(
                name,
                version,
                description,
                False,
                custom_pref_path,
                custom_pref_user_preset_path,
                custom_pref_associated_installation
            )
