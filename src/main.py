from pathlib import Path, PurePath

from cpm import Cubase, PreferencesManager


def main():
    cb = Cubase()
    # cb_prefs = PreferencesManager()
    print(cb.is_open())


if __name__ == "__main__":
    main()
