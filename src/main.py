import cli
from platform import system
from cubase import Cubase


def main():
    cli.parser.parse_args()

    cubase = Cubase()
    print(cubase.default_location)
    # print(cubase.installations)
    # print(cubase.is_open)



if __name__ == "__main__":
    if system() != "Darwin" or system() != "Windows":
        print(f"{system()} is not supported!")
    else:
        main()
