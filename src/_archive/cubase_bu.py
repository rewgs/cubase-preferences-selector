from pathlib import Path
from pathlib import PurePath
from platform import system
from types import NoneType
from dataclasses import dataclass
import psutil


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
        self.is_open: bool = self.__check_if_open()


    def __get_default_location(self) -> Path:
        default_location: Path = Path(PurePath(Path.home().root))

        if system() == "Darwin":
            default_location = default_location.joinpath("Applications")
        # TODO:
        elif system() == "Windows":
            pass

        try:
            default_location.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return default_location.resolve(strict=True)


    def __get_installations(self) -> list[CubaseApp]:
        installations: list[CubaseApp] = []

        app_paths = [file for file in self.default_location.iterdir() if file.is_dir() and "Cubase" in file.name]
        for p in app_paths:
            extracted_number: list = [char for char in p.stem.split() if char.isdigit()]
            version_number = int(extracted_number[0])
            installation = CubaseApp(p, version_number)
            installations.append(installation)

        return installations

    def __check_if_open(self) -> bool:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            if "Cubase" in proc.name() and proc.is_running():
                return True
        return False
