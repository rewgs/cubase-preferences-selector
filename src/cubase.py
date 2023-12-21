from pathlib import Path
from pathlib import PurePath
from platform import system
from types import NoneType
from dataclasses import dataclass
import psutil


class App:
    """
    A single Cubase application installation (i.e. one for Cubase 12, another for Cubase 13, etc). 
    Composed from class Cubase?
    """

    def __init__(self, path, version):
        self.path: Path = path
        self.version: int = version

    def __repr__(self):
        return f"Cubase version {self.version} is called {self.path.name} and is located at {self.path}"

    def __str__(self):
        """
        This is a special function that runs when printing instances of this object, 
        e.g. cubase_13 = App(some_path, 13); print(cubase_13)
        """
        return f"Cubase version {self.version} is called {self.path.name} and is located at {self.path}"


class Cubase:
    """
    Primary class regarding Cubase.
    """

    def __get_installed_apps(self) -> list[App]:
        def get_default_path() -> Path:
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


        installations: list[App] = []
        app_paths = [file for file in get_default_path().iterdir() if file.is_dir() and "Cubase" in file.name]

        for p in app_paths:
            extracted_number: list = [char for char in p.stem.split() if char.isdigit()]
            version_number = int(extracted_number[0])
            app = App(p, version_number)
            installations.append(app)

        return installations

    def __get_newest_version(self) -> App:
        version_nums = [i.version for i in self.apps]
        newest_version_num = max(version_nums)
        newest = [i for i in self.apps if str(newest_version_num) in i.path.stem]
        return newest[0]

    def __init__(self):
        self.apps: list[App] = self.__get_installed_apps()
        self.newest: App = self.__get_newest_version()

    def __str__(self):
        return "test"

    def get_by_version(self, version: int) -> App | NoneType:
        for app in self.apps:
            if app.version == version:
                return app
        return None

    # TODO: make a version of this that checks if a specific version of Cubase is open; do this in class CubaseApp
    def is_open(self) -> bool:
        """
        Checks if *any* version of Cubase is open.
        """
        for proc in psutil.process_iter(["pid", "name", "username"]):
            if "Cubase" in proc.name() and proc.is_running():
                return True
        return False


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

class Preferences:
    """
    Deals with locating, storing, and creating Cubase preferences, both default and custom.
    """

    def __init__(self):
        self.default_main_path: Path = self.__get_default_main_path()
        self.default_user_path: Path = self.__get_default_user_path()
        # FIX: the use of Cubase() here smells...wrong. Perhaps this is a usecase for composition/inheritance?
        self.default: list[Pref] = self.__get_default_preferences(Cubase().apps)
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
    def store_custom(self):
        pass

        
    # read: https://realpython.com/python-json/
    def read_custom(self):
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
            custom_pref_user_preset_path: Path = Preferences().default_user_path

            custom_pref = Pref(
                name,
                version,
                description,
                False,
                custom_pref_path,
                custom_pref_user_preset_path,
                custom_pref_associated_installation
            )
