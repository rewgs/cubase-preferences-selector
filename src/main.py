import cli
from platform import system
from cubase import CubaseApp, CubasePreferences


def main():
    cli.parser.parse_args()

    cubase = CubaseApp()
    prefs = CubasePreferences()

    print(cubase.default_path)



if __name__ == "__main__":
    main()
