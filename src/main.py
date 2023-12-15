import cli
from platform import system
from cubase import Cubase


def main():
    if system() != "Darwin" or system() != "Windows":
        print(f"{system()} is not supported!")
    else:
        cli.parser.parse_args()

        cubase = Cubase()
        print(cubase.default_location)
        # print(cubase.installations)
        # print(cubase.is_open)



if __name__ == "__main__":
    main()
