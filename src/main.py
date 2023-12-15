import cli
from configs import Cubase


def main():
    cli.parser.parse_args()

    cubase = Cubase()
    print(cubase.installations)



if __name__ == "__main__":
    main()
