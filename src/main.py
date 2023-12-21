import cli
from platform import system
from cubase import Cubase, App, Preferences


def main():
    # cli.parser.parse_args()

    cubase = Cubase()
    cubase_13 = cubase.get_by_version(13)
    print(cubase_13)





if __name__ == "__main__":
    main()
