import cli
from cubase import Cubase


def main():
    cli.parser.parse_args()

    cubase = Cubase()
    # print(cubase.installations)
    print(cubase.is_open)



if __name__ == "__main__":
    main()
