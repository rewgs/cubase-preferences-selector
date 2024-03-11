from dataclasses import dataclass
from pathlib import Path, PurePath
from platform import system
from types import NoneType

import psutil


@dataclass(repr=True)
class CubaseApp:
    """
    A single Cubase application installation (i.e. one for Cubase 12, another for Cubase 13, etc).
    """
    path: Path
    version: int


class Cubase:
    """
    Concerned with an abstract notion of Cubase -- the various application versions installed, whether any of said applications are open, etc.
    """

    @staticmethod
    def __get_installed_apps() -> list[CubaseApp]:
        def get_default_path() -> Path:
            system_root: Path = Path(PurePath(Path.home().root))

            if system() == "Darwin":
                return system_root.joinpath("Applications")
            elif system() == "Linux":
                program_files = system_root.joinpath("mnt", "c", "Program Files")

                class NotWsl(Exception):
                    """Raises a basic exception if not running on WSL."""

                def running_on_wsl(test_path: Path) -> bool:
                    try:
                        test_path.resolve(strict=True)
                    except FileNotFoundError:
                        return False
                    else:
                        return True

                if not running_on_wsl(program_files):
                    raise NotWsl(f"Expected to find {program_files.as_posix()}, but didn't. Are you running this on WSL?")

                return program_files.joinpath("Steinberg")

            # TODO:
            elif system() == "Windows":
                pass
            else:
                class WrongOsBuddy(Exception):
                    """Raises a basic exception if running on the wrong system."""
                raise WrongOsBuddy(f"This app is not designed to run on {system()}!")

        default_path = get_default_path()
        try:
            default_path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            installations: list[CubaseApp] = []
            app_paths = [file for file in get_default_path().iterdir() if file.is_dir() and "Cubase" in file.name]
            for p in app_paths:
                extracted_number: list = [char for char in p.stem.split() if char.isdigit()]
                version_number = int(extracted_number[0])
                app = CubaseApp(p, version_number)
                installations.append(app)
            return installations

    def __get_latest_version(self) -> CubaseApp:
        version_nums = [i.version for i in self.apps]
        latest_version_num = max(version_nums)
        latest = [i for i in self.apps if str(latest_version_num) in i.path.stem]
        return latest[0]

    def __init__(self):
        self.apps: list[CubaseApp] = self.__get_installed_apps()
        self.latest: CubaseApp = self.__get_latest_version()

    def __str__(self):
        return "test"

    def get_by_version(self, version: int) -> CubaseApp | NoneType:
        for app in self.apps:
            if app.version == version:
                return app
        return None

    def is_open(self, version: int | NoneType = None) -> bool:
        """
        Checks if Cubase is open. If version is supplied, only that version is checked.
        """
        if version is not None:
            for proc in psutil.process_iter(["pid", "name", "username"]):
                if f"Cubase {str(version)}" in proc.name() and proc.is_running():
                    return True
        else:
            for proc in psutil.process_iter(["pid", "name", "username"]):
                if "Cubase" in proc.name() and proc.is_running():
                    return True
        return False

    def list_all_apps(self):
        for app in self.apps:
            print(app)
