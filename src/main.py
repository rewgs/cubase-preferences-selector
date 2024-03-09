from pathlib import Path, PurePath

from cpm import Cubase, PreferencesManager


def main():
    cb = Cubase()
    # cb_prefs = PreferencesManager()
    cb.list_all_apps()


if __name__ == "__main__":
    main()
