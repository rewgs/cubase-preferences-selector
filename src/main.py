import cli
from platform import system
from cubase import CubaseApp, CubasePreferences


def main():
    cli.parser.parse_args()

    cubase = CubaseApp()
    print(cubase.default_path)

    prefs = CubasePreferences()
    # for p in prefs.default:
    #     print(p)




if __name__ == "__main__":
    main()
