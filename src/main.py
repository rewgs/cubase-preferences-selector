import cli
from cpm import Cubase


def main():
    cb = Cubase()
    cli.parse(cb)


if __name__ == "__main__":
    main()
