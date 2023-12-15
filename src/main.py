import cli
from platform import system
import cubase


def main():
    cli.parser.parse_args()

    cubase_app = cubase.App()
    # print(cubase_app.default_location)

    # cubase_prefs = cubase.Preferences()
    # for p in cubase_prefs.default:
    #     print(p)




if __name__ == "__main__":
    main()
